"""交易日窗口：使用 tc 日历，禁止用工作日猜测交易日。"""

from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")
SH = ZoneInfo("Asia/Shanghai")
MODES = ("weekly", "daily", "realtime")


def aware(value: str) -> datetime:
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("时间必须包含时区")
    return result


def closing(day: dict) -> datetime:
    if day["session_type"] not in {"full", "half"}:
        raise ValueError("未知交易时段，不能推测收盘时间")
    return datetime.combine(
        date.fromisoformat(day["trade_date"]), time(13 if day["session_type"] == "half" else 16), NY
    )


def research_window(mode: str, cutoff: datetime, calendar: dict, target: date | None = None):
    if mode not in MODES or cutoff.tzinfo is None:
        raise ValueError("模式或截止时间无效")
    local = cutoff.astimezone(NY)
    days = sorted(calendar["trading_days"], key=lambda d: d["trade_date"])
    first, last = (date.fromisoformat(calendar["range"][k]) for k in ["from", "to"])
    if not first <= local.date() <= last:
        raise ValueError("交易日历未覆盖截止时间")
    complete = [d for d in days if closing(d) <= cutoff]
    if target:
        complete = [d for d in complete if d["trade_date"] <= str(target)]
    if not complete:
        raise ValueError("没有已完成交易日")
    end = date.fromisoformat(complete[-1]["trade_date"])
    if mode == "weekly":
        monday = end - timedelta(days=end.weekday())
        friday = monday + timedelta(days=4)
        if last < friday:
            raise ValueError("日历未覆盖完整交易周")
        # 周内最后一场收盘前，使用上一完整周；周五休市时周四收盘即完成。
        week = [d for d in days if str(monday) <= d["trade_date"] <= str(friday)]
        if any(closing(d) > cutoff for d in week) or (target and friday > target):
            monday -= timedelta(days=7)
            friday -= timedelta(days=7)
            week = [d for d in days if str(monday) <= d["trade_date"] <= str(friday)]
        if first > monday or not week:
            raise ValueError("缺少完整周日历")
        end = date.fromisoformat(week[-1]["trade_date"])
        start = date.fromisoformat(week[0]["trade_date"])
        year, number, _ = monday.isocalendar()
        period = f"{year}-W{number:02}"
    else:
        start, period = end, str(local.date() if mode == "realtime" else end)
    today = next((d for d in days if d["trade_date"] == str(local.date())), None)
    phase = "休市"
    if today:
        opening = datetime.combine(local.date(), time(9, 30), NY)
        if time(4) <= local.time().replace(tzinfo=None) < time(9, 30):
            phase = "盘前"
        elif opening <= cutoff < closing(today):
            phase = "盘中"
        elif closing(today) <= cutoff and local.hour < 20:
            phase = "盘后"
    following = next((d["trade_date"] for d in days if d["trade_date"] > str(end)), None)
    if following is None:
        raise ValueError("日历缺少下一交易日")
    return {
        "mode": mode,
        "period": period,
        "start_date": str(start),
        "end_date": str(end),
        "cutoff": cutoff.isoformat(),
        "cutoff_ny": local.isoformat(),
        "cutoff_shanghai": cutoff.astimezone(SH).isoformat(),
        "market_phase": phase,
        "next_session": following,
        "note": "价格窗口与发布后消息分开；研究截止时间不等于所有来源观测时间",
    }
