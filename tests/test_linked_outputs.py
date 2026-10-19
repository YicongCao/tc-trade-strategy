import json
from datetime import UTC, datetime

import pytest

from tc_trade_strategy.calendar import aware, daily_slot
from tc_trade_strategy.position_review import save_private_review
from tc_trade_strategy.publishing import git, published_period


@pytest.mark.parametrize(
    ("cutoff", "expected"),
    [
        ("2026-10-18T07:14:59+08:00", "2026-10-17T20:00:00+08:00"),
        ("2026-10-18T07:15:00+08:00", "2026-10-18T07:15:00+08:00"),
        ("2026-10-18T19:59:00+08:00", "2026-10-18T07:15:00+08:00"),
        ("2026-10-18T20:00:00+08:00", "2026-10-18T20:00:00+08:00"),
        ("2026-11-02T12:10:00Z", "2026-11-02T20:00:00+08:00"),
    ],
)
def test_daily_slots_weekends_dst_and_catchup(cutoff, expected):
    assert daily_slot(aware(cutoff)) == expected


def test_morning_publication_does_not_skip_evening(tmp_path, monkeypatch):
    import tc_trade_strategy.publishing as publishing

    data = {
        "window": {"mode": "daily", "period": "2026-10-16"},
        "delivery_slot": "2026-10-18T07:15:00+08:00",
    }
    monkeypatch.setattr(
        publishing, "all_reports", lambda root: [(tmp_path / "evidence.json", data)]
    )
    monkeypatch.setattr(publishing, "remote_contains", lambda root, path: True)
    assert published_period(tmp_path, "daily", "2026-10-16", data["delivery_slot"])
    assert not published_period(tmp_path, "daily", "2026-10-16", "2026-10-18T20:00:00+08:00")
    assert not published_period(tmp_path, "daily", "2026-10-16", "2026-10-19T07:15:00+08:00")


def test_private_report_one_way_link_and_failure(tmp_path):
    git(tmp_path, "init")
    (tmp_path / ".gitignore").write_text("/sensitive/\n")
    public = tmp_path / "reports/daily/2026-10-16/public-run"
    public.mkdir(parents=True)
    (public / "evidence.json").write_text(
        json.dumps({"window": {"cutoff": "2026-10-18T01:00:00Z"}})
    )
    original = (public / "evidence.json").read_bytes()
    data = {
        "status": "unavailable",
        "observed_at": None,
        "summary": "cannot verify",
        "account_risk": None,
        "positions": [],
        "holding_reviews": [],
        "gaps": ["offline"],
    }
    output = save_private_review(tmp_path, public, data)
    payload = json.loads((output / "review.json").read_text())
    assert payload["public_report"] == str(public)
    assert payload["status"] == "unavailable"
    assert (output / "index.html").exists() and (output / "report.md").exists()
    assert original == (public / "evidence.json").read_bytes()
    assert git(tmp_path, "check-ignore", "--", str(output / "review.json"))
    with pytest.raises(ValueError, match="每个持仓"):
        save_private_review(
            tmp_path,
            public,
            {
                **data,
                "status": "reviewed",
                "observed_at": "2026-10-18T01:00:00Z",
                "positions": [{"symbol": "TEST"}],
            },
        )
    (tmp_path / ".gitignore").write_text("")
    with pytest.raises(ValueError, match="Git"):
        save_private_review(tmp_path, public, data)


def test_private_review_rejects_symlink_and_credentials(tmp_path):
    git(tmp_path, "init")
    (tmp_path / ".gitignore").write_text("/sensitive/\n")
    public = tmp_path / "reports/realtime/2026-10-18/run"
    public.mkdir(parents=True)
    (public / "evidence.json").write_text('{"window":{"cutoff":"2026-10-18T01:00:00Z"}}')
    data = {
        "status": "unavailable",
        "observed_at": None,
        "summary": "offline",
        "account_risk": {"api_key": "forbidden"},
        "positions": [],
        "holding_reviews": [],
        "gaps": ["offline"],
    }
    with pytest.raises(ValueError, match="凭证"):
        save_private_review(tmp_path, public, data)
    (tmp_path / "sensitive/position-reviews/realtime").symlink_to(
        tmp_path, target_is_directory=True
    )
    with pytest.raises(ValueError, match="符号链接"):
        save_private_review(tmp_path, public, {**data, "account_risk": None})


@pytest.mark.parametrize("mode", ["weekly", "daily", "realtime"])
def test_reviewed_positions_cover_every_symbol_and_escape_html(tmp_path, mode):
    git(tmp_path, "init")
    (tmp_path / ".gitignore").write_text("/sensitive/\n")
    public = tmp_path / "reports" / mode / "period" / "run"
    public.mkdir(parents=True)
    (public / "evidence.json").write_text('{"window":{"cutoff":"2026-10-18T01:00:00Z"}}')
    review = {
        "symbol": "TEST",
        "catalysts": [],
        "impact": "no verified event",
        "upside_case": "improves",
        "downside_case": "worsens",
        "confirmation": "confirm",
        "invalidation": "invalidate",
        "horizon": "week",
        "guidance": "observe",
        "sources": ["https://official.example"],
    }
    data = {
        "status": "reviewed",
        "observed_at": datetime.now(UTC).isoformat(),
        "summary": "<script>unsafe</script>",
        "account_risk": {"cash": 100},
        "positions": [{"symbol": "TEST", "quantity": 1}],
        "holding_reviews": [review],
        "gaps": ["no upcoming event verified"],
    }
    output = save_private_review(tmp_path, public, data)
    assert "<script>unsafe</script>" not in (output / "index.html").read_text()
    payload = json.loads((output / "review.json").read_text())
    assert payload["holding_reviews"][0]["symbol"] == "TEST"
    assert payload["public_evidence_sha256"]
    assert not (public / "review.json").exists()
