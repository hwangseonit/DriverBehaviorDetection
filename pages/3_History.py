import streamlit as st
import pandas as pd
from io import BytesIO
# ==== Cấu Hình Trang ====
st.set_page_config(page_title="📜 Lịch sử", layout="centered")
st.markdown("<h1>📜 Lịch Sử Dự Đoán Hành Vi Lái Xe</h1>", unsafe_allow_html=True)

# ==== CSS ====

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
# ===== Css Trang =====
html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(-45deg, #0f172a, #1e3a8a, #06b6d4, #3b82f6);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: #f8fafc;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
h1 {
    text-align: center;
    font-size: 3rem;
    font-weight: 900;
    color: white;
    margin-top: 1.2rem;
    margin-bottom: 2.2rem;
    white-space: nowrap;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.4);
}
.result-label {
    font-size: 2.5rem;
    font-weight: 700;
    color: #22d3ee;
    text-align: center;
    margin-top: 2rem;
}
.result-box {
    background: rgba(255,255,255,0.1);
    border-radius: 15px;
    padding: 2rem;
    margin-top: 1.5rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# ==== Hiển thị lịch sử ====
if "history" in st.session_state and st.session_state["history"]:
    for record in reversed(st.session_state["history"]):
        mode = record.get("mode", "Ảnh")
        if mode == "Ảnh":
            st.markdown('<div class="result-label">🖼️ ẢNH</div>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="result-box">Độ Tin Cậy: {record["confidence"]:.2%} <br>Kết Quả Dự Đoán: {record["label"]}</div>',
                unsafe_allow_html=True
            )
            st.image(BytesIO(record["image_bytes"]), caption=f"Ảnh Đại Diện ({record['label']})",
                     use_container_width=True)
            if "details" in record:
                with st.expander("📊 Xem Chi Tiết Phân Bố Dự Đoán"):
                    st.dataframe(record["details"].style.format("{:.2%}"))
        elif mode == "Video":
            st.markdown(f'<div class="result-label">🎞️ VIDEO</div>', unsafe_allow_html=True)
            # Hiển thị ảnh đại diện (frame đầu video)
            if "thumbnail_bytes" in record:
                st.image(BytesIO(record["thumbnail_bytes"]), caption="Ảnh Đại Diện (Video)", use_container_width=True)
            # Hiển thị tỉ lệ các hành vi
            stats = record.get("behavior_stats", {})
            if stats:
                stat_df = pd.DataFrame([stats])
                st.markdown("### 📊 Tỉ Lệ Các Hành Vi Trong Video")
                st.dataframe(stat_df.style.format("{:.0f}"))
        st.markdown("---")
else:
    st.info("Chưa Có Lịch Sử Dự Đoán Nào.")
