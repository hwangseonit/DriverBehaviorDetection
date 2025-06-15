import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="📊 Dashboard", layout="centered")
HISTORY_CSV = "history.csv"
CLASS_NAMES = ["Other", "Safe", "Talking", "Texting", "Turning"]

# ===== CSS Dashboard Pastel Glass, Gradient, Title Case, Không Xuống Dòng Hành Vi =====
st.markdown("""
<style>
    /* Sidebar nền glass sáng, gradient xanh-cam nhạt, bóng đổ nhẹ */
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

/* Menu item container và danh sách menu */
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

/* Link cơ bản */
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

/* Hover + focus: nổi, nền trắng đục, bóng nhẹ, chữ xanh đậm */
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

/* Active: gradient xanh-cam nhạt, chữ trắng + xanh, bóng nổi */
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

/* Ẩn dòng đỏ ở trên cùng (nếu muốn) */
div[data-testid="stDecoration"] {
    background: transparent !important;
    height: 0px !important;
}

/* Logo hoặc icon sidebar (nếu có) */
section[data-testid="stSidebar"] img,
section[data-testid="stSidebar"] svg {
    filter: drop-shadow(0 2px 10px #bae6fd55);
}

/* Responsive: nhỏ lại */
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

# Tiêu đề đẹp, không xuống dòng chữ "Hành Vi"
st.markdown("""
<div class="dashboard-title">
    <span style="font-size:2.1rem;vertical-align:-0.26em;filter:drop-shadow(0 2px 10px #6366f155);margin-right:0.22em;">📊</span>
    Dashboard Thống Kê <span style="white-space:nowrap;">Hành Vi</span>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="big-card">', unsafe_allow_html=True)
    # --- Đọc dữ liệu từ session_state nếu có, ưu tiên hơn file CSV ---
    hist_df = None
    if "history" in st.session_state and st.session_state["history"]:
        # Chuyển lịch sử từ session_state sang DataFrame
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
    elif os.path.isfile(HISTORY_CSV):
        hist_df = pd.read_csv(HISTORY_CSV)

    if hist_df is not None and not hist_df.empty:
        st.subheader("Biểu Đồ Số Lượt Dự Đoán Từng Hành Vi")
        counts = hist_df["predict"].value_counts().reindex(CLASS_NAMES, fill_value=0)
        st.bar_chart(counts)
        st.subheader("Tỉ Lệ Hành Vi Được Phát Hiện")
        st.pyplot(counts.plot.pie(autopct='%1.1f%%', labels=CLASS_NAMES, ylabel='').get_figure())
        st.markdown("---")
        st.write("**Lịch Sử Gần Nhất:**")
        show_df = hist_df.copy()
        show_df = show_df[["predict", "confidence", "loai_du_doan"]] if "loai_du_doan" in show_df.columns else show_df
        # Chuyển cột về Title Case để đồng bộ giao diện
        for col in ["predict", "loai_du_doan"]:
            if col in show_df.columns:
                show_df[col] = show_df[col].astype(str).str.title()
        st.dataframe(show_df.tail(10).iloc[::-1], use_container_width=True)
    else:
        st.info("Chưa Có Dữ Liệu Lịch Sử.")
    st.markdown('</div>', unsafe_allow_html=True)