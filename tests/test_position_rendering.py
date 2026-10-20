from tc_trade_strategy.position_rendering import allocation_chart, render_private


def test_weight_chart_does_not_guess_or_normalize():
    page = allocation_chart([
        {"symbol": "SHORT", "weight_pct": -12.5},
        {"symbol": "LONG", "weight_pct": 150},
        {"symbol": "UNKNOWN", "market_value_display": 500},
    ])
    assert '150.00%' in page and '-12.50%' in page
    assert '1 项比例缺失' in page
    assert 'width:100.0000%' in page and 'width:8.3333%' in page
    assert 'UNKNOWN' not in page
    assert '暂不绘制' in allocation_chart([{'symbol': 'MISSING'}])


def test_private_unavailable_readable_without_misleading_chart():
    md, page = render_private(dict(
        summary='<script>unsafe</script>', account_risk=None, positions=[],
        holding_reviews=[], gaps=['不可读取'], generated_at='2026-10-21T00:00:00Z',
        observed_at=None, public_cutoff='2026-10-20T23:00:00Z', public_report='reports/test',
        status='unavailable',
    ))
    assert '<pre' not in page and '<script>unsafe</script>' not in page
    assert '当前持仓不可用' in page and 'weight-row"' not in page
    assert '不可读取' in md
