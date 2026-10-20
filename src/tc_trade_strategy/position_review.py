"""个人持仓附录写入器：只在忽略的本地目录输出，单向关联公共报告。"""

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path

from .calendar import aware
from .evidence import digest
from .position_rendering import render_private
from .publishing import git, run_lock


def private_directory(root):
    directory = root / "sensitive/position-reviews"
    for path in (root / "sensitive", directory):
        if path.is_symlink():
            raise ValueError("私人附录目录不允许符号链接")
    probe = "sensitive/position-reviews/probe.json"
    if not git(root, "check-ignore", "--", probe, check=False) or git(
        root, "ls-files", "--", "sensitive/position-reviews"
    ):
        raise ValueError("私人附录目录必须被Git忽略且没有已跟踪文件")
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def validate(data):
    required = {
        "status",
        "observed_at",
        "summary",
        "account_risk",
        "positions",
        "holding_reviews",
        "gaps",
    }
    if set(data) != required or data["status"] not in ("reviewed", "unavailable"):
        raise ValueError("私人附录输入不完整或状态无效")
    if not data["summary"] or not isinstance(data["positions"], list):
        raise ValueError("缺少私人结论或持仓数组")
    if data["status"] == "unavailable":
        if not data["gaps"] or data["positions"] or data["holding_reviews"]:
            raise ValueError("无法读取时只记录原因，不能冒充有当前持仓或建议")
    else:
        if not data["observed_at"] or aware(data["observed_at"]) > datetime.now(UTC):
            raise ValueError("已复核持仓需有效实际观察时间")
        symbols = {p["symbol"] for p in data["positions"]}
        reviews = data["holding_reviews"]
        if len(symbols) != len(data["positions"]):
            raise ValueError("重复持仓代码，先合并或核实币种/交易所")
        if {r["symbol"] for r in reviews} != symbols or len(reviews) != len(symbols):
            raise ValueError("每个持仓必须有一条公司/指数事件与情景复核")
        for review in reviews:
            for field in (
                "symbol",
                "catalysts",
                "impact",
                "upside_case",
                "downside_case",
                "confirmation",
                "invalidation",
                "horizon",
                "guidance",
                "sources",
            ):
                if field not in review or (field != "catalysts" and not review[field]):
                    raise ValueError("持仓复核缺少事件、情景、指导或证据")
            if not isinstance(review["catalysts"], list):
                raise ValueError("催化剂需为数组；查无事件时为空并解释缺口")

    # 私人报告可以含仓位和财务数值，但仍拒绝登录资料和凭证字段。
    def no_credentials(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key.lower() in {
                    "api_key",
                    "password",
                    "authorization",
                    "access_token",
                    "refresh_token",
                    "cookie",
                    "account_id",
                    "user_id",
                }:
                    raise ValueError("私人报告也不得保存账户标识或登录凭证")
                no_credentials(item)
        elif isinstance(value, list):
            for item in value:
                no_credentials(item)
        elif isinstance(value, str) and any(
            marker in value for marker in ("Bearer ", "-----BEGIN", "sk-proj-", "github_pat_")
        ):
            raise ValueError("私人报告疑似含凭证")

    no_credentials(data)
    json.dumps(data, allow_nan=False)


def save_private_review(root, public_report, data):
    """调用方持有run_lock；公共报告不写回私人路径或持仓代码列表。"""
    root = root.resolve()
    directory = private_directory(root)
    public_report = public_report.resolve()
    relative = public_report.relative_to(root).parts
    if (
        len(relative) != 4
        or relative[0] != "reports"
        or relative[1] not in ("weekly", "daily", "realtime")
    ):
        raise ValueError("仅关联 reports/{mode}/{period}/{run} 公共报告")
    public = json.loads((public_report / "evidence.json").read_text())
    validate(data)
    stamp = datetime.now(UTC)
    # 各层路径验证，拒绝跳转至其他敏感目录或公开目录。
    parent = directory
    for name in relative[1:]:
        parent /= name
        if parent.is_symlink():
            raise ValueError("私人附录路径不允许符号链接")
        parent.mkdir(exist_ok=True)
    target = parent / stamp.strftime("%Y%m%dT%H%M%S.%fZ")
    target.mkdir(exist_ok=False)
    payload = {
        **data,
        "generated_at": stamp.isoformat(),
        "public_report": str(public_report),
        "public_evidence_sha256": digest(public),
        "public_cutoff": public["window"]["cutoff"],
        "delivery_slot": public.get("delivery_slot"),
    }
    md, page = render_private(payload)
    (target / "review.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False)
    )
    (target / "report.md").write_text(md)
    (target / "index.html").write_text(page)
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--public-report", type=Path, required=True)
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    with run_lock(root):
        base = private_directory(root)
        incoming = args.input.resolve()
        if not incoming.is_relative_to(base.resolve()):
            raise ValueError("仅接受 sensitive/position-reviews/ 内已授权的私人分析输入")
        output = save_private_review(root, args.public_report, json.loads(incoming.read_text()))
    print(json.dumps({"private_report": str(output), "status": "local_only"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
