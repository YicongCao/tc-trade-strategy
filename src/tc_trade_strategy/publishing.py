"""不可覆盖的报告、进程锁、只暂存报告及索引的 Git 发布。"""

import fcntl
import json
import subprocess
from contextlib import contextmanager
from datetime import UTC, datetime

from .evidence import digest
from .reporting import history_index, render


def git(root, *args, check=True):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout.strip()


@contextmanager
def run_lock(root):
    directory = root / "results/research-state"
    directory.mkdir(parents=True, exist_ok=True)
    with (directory / "run.lock").open("a+") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError("其他报告任务正在生成或发布；本次退出，不覆盖") from exc
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def all_reports(root):
    reports = []
    for path in (root / "reports").glob("*/*/*/evidence.json"):
        d = json.loads(path.read_text())
        reports.append((path, d))
    return sorted(reports, key=lambda pair: pair[1]["generated_at"])


def remote_contains(root, directory):
    relative = directory.relative_to(root).as_posix() + "/evidence.json"
    result = git(root, "show", "refs/remotes/origin/main:" + relative, check=False)
    if not result:
        return False
    return digest(json.loads(result)) == digest(
        json.loads((directory / "evidence.json").read_text())
    )


def published_period(root, mode, period):
    return any(
        d["window"]["mode"] == mode
        and d["window"]["period"] == period
        and remote_contains(root, p.parent)
        for p, d in all_reports(root)
    )


def save_report(root, data):
    """调用方持有 run_lock。索引若被人手改动，先保留而非覆盖。"""
    state_path = root / "results/research-state/index-hashes.json"
    hashes = json.loads(state_path.read_text()) if state_path.exists() else {}
    for name in ("index.md", "index.html"):
        path = root / "reports" / name
        clean_tracked = git(root, "ls-files", "--", "reports/" + name) and not git(
            root, "status", "--porcelain", "--", "reports/" + name
        )
        if path.exists() and hashes.get(name) != digest(path.read_text()) and not clean_tracked:
            raise RuntimeError("历史索引有未登记修改，保留原文件: " + str(path))
    w = data["window"]
    run = datetime.now(UTC).strftime("%Y%m%dT%H%M%S.%fZ")
    directory = root / "reports" / w["mode"] / w["period"] / run
    directory.mkdir(parents=True, exist_ok=False)
    md, page = render(data)
    (directory / "evidence.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    )
    (directory / "report.md").write_text(md)
    (directory / "index.html").write_text(page)
    history_index(root)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(
        json.dumps(
            {n: digest((root / "reports" / n).read_text()) for n in ("index.md", "index.html")}
        )
    )
    return directory


def publish(root, directory):
    """不修改报告内容。发布收据只留本地；origin/main 中存在才视为成功。"""
    directory = directory.resolve()
    relative = directory.relative_to(root).as_posix()
    if not relative.startswith("reports/") or not (directory / "evidence.json").is_file():
        raise ValueError("仅接受已生成报告目录")
    if git(root, "branch", "--show-current") != "main":
        raise RuntimeError("发布必须在 main；不自动切换或合并用户分支")
    if git(root, "diff", "--cached", "--name-only"):
        raise RuntimeError("暂存区已有变更，保留原状；请先处理再发布")
    data = json.loads((directory / "evidence.json").read_text())
    from .evidence import safe_public_data

    safe_public_data(data)
    expected_md, expected_html = render(data)
    if (directory / "report.md").read_text() != expected_md or (
        directory / "index.html"
    ).read_text() != expected_html:
        raise RuntimeError("报告与证据不一致，拒绝发布")
    paths = [relative + "/" + n for n in ("evidence.json", "report.md", "index.html")]
    paths += ["reports/index.md", "reports/index.html"]
    # 检查远端，但不自动 rebase/merge，也不自动把其他本地提交推送出去。
    git(root, "fetch", "origin", "main")
    upstream = git(root, "rev-parse", "refs/remotes/origin/main")
    head = git(root, "rev-parse", "HEAD")
    if upstream != head:
        ahead_files = git(root, "diff", "--name-only", upstream, head).splitlines()
        ancestor = (
            subprocess.run(
                ["git", "-C", str(root), "merge-base", "--is-ancestor", upstream, head],
                capture_output=True,
            ).returncode
            == 0
        )
        if not ancestor or any(not p.startswith("reports/") for p in ahead_files):
            raise RuntimeError("main 与远端分歧或含未推送的非报告提交，保留成果，停止发布")
    # 不额外暂存其他报告；索引引用的其他本地报告须已经进入当前提交树。
    for p, _ in all_reports(root):
        rel = p.relative_to(root).as_posix()
        if p.parent != directory and not git(root, "ls-files", "--", rel):
            raise RuntimeError("先发布索引中尚未入库的报告: " + str(p.parent))
    git(root, "add", "--", *paths)
    staged = git(root, "diff", "--cached", "--name-only").splitlines()
    if any(p not in paths for p in staged):
        raise RuntimeError("检测到并发暂存修改，停止提交")
    if staged:
        git(
            root,
            "commit",
            "-m",
            f"docs: 发布 {data['window']['mode']} {data['window']['period']} 研究报告",
        )
    commit = git(root, "rev-parse", "HEAD")
    # 失败时保留已提交报告与本地状态，重试只 push，不强推。
    git(root, "push", "origin", "HEAD:main")
    receipt = {
        "status": "pushed",
        "commit": commit,
        "path": relative,
        "pushed_at": datetime.now(UTC).isoformat(),
    }
    target = root / "results/research-state" / (directory.name + "-publication.json")
    target.write_text(json.dumps(receipt, indent=2))
    return receipt
