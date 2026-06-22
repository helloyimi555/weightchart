import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime

# ============================================================
# DATA
# ============================================================
raw = [
    ("2026-04-20", 77.5,  None,  1478, 1, ""),
    ("2026-04-21", 77.9,  27.9,  1530, 5, "飲み会"),
    ("2026-04-22", 77.0,  None,  2010, 4, "飲み会"),
    ("2026-04-23", 76.9,  26.7,   710, 0, ""),
    ("2026-04-24", 76.8,  26.4,  1563, 0, ""),
    ("2026-04-25", 76.7,  26.9,  1510, 6, "飲み会"),
    ("2026-04-26", 76.7,  26.6,  1731, 0, ""),
    ("2026-04-27", 77.1,  26.5,  1745, 3, "飲み会"),
    ("2026-04-28", 77.1,  27.8,  2090, 4, "飲み会"),
    ("2026-04-29", 76.9,  26.8,  1667, 1, ""),
    ("2026-04-30", 76.9,  26.3,  1905, 0, ""),
    ("2026-05-01", 76.6,  27.5,  1856, 0, ""),
    ("2026-05-02", 75.9,  26.8,  1282, 0, ""),
    ("2026-05-03", 76.6,  26.9,  1738, 4, "飲み会"),
    ("2026-05-04", 76.8,  28.1,  1877, 3, "飲み会"),
    ("2026-05-05", 77.1,  26.7,  1864, 4, "飲み会"),
    ("2026-05-06", 77.4,  26.4,  1791, 0, ""),
    ("2026-05-07", 76.7,  26.6,  1631, 0, ""),
    ("2026-05-08", 76.3,  26.3,  2701, 5, "飲み会"),
    ("2026-05-09", 76.7,  26.8,  1966, 1, ""),
    ("2026-05-10", 76.8,  26.4,  1677, 0, ""),
    ("2026-05-11", 76.3,  26.8,  1670, 0, ""),
    ("2026-05-12", 76.2,  26.4,  1735, 0, ""),
    ("2026-05-13", 75.9,  25.8,  1556, 0, ""),
    ("2026-05-14", 76.5,  26.8,  1787, 0, ""),
    ("2026-05-15", 76.1,  25.7,  1867, 5, "飲み会"),
    ("2026-05-16", 75.9,  25.2,  1814, 0, ""),
    ("2026-05-17", 76.1,  26.3,  1932, 0, ""),
    ("2026-05-18", 76.3,  26.3,  1694, 0, ""),
    ("2026-05-19", 75.1,  27.0,  1813, 0, ""),
    ("2026-05-20", 75.4,  27.1,  1809, 0, ""),
    ("2026-05-21", 75.7,  27.2,  2003, 2, "飲み会"),
    ("2026-05-22", 75.2,  27.0,  1763, 0, ""),
    ("2026-05-23", 75.0,  26.9,  1754, 0, ""),
    ("2026-05-24", 75.3,  26.9,  1832, 0, ""),
    ("2026-05-25", 75.1,  26.8,  1742, 0, ""),
    ("2026-05-26", 74.8,  26.7,  1682, 0, ""),
    ("2026-05-27", 75.0,  26.8,  1923, 2, "飲み会"),
    ("2026-05-28", 75.2,  26.9,  1798, 0, ""),
    ("2026-05-29", 74.9,  26.7,  1751, 0, ""),
    ("2026-05-30", 74.6,  26.5,  1698, 0, ""),
    ("2026-05-31", 74.8,  26.6,  1843, 0, ""),
    ("2026-06-01", 74.5,  26.4,  1712, 0, ""),
    ("2026-06-02", 74.3,  26.3,  1678, 0, ""),
    ("2026-06-03", 74.6,  26.5,  1891, 2, "飲み会"),
    ("2026-06-04", 74.7,  26.4,  1803, 0, ""),
    ("2026-06-05", 74.9,  26.1,  1613, 0, ""),
    ("2026-06-06", 74.3,  25.8,  1787, 0, ""),
    ("2026-06-07", 74.0,  26.1,  1687, 0, ""),
    ("2026-06-08", 74.1,  25.7,  1932, 0, ""),
    ("2026-06-09", 74.6,  26.2,  1664, 3, "飲み会(鳥貴族)"),
    ("2026-06-10", 74.3,  25.7,  1860, 0, ""),
    ("2026-06-11", 74.1,  25.6,  1666, 0, ""),
    ("2026-06-12", 74.6,  26.2,  1621, 0, ""),
    ("2026-06-13", 73.3,  26.5,  1925, 1, "焼酎"),
    ("2026-06-14", 73.7,  26.3,  1815, 1, "焼酎"),
    ("2026-06-15", 74.1,  26.2,  1868, 0, ""),
    ("2026-06-16", 74.3,  25.9,  1782, 0, ""),
    ("2026-06-17", 74.3,  26.3,  1264, 0, ""),
    ("2026-06-18", 74.2,  25.5,  1897, 0, ""),
    ("2026-06-19", 74.0,  25.5,  1707, 3, "飲み会"),
    ("2026-06-20", 74.3,  25.9,  1644, 0, ""),
    ("2026-06-21", 73.5,  25.8,  1696, 0, ""),
]

cols = ["date", "weight", "fat", "kcal", "alcohol", "memo"]
df = pd.DataFrame(raw, columns=cols)
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

w = df["weight"].astype(float)

# indicators
sma3  = w.rolling(3).mean()
sma7  = w.rolling(7).mean()
sma14 = w.rolling(14).mean()
std14 = w.rolling(14).std()
bb_upper = sma14 + 2 * std14
bb_lower = sma14 - 2 * std14

delta = w.diff()
gain  = delta.clip(lower=0).rolling(9).mean()
loss  = (-delta.clip(upper=0)).rolling(9).mean()
rs    = gain / loss.replace(0, np.nan)
rsi   = 100 - 100 / (1 + rs)

ema5   = w.ewm(span=5,  adjust=False).mean()
ema14  = w.ewm(span=14, adjust=False).mean()
macd   = ema5 - ema14
signal = macd.ewm(span=5, adjust=False).mean()
hist   = macd - signal

def linreg_forecast(series, lookback, ahead):
    s = series.dropna().tail(lookback)
    if len(s) < 3:
        return [], []
    x = np.arange(len(s))
    p = np.polyfit(x, s.values, 1)
    future_x = np.arange(len(s), len(s) + ahead)
    future_y = np.polyval(p, future_x)
    future_dates = pd.date_range(s.index[-1] + pd.Timedelta(days=1), periods=ahead)
    return future_dates, future_y

fc7_d,  fc7_y  = linreg_forecast(w, 7,  7)
fc14_d, fc14_y = linreg_forecast(w, 14, 14)
fc30_d, fc30_y = linreg_forecast(w, 30, 30)

# colors
BG    = "#fafafa"
GRID  = "#e8e8e8"
TEXT  = "#333333"
BLUE  = "#58a6ff"
GREEN = "#3fb950"
RED   = "#f85149"
AMBER = "#e3b341"
PURPLE= "#bc8cff"
PINK  = "#ff7b72"

dates   = df.index
weights = w.values
fats    = df["fat"].values
kcals   = df["kcal"].values
alcohol = df["alcohol"].values

alc_dates = [d for d, a in zip(dates, alcohol) if a and a > 0]
alc_vals  = [weights[i] for i, a in enumerate(alcohol) if a and a > 0]

# ============================================================
# FIGURE
# ============================================================
fig = make_subplots(
    rows=5, cols=1,
    shared_xaxes=True,
    row_heights=[0.40, 0.15, 0.15, 0.15, 0.15],
    vertical_spacing=0.025,
    subplot_titles=("体重 (kg)", "摂取 kcal", "体脂肪 (%)", "RSI(9)", "MACD(5,14,5)")
)

# Row1: Weight
fig.add_trace(go.Scatter(x=dates, y=bb_upper, name="BB+2σ",
    line=dict(color="rgba(88,166,255,0.2)", width=1, dash="dot"),
    showlegend=False, hoverinfo="skip"), row=1, col=1)
fig.add_trace(go.Scatter(x=dates, y=bb_lower, name="BB-2σ",
    fill="tonexty", fillcolor="rgba(88,166,255,0.05)",
    line=dict(color="rgba(88,166,255,0.2)", width=1, dash="dot"),
    showlegend=False, hoverinfo="skip"), row=1, col=1)
fig.add_trace(go.Scatter(x=dates, y=sma14, name="SMA14",
    line=dict(color=AMBER, width=1.2, dash="dash"),
    hovertemplate="%{y:.2f}kg<extra>SMA14</extra>"), row=1, col=1)
fig.add_trace(go.Scatter(x=dates, y=sma7, name="SMA7",
    line=dict(color=PURPLE, width=1.5),
    hovertemplate="%{y:.2f}kg<extra>SMA7</extra>"), row=1, col=1)
fig.add_trace(go.Scatter(x=dates, y=sma3, name="SMA3",
    line=dict(color=GREEN, width=1.0, dash="dot"),
    hovertemplate="%{y:.2f}kg<extra>SMA3</extra>"), row=1, col=1)
fig.add_trace(go.Scatter(x=dates, y=weights, name="体重",
    mode="lines+markers",
    line=dict(color=BLUE, width=2),
    marker=dict(size=4, color=BLUE),
    hovertemplate="%{x|%m/%d} %{y:.1f}kg<extra></extra>"), row=1, col=1)
if alc_dates:
    fig.add_trace(go.Scatter(x=alc_dates, y=alc_vals, name="🍶飲酒",
        mode="markers",
        marker=dict(symbol="star", size=10, color=RED, opacity=0.8),
        hovertemplate="%{x|%m/%d} 飲酒日<extra></extra>"), row=1, col=1)

for fd, fy, lbl, col in [
    (fc7_d,  fc7_y,  "予測7d",  "rgba(255,123,114,0.6)"),
    (fc14_d, fc14_y, "予測14d", "rgba(227,179,65,0.5)"),
    (fc30_d, fc30_y, "予測30d", "rgba(63,185,80,0.4)"),
]:
    if len(fd):
        all_d = list(dates[-1:]) + list(fd)
        all_y = [w.dropna().iloc[-1]] + list(fy)
        fig.add_trace(go.Scatter(x=all_d, y=all_y, name=lbl,
            line=dict(color=col, width=1.5, dash="dash"),
            hovertemplate="%{x|%m/%d} %{y:.2f}kg<extra>" + lbl + "</extra>"), row=1, col=1)

fig.add_hline(y=72.0, line_color="rgba(248,81,73,0.4)", line_dash="dot", line_width=1, row=1, col=1)
fig.add_annotation(x=dates[-1], y=72.0, text="目標 72kg",
    font=dict(color=RED, size=10), showarrow=False,
    xanchor="right", yanchor="bottom", row=1, col=1)

# Row2: kcal
kcal_colors = []
for k in kcals:
    if k is None:
        kcal_colors.append(GRID)
    elif k > 1900:
        kcal_colors.append("rgba(248,81,73,0.6)")
    elif k < 1600:
        kcal_colors.append("rgba(63,185,80,0.6)")
    else:
        kcal_colors.append("rgba(88,166,255,0.5)")
fig.add_trace(go.Bar(x=dates, y=kcals, name="摂取kcal", width=69120000,
    marker_color=kcal_colors,
    hovertemplate="%{x|%m/%d} %{y}kcal<extra></extra>"), row=2, col=1)
fig.add_hline(y=1782, line_color="rgba(227,179,65,0.5)", line_dash="dot", line_width=1, row=2, col=1)

# Row3: body fat
fig.add_trace(go.Scatter(x=dates, y=fats, name="体脂肪%",
    line=dict(color=AMBER, width=1.5),
    hovertemplate="%{x|%m/%d} %{y:.1f}%<extra></extra>"), row=3, col=1)

# Row4: RSI
fig.add_trace(go.Scatter(x=dates, y=rsi, name="RSI",
    line=dict(color=PINK, width=1.5),
    hovertemplate="%{x|%m/%d} RSI=%{y:.1f}<extra></extra>"), row=4, col=1)
fig.add_hline(y=70, line_color="rgba(248,81,73,0.3)", line_dash="dot", line_width=1, row=4, col=1)
fig.add_hline(y=30, line_color="rgba(63,185,80,0.3)", line_dash="dot", line_width=1, row=4, col=1)

# Row5: MACD
hist_colors = [GREEN if v >= 0 else RED for v in hist.fillna(0)]
fig.add_trace(go.Bar(x=dates, y=hist, name="MACDヒスト",
    marker_color=hist_colors, opacity=0.7,
    hovertemplate="%{x|%m/%d} %{y:.3f}<extra></extra>"), row=5, col=1)
fig.add_trace(go.Scatter(x=dates, y=macd, name="MACD",
    line=dict(color=BLUE, width=1.2),
    hovertemplate="%{x|%m/%d} %{y:.3f}<extra></extra>"), row=5, col=1)
fig.add_trace(go.Scatter(x=dates, y=signal, name="Signal",
    line=dict(color=RED, width=1.2, dash="dash"),
    hovertemplate="%{x|%m/%d} %{y:.3f}<extra></extra>"), row=5, col=1)

# ============================================================
# LAYOUT — 前回と同じシンプルな形
# ============================================================
fig.update_layout(
    height=900,
    paper_bgcolor="white",
    plot_bgcolor=BG,
    font=dict(color='#333', family='-apple-system, BlinkMacSystemFont, sans-serif'),
    legend=dict(orientation="h", x=0, y=1.02, bgcolor="rgba(0,0,0,0)", font=dict(size=10)),
    hovermode="x unified",
    margin=dict(l=50, r=50, t=60, b=40),
    title=dict(text=f"WeightChart v0.2  |  更新: {datetime.now().strftime('%Y-%m-%d')}",
               font=dict(size=13, color=TEXT), x=0.5),
)

# 全サブプロットの軸スタイル
for row in range(1, 6):
    fig.update_xaxes(showgrid=True, gridcolor=GRID, gridwidth=0.5,
                     zeroline=False, showline=False,
                     tickfont=dict(color=TEXT), row=row, col=1)
    fig.update_yaxes(showgrid=True, gridcolor=GRID, gridwidth=0.5,
                     zeroline=False, showline=False,
                     tickfont=dict(color=TEXT), row=row, col=1)

fig.update_yaxes(range=[71.0, 78.5], row=1, col=1)
fig.update_yaxes(range=[800, 3200], row=2, col=1)
fig.update_yaxes(range=[23, 30], row=3, col=1)
fig.update_yaxes(range=[0, 100], row=4, col=1)

# ============================================================
# STATUS + 傾向分析
# ============================================================
latest  = w.dropna().iloc[-1]
s7_val  = sma7.dropna().iloc[-1]
rsi_val = rsi.dropna().iloc[-1]
macd_h  = hist.dropna().iloc[-1]
start_w = w.dropna().iloc[0]
diff_w  = latest - start_w

# SMA7トレンド（過去3日の変化）
s7_diff = sma7.dropna().iloc[-1] - sma7.dropna().iloc[-4]
if s7_diff < -0.02:
    sma_status = f"✓ 7日SMA下向き（過去3日で{s7_diff:+.2f}kg）→ 中期トレンドは減量継続"
elif s7_diff > 0.02:
    sma_status = f"⚠ 7日SMA上向き（過去3日で{s7_diff:+.2f}kg）→ 停滞注意"
else:
    sma_status = f"⊙ 7日SMA横ばい（過去3日で{s7_diff:+.2f}kg）→ 様子見"

# MACDヒスト
if macd_h < -0.05:
    macd_status = f"✓ MACDヒストグラム負（{macd_h:.3f}）→ 減量加速中"
elif macd_h > 0.05:
    macd_status = f"⊙ MACDヒストグラム正（{macd_h:.3f}）→ 上昇圧力"
else:
    macd_status = f"⊙ MACDヒストグラム中立（{macd_h:.3f}）→ トレンド転換注意"

# RSI
if rsi_val < 35:
    rsi_status = f"✓ RSI={rsi_val:.1f} → 売られすぎ圏（減量強め）"
elif rsi_val > 65:
    rsi_status = f"⚠ RSI={rsi_val:.1f} → 買われすぎ圏（反発注意）"
else:
    rsi_status = f"⊙ RSI={rsi_val:.1f} → 正常域"

bb_lo = bb_lower.dropna().iloc[-1]
bb_status = f"⊙ BB内推移（下バンド{bb_lo:.2f}）"

# ============================================================
# HTML
# ============================================================
chart_html = fig.to_html(include_plotlyjs=True, full_html=False, config={"responsive": True})

recent = df.tail(14).copy()
table_rows = ""
for d, row_data in recent.iterrows():
    s7v  = sma7.get(d)
    rsiv = rsi.get(d)
    table_rows += f"""<tr>
        <td>{d.strftime('%m/%d')}</td>
        <td><b>{row_data['weight']:.1f}</b></td>
        <td>{f"{row_data['fat']:.1f}" if row_data['fat'] else '-'}</td>
        <td>{f"{s7v:.2f}" if s7v else '-'}</td>
        <td>{f"{rsiv:.0f}" if rsiv else '-'}</td>
        <td>{int(row_data['kcal']) if row_data['kcal'] else '-'}</td>
        <td>{'🍶' * int(row_data['alcohol']) if row_data['alcohol'] else ''}</td>
        <td>{row_data['memo']}</td>
    </tr>"""


# ============================================================
# AI自動コメント生成（Claude API）
# ============================================================
import urllib.request, json

def generate_ai_comment():
    prompt = f"""あなたはダイエット管理アシスタントです。以下のテクニカル分析データをもとに、500字以内の日本語で所見コメントを書いてください。FXのテクニカル分析の視点と、健康的なダイエットの視点を組み合わせてください。

【最新データ】
- 最新体重: {latest:.1f}kg（開始比: {diff_w:+.1f}kg、目標72kgまで: {latest - 72.0:.1f}kg）
- SMA7: {s7_val:.2f}kg（{sma_status}）
- RSI(9): {rsi_val:.1f}（{rsi_status}）
- MACDヒスト: {macd_h:+.3f}（{macd_status}）
- BB下限: {bb_lo:.2f}kg（{bb_status}）
- 直近7日の体重推移: {", ".join([f"{v:.1f}" for v in w.dropna().tail(7).values])}

所見（500字以内）:"""

    try:
        import os
        api_key = os.environ.get("ANTHROPIC_API_KEY", "")
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=json.dumps({
                "model": "claude-sonnet-4-6",
                "max_tokens": 600,
                "messages": [{"role": "user", "content": prompt}]
            }).encode(),
            headers={"Content-Type": "application/json", "x-api-key": api_key, "anthropic-version": "2023-06-01"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=15) as res:
            data = json.loads(res.read())
            return data["content"][0]["text"].strip()
    except Exception as e:
        return f"（コメント生成エラー: {e}）"

ai_comment = generate_ai_comment()

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>WeightChart v0.2</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif; background: white; color: #333; margin: 0; padding: 16px; }}
  .status {{ background: #f8f8f8; border: 1px solid #ddd; border-radius: 6px; padding: 12px 16px; margin-bottom: 12px; font-size: 13px; line-height: 1.8; }}
  .status .label {{ font-size: 10px; font-weight: bold; color: #999; letter-spacing: 1px; margin-bottom: 4px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 12px; margin-top: 16px; }}
  th {{ background: #f5f5f5; color: #666; padding: 8px; text-align: center; border-bottom: 2px solid #ddd; font-weight: normal; }}
  td {{ padding: 6px 8px; text-align: center; border-bottom: 1px solid #eee; }}
  tr:hover td {{ background: #fafafa; }}
  .legend-tags {{ font-size: 11px; color: #888; margin-top: 8px; }}
  .comment {{ background: #f0f7ff; border-left: 3px solid #58a6ff; border-radius: 0 6px 6px 0; padding: 12px 16px; margin-top: 16px; font-size: 13px; line-height: 1.9; color: #333; }}
  .comment .label {{ font-size: 10px; font-weight: bold; color: #58a6ff; letter-spacing: 1px; margin-bottom: 6px; }}
  .footer {{ font-size: 11px; color: #bbb; text-align: center; margin-top: 24px; padding-bottom: 16px; }}
</style>
</head>
<body>
<div class="status">
  <div class="label">STATUS</div>
  {sma_status}<br>{macd_status}<br>{rsi_status}<br>{bb_status}
</div>
{chart_html}
<table>
  <thead><tr>
    <th>日付</th><th>体重</th><th>体脂肪%</th><th>SMA7</th><th>RSI</th><th>kcal</th><th>🍶</th><th>メモ</th>
  </tr></thead>
  <tbody>{table_rows}</tbody>
</table>
<div class="legend-tags">🍶=アルコール（unit）</div>
<div class="comment">
  <div class="label">AI所見</div>
  {ai_comment}
</div>
<div class="footer">Generated by WeightChart v0.2 — {datetime.now().strftime('%Y-%m-%d %H:%M')}</div>
</body>
</html>"""

with open("/mnt/user-data/outputs/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done.")
print(f"Latest: {latest:.1f}kg  (start: {start_w:.1f}kg, diff: {diff_w:+.1f}kg)")
print(f"SMA7: {s7_val:.2f}  RSI: {rsi_val:.1f}  MACD hist: {macd_h:+.3f}")
