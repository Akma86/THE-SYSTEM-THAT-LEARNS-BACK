"""
Stage animated banner components for The Vanishing Currency.
"""
import streamlit as st


def render_stage_banner(
    stage_num: str,
    chapter_num: str,
    title_line1: str,
    title_line2: str,
    accent_color: str,
    meta_tags: list,
    ticker_items: list,
    node_name: str = "NODE_SYS",
    status_label: str = "RESTRICTED",
):
    """Renders a pure CSS animated stage banner."""
    meta_spans = " · ".join([f"<span>{tag}</span>" for tag in meta_tags])

    ticker_spans = ""
    for item in ticker_items:
        hot_cls = "hot" if item.get("hot") else ("warn" if item.get("warn") else "")
        ticker_spans += f'<span class="sb-tick-item {hot_cls}">{item["text"]}</span>'
    ticker_spans_full = ticker_spans + ticker_spans

    banner_html = f"""
    <style>
      .sb-root-{stage_num} {{
        font-family: 'Space Mono', monospace;
        background: #020712;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        overflow: hidden;
        position: relative;
        width: 100%;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5), inset 0 0 30px {accent_color}10;
      }}
      .sb-topbar-{stage_num} {{
        display: flex; align-items: center; justify-content: space-between;
        padding: 8px 18px; border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(2,6,23,0.85);
      }}
      .sb-dot-{stage_num} {{
        width: 8px; height: 8px; border-radius: 50%; background: {accent_color};
        box-shadow: 0 0 12px {accent_color};
        animation: sb-pulse-{stage_num} 1.8s infinite;
      }}
      @keyframes sb-pulse-{stage_num} {{
        0%,100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.4; transform: scale(1.3); }}
      }}
      .sb-main-{stage_num} {{
        position: relative; height: 230px; overflow: hidden;
        display: flex; align-items: stretch;
        background: linear-gradient(135deg, rgba(2,6,23,0.95), rgba(15,23,42,0.85));
      }}
      .sb-scanline-{stage_num} {{
        position: absolute; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, transparent 0%, {accent_color}40 20%, {accent_color}90 50%, {accent_color}40 80%, transparent 100%);
        animation: sb-scan-{stage_num} 3.5s linear infinite; pointer-events: none; z-index: 5;
      }}
      @keyframes sb-scan-{stage_num} {{
        0% {{ top: -2px; }}
        100% {{ top: 230px; }}
      }}
      .sb-left-bar-{stage_num} {{
        width: 4px; background: {accent_color}; flex-shrink: 0; position: relative; z-index: 2;
        box-shadow: 0 0 15px {accent_color};
      }}
      .sb-vert-label-{stage_num} {{
        writing-mode: vertical-rl; transform: rotate(180deg); font-size: 11px;
        letter-spacing: 3px; color: {accent_color}; opacity: 0.7; text-transform: uppercase;
        padding: 12px 10px; flex-shrink: 0; position: relative; z-index: 2;
        border-right: 1px solid rgba(255,255,255,0.06);
      }}
      .sb-center-{stage_num} {{
        flex: 1; display: flex; flex-direction: column; justify-content: center;
        padding: 0 28px; position: relative; z-index: 2;
      }}
      .sb-chapter-{stage_num} {{
        font-size: 13px; letter-spacing: 4px; color: {accent_color}; opacity: 0.9;
        text-transform: uppercase; margin-bottom: 6px;
        display: flex; align-items: center; gap: 8px; font-weight: 700;
      }}
      .sb-title-{stage_num} {{
        font-family: 'Barlow Condensed', sans-serif; font-weight: 900; font-size: 64px;
        line-height: 0.92; letter-spacing: -1.5px; color: #f8fafc;
        text-transform: uppercase; margin-bottom: 10px;
      }}
      .sb-title-{stage_num} span {{ color: {accent_color}; display: block; }}
      .sb-meta-{stage_num} {{
        font-size: 11px; letter-spacing: 1.5px; color: #94a3b8;
        text-transform: uppercase; display: flex; align-items: center; gap: 8px; flex-wrap: wrap;
      }}
      .sb-right-{stage_num} {{
        display: flex; flex-direction: column; align-items: flex-end;
        justify-content: center; padding: 0 24px; gap: 8px;
        position: relative; z-index: 2; border-left: 1px solid rgba(255,255,255,0.06);
      }}
      .sb-hex-{stage_num} {{
        font-family: 'Barlow Condensed', sans-serif; font-weight: 900; font-size: 80px;
        line-height: 1; color: {accent_color}; opacity: 0.12; letter-spacing: -3px;
      }}
      .sb-badge-{stage_num} {{
        font-size: 11px; letter-spacing: 2px; padding: 4px 12px;
        border: 1px solid {accent_color}80; color: {accent_color};
        text-transform: uppercase; margin-top: -24px; border-radius: 6px;
        background: {accent_color}15;
      }}
      .sb-bottombar-{stage_num} {{
        display: flex; align-items: stretch;
        border-top: 1px solid rgba(255,255,255,0.06); background: rgba(2,6,23,0.9);
      }}
      .sb-ticker-wrap-{stage_num} {{ flex: 1; overflow: hidden; position: relative; }}
      .sb-ticker-{stage_num} {{
        display: flex; align-items: center; gap: 0;
        animation: sb-tick-{stage_num} 24s linear infinite; white-space: nowrap; padding: 8px 0;
      }}
      @keyframes sb-tick-{stage_num} {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(-50%); }}
      }}
      .sb-tick-item {{
        font-size: 11px; letter-spacing: 1.5px; color: #64748b; text-transform: uppercase;
        padding: 0 18px; border-right: 1px solid rgba(255,255,255,0.06); flex-shrink: 0;
      }}
      .sb-tick-item.hot {{ color: {accent_color}; font-weight: 700; }}
      .sb-tick-item.warn {{ color: #f59e0b; }}
    </style>

    <div class="sb-root-{stage_num}">
      <div class="sb-topbar-{stage_num}">
        <div style="display:flex; align-items:center; gap:10px;">
          <div class="sb-dot-{stage_num}"></div>
          <span style="font-size:11px; letter-spacing:2px; color:{accent_color}; opacity:0.85;">
            SYS::FINCORE · {node_name} · MONITORING ACTIVE
          </span>
        </div>
        <span style="font-size:10px; letter-spacing:2px; color:#f43f5e; border:1px solid #f43f5e60; padding:2px 8px; border-radius:4px;">
          {status_label}
        </span>
      </div>

      <div class="sb-main-{stage_num}">
        <div class="sb-scanline-{stage_num}"></div>
        <div class="sb-left-bar-{stage_num}"></div>
        <div class="sb-vert-label-{stage_num}">Stage {stage_num}</div>
        <div class="sb-center-{stage_num}">
          <div class="sb-chapter-{stage_num}">Chapter {chapter_num}</div>
          <div class="sb-title-{stage_num}">
            {title_line1}
            <span>{title_line2}</span>
          </div>
          <div class="sb-meta-{stage_num}">
            {meta_spans}
          </div>
        </div>
        <div class="sb-right-{stage_num}">
          <div class="sb-hex-{stage_num}">{stage_num}</div>
          <div class="sb-badge-{stage_num}">LIVE TELEMETRY</div>
        </div>
      </div>

      <div class="sb-bottombar-{stage_num}">
        <div class="sb-ticker-wrap-{stage_num}">
          <div class="sb-ticker-{stage_num}">
            {ticker_spans_full}
          </div>
        </div>
      </div>
    </div>
    """
    st.markdown(banner_html, unsafe_allow_html=True)
