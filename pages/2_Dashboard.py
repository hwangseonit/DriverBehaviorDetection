import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="📊 Dashboard", layout="centered")
HISTORY_CSV = "history.csv"
CLASS_NAMES = ["Other", "Safe", "Talking", "Texting", "Turning"]

# ===== CSS giữ nguyên như của bạn đã gửi =====
st.markdown("""
<style>
    section[data-testid="stSidebar"] {
        background: linear-gradient(120deg, #e0e7ff 0%, #fef9c3 90%, #ffe8d6 100%);
        color: #383e53;
        box-shadow: 8px 0 38px 0 #c7d2fe33, 0 0.5px 0 #fbc2eb33;
        border-top-right-radius: 26px;
        border-bottom-right-radius: 26px;
        border-left: 1.5px solid #fbc2eb33;
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border-top: 1px solid #e0e7ff88;
        border-bottom: 1px solid #fff3cd99;
    }
    section[data-testid="stSidebar"] .css-1wvake5,
    section[data-testid="stSidebar"] nav[aria-label="Main menu"] {
        padding: 2.1rem 0 0 0;
    }
    section[data-testid="stSidebar"] ul {
        margin-top: 2rem;
        padding-left: 0.6rem;
    }
    section[data-testid="stSidebar"] li {
        margin-bottom: 1.18rem;
    }
    section[data-testid="stSidebar"] a {
        font-size: 1.13rem;
        font-weight: 600;
        color: #385898 !important;
        border-radius: 14px;
        padding: 0.8rem 2.1rem;
        transition:
            background 0.19s,
            color 0.19s,
            box-shadow 0.19s,
            transform 0.15s;
        display: flex;
        align-items: center;
        gap: 0.7rem;
        box-shadow: none;
        letter-spacing: 0.12px;
        text-shadow: 0 1px 8px #e0e7ff22;
        background: none;
    }
    section[data-testid="stSidebar"] a:hover,
    section[data-testid="stSidebar"] a:focus {
        background: rgba(255,255,255,0.72);
        color: #1760b9 !important;
        text-shadow: 0 2px 12px #bae6fdcc, 0 1.5px 0 #fbc2eb;
        font-weight: 800;
        box-shadow: 0 4px 18px #bae6fd55;
        transform: translateY(-1.5px) scale(1.03);
        border: 1.5px solid #bae6fd77;
    }
    section[data-testid="stSidebar"] .css-1v0mbdj,
    section[data-testid="stSidebar"] a[aria-current="page"] {
        background: linear-gradient(90deg,#6dd5ed 10%,#fbc2eb 90%) !important;
        color: #1e293b !important;
        font-weight: 900;
        box-shadow: 0 6px 24px 0 #bae6fd77, 0 1.5px 0 #fbc2eb33;
        text-shadow: 0 2px 18px #fbc2ebcc;
        border-radius: 16px;
        letter-spacing: 0.22px;
        transform: scale(1.045);
        border: 1.7px solid #fbc2eb88;
    }
    div[data-testid="stDecoration"] {
        background: transparent !important;
        height: 0px !important;
    }
    section[data-testid="stSidebar"] img,
    section[data-testid="stSidebar"] svg {
        filter: drop-shadow(0 2px 10px #bae6fd55);
    }
    @media (max-width: 800px) {
        section[data-testid="stSidebar"] {
            border-radius: 0 0 18px 18px;
            min-width: 120px;
        }
        section[data-testid="stSidebar"] a {
            font-size: 0.99rem;
            padding: 0.6rem 1.1rem;
        }
    }
    #MainMenu {visibility: hidden;}
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;900&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Poppins', 'Segoe UI', Arial, sans-serif;
        background: linear-gradient(120deg, #e0e7ff 0%, #fef9c3 90%, #ffe8d6 100%);
        background-size: 320% 320%;
        animation: gradientBG 18s ease-in-out infinite;
        color: #22223b;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .dashboard-title {
        text-align: center;
        font-size: 2.1rem;
        font-weight: 900;
        letter-spacing: 1.5px;
        background: linear-gradient(90deg, #6366f1 15%, #38bdf8 55%, #0ea5e9 90%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 1.1em;
        margin-bottom: 1.3em;
        text-transform: capitalize;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.4em;
        flex-wrap: wrap;
        line-height: 1.13;
        white-space: normal;
    }
    @media (max-width: 600px) {
        .dashboard-title { font-size: 1.15rem; }
    }
    .big-card {
        background: rgba(255,255,255,0.92);
        border-radius: 28px;
        box-shadow: 0 8px 42px 0 #6366f122, 0 1.5px 0 #a5b4fc22;
        padding: 2.5rem 2.3rem 2rem 2.3rem;
        margin-bottom: 2.5rem;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1.5px solid #e0e7ff77;
        transition: box-shadow 0.2s;
    }
    .big-card:hover {
        box-shadow: 0 16px 48px 0 #6366f1bb, 0 4px 0 #fbc2eb33;
    }
    .stDataFrame, .stTable {
        border-radius: 16px !important;
        overflow: hidden !important;
        box-shadow: 0 2px 12px #6366f111;
        text-transform: capitalize;
    }
    .stDataFrame thead tr th {
        background: #e0e7ff33 !important;
        color: #4f46e5 !important;
        font-weight: 700 !important;
        font-size: 1.01em !important;
        text-transform: capitalize;
    }
    .stDataFrame tbody tr td {
        background: #fcfcff !important;
        text-transform: capitalize;
    }
    .stAlert {
        border-radius: 14px !important;
        box-shadow: 0 2px 8px #38bdf833;
        text-transform: capitalize;
    }
    hr {
        border: none;
        border-top: 1.5px solid #e0e7ff;
        margin: 2em 0 2em 0;
    }
    .stPlotlyChart, .element-container:has(.js-plotly-plot) {
        border-radius: 18px;
        box-shadow: 0 2px 16px #6366f122;
        background: #f0f4ff;
        margin-bottom: 1.5em;
        padding: 1.1em 1.3em;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dashboard-title">
    <span style="font-size:2.1rem;vertical-align:-0.26em;filter:drop-shadow(0 2px 10px #6366f155);margin-right:0.22em;">📊</span>
    Dashboard Thống Kê <span style="white-space:nowrap;">Hành Vi</span>
</div>
""", unsafe_allow_html=True)

def remap_predict_column(df):
    mapping = {
        "other_activities": "Other",
        "safe_driving": "Safe",
        "talking_phone": "Talking",
        "texting_phone": "Texting",
        "turning": "Turning",
        "other": "Other",
        "safe": "Safe",
        "talking": "Talking",
        "texting": "Texting"
    }
    if "predict" in df.columns:
        df["predict"] = df["predict"].map(lambda x: mapping.get(str(x).lower(), str(x).title()))
    return df

with st.container():
    st.markdown('<div class="big-card">', unsafe_allow_html=True)
    empty_df = pd.DataFrame(columns=["predict", "confidence", "loai_du_doan"])
    hist_df = None

    if "history" in st.session_state and st.session_state["history"]:
        records = []
        for rec in st.session_state["history"]:
            label = rec.get("label", "")
            confidence = rec.get("confidence", "")
            mode = rec.get("mode", "")
            records.append({
                "predict": label,
                "confidence": confidence,
                "loai_du_doan": mode
            })
        hist_df = pd.DataFrame(records)
    elif os.path.isfile(HISTORY_CSV) and os.path.getsize(HISTORY_CSV) > 0:
        try:
            hist_df = pd.read_csv(HISTORY_CSV)
        except Exception:
            hist_df = empty_df.copy()
    else:
        hist_df = empty_df.copy()

    for col in empty_df.columns:
        if col not in hist_df.columns:
            hist_df[col] = ""
    if "loai_du_doan" in hist_df.columns:
        hist_df = hist_df[hist_df["loai_du_doan"].astype(str).str.lower() == "ảnh"]
    if "predict" not in hist_df.columns:
        hist_df["predict"] = ""

    hist_df = remap_predict_column(hist_df)
    # Đảm bảo không NaN, luôn là int hoặc float
    counts = hist_df["predict"].value_counts().reindex(CLASS_NAMES).fillna(0)
    # Nếu tất cả đều là 0, phải ép về float vì matplotlib không cho toàn int 0 (NaN sang int lỗi)
    counts = counts.astype(float)

    # --- Biểu Đồ Số Lượt Dự Đoán Từng Hành Vi ---
    st.subheader("Biểu Đồ Số Lượt Dự Đoán Từng Hành Vi")
    st.bar_chart(counts)

    # --- Pie Chart ---
    st.subheader("Tỉ Lệ Hành Vi Được Phát Hiện")
    if counts.sum() == 0:
        fig, ax = plt.subplots()
        # Vẽ 1 lát rất nhạt với label "No Data"
        ax.pie([1], labels=["No Data"], colors=["#f3f3f3"])
        plt.title("Không Có Dữ Liệu")
        st.pyplot(fig)
    else:
        def autopct_format(pct):
            return ('%1.1f%%' % pct) if pct > 0 else ''
        st.pyplot(
            counts.plot.pie(
                autopct=autopct_format,
                labels=CLASS_NAMES,
                ylabel=''
            ).get_figure()
        )

    # --- Bảng Lịch Sử Gần Nhất ---
    show_df = hist_df.copy()
    show_df = show_df[["predict", "confidence", "loai_du_doan"]] if "loai_du_doan" in show_df.columns else show_df
    for col in ["predict", "loai_du_doan"]:
        if col in show_df.columns:
            show_df[col] = show_df[col].astype(str).str.title()
    show_df = show_df.fillna("")
    st.markdown("---")
    st.write("**Lịch Sử Gần Nhất:**")
    st.dataframe(show_df.tail(10).iloc[::-1], use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
