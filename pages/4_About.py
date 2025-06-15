import streamlit as st

st.set_page_config(page_title="ℹ️ Giới Thiệu", layout="centered")

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
.center-title {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 2.2rem;
    margin-bottom: 1.2rem;
}
.gioithieu-title {
    font-size: 2.2rem;
    font-weight: 900;
    letter-spacing: 1.2px;
    background: linear-gradient(90deg, #6366f1 15%, #38bdf8 55%, #0ea5e9 90%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-transform: capitalize;
    text-align: center;
    line-height: 1.12;
    margin-left: 0.25em;
}
h2, h3, h4 {
    text-align: center;
    font-weight: 800;
    text-transform: capitalize !important;
    letter-spacing: 0.8px;
}
.gioithieu-card {
    background: rgba(255,255,255,0.97);
    border-radius: 30px;
    box-shadow: 0 8px 38px 0 #6366f122, 0 1.5px 0 #a5b4fc22;
    padding: 2.6rem 2.6rem 2.3rem 2.6rem;
    margin: 1.3rem auto 2.7rem auto;
    max-width: 710px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1.6px solid #e0e7ffcc;
    transition: box-shadow 0.2s;
    display: flex;
    flex-direction: column;
    gap: 1.7rem;
}
.gioithieu-card ul, .gioithieu-card ol {
    text-align: left !important;
    margin-left: 1.3em;
    font-size: 1.07em;
    padding-left: 0.2em;
}
.gioithieu-card li {
    margin-bottom: 0.21em;
    text-transform: capitalize;
}
.gioithieu-card strong {
    color: #2563eb;
}
.gioithieu-card .fun {
    color: #f97316;
    font-weight: 700;
    font-style: italic;
    text-transform: none;
}
.gioithieu-card .team {
    color: #0ea5e9;
    font-weight: 900;
    letter-spacing: 1px;
    text-shadow: 0 1px 7px #bae6fd33;
    font-size: 1.08em;
}
.gioithieu-section-title {
    font-size: 1.17rem;
    font-weight: 800;
    background: linear-gradient(90deg, #a5b4fc 10%, #fbc2eb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5em;
    margin-top: 0.9em;
    text-align: center;
    text-transform: capitalize;
    letter-spacing: 0.15em;
}
.gioithieu-row {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2.3em 1.5em;
}
.gioithieu-box {
    background: linear-gradient(120deg, #f0f7fa 60%, #f9fafb 100%);
    border-radius: 18px;
    box-shadow: 0 4px 24px 0 #6366f122;
    padding: 1.33em 1.7em 1.15em 1.7em;
    min-width: 215px;
    max-width: 335px;
    flex: 1 1 240px;
    margin-bottom: 0.8em;
    text-align: center;
    font-size: 1.09em;
    transition: box-shadow 0.17s;
    border: 1px solid #e0e7ff55;
}
.gioithieu-box:hover {
    box-shadow: 0 8px 38px 0 #a5b4fc33, 0 0.5px 0 #fbc2eb44;
}
.gioithieu-icon {
    font-size: 2.2rem;
    display: block;
    margin-bottom: 0.25em;
    filter: drop-shadow(0 2px 10px #a5b4fc77);
}
.gioithieu-card a {
    text-decoration: none;
    color: #0ea5e9;
    font-weight: 700;
}
@media (max-width: 900px) {
    .gioithieu-card {padding: 1.1em 0.5em;}
    .gioithieu-title {font-size: 1.08rem;}
    .gioithieu-row {gap: 1.2em 0.4em;}
}
</style>
""", unsafe_allow_html=True)

# Tiêu đề căn giữa đẹp
st.markdown("""
<div class="center-title">
    <span style="font-size:2.1rem;vertical-align:-0.26em;filter:drop-shadow(0 2px 10px #6366f155);margin-right:0.22em;">ℹ️</span>
    <span class="gioithieu-title">Giới Thiệu</span>
</div>
""", unsafe_allow_html=True)
st.markdown('<h2>👨‍💻 Thông Tin Nhóm & Ứng Dụng</h2>', unsafe_allow_html=True)

# Card chính
st.markdown("""
<div class="gioithieu-card">

<div class="gioithieu-row">
    <div class="gioithieu-box">
        <span class="gioithieu-icon">🤖</span>
        <b>Nhóm 20 Trí Tuệ Nhân Tạo</b><br>
        Đam mê AI, học tập sáng tạo, cùng nhau phát triển sản phẩm giá trị thực tiễn.
    </div>
    <div class="gioithieu-box">
        <span class="gioithieu-icon">🚗</span>
        <b>AI Driver Behavior Classifier Pro</b><br>
        Ứng dụng nhận diện & cảnh báo hành vi tài xế bằng AI hiện đại. Đa mô hình, realtime, bảo vệ an toàn giao thông.
    </div>
</div>

<div class="gioithieu-section-title">🌟 Nổi Bật & Tính Năng</div>
<ul>
    <li>Giao Diện Hiện Đại – Pastel Glass, Responsive, Thống Kê Trực Quan</li>
    <li>Đa Mô Hình: DenseNet, EfficientNet, ResNet</li>
    <li>Lưu Lịch Sử, Dashboard Tương Tác, Đánh Giá Hiệu Năng</li>
    <li>Hỗ Trợ Đa Nền Tảng, Mở Rộng Dễ Dàng</li>
    <li class="fun">🎉 Có Easter Egg Khi Bấm 5 Lần Vào Logo App!</li>
    <li class="fun">🪄 Đếm Số Lần Nhận Diện Thành Công, Tặng Lời Khen Độc Lạ</li>
    <li class="fun">⚡ Chế Độ "Thử Thách": Đua Top Dự Đoán Đúng Nhanh Nhất!</li>
</ul>

<div class="gioithieu-section-title">🔧 Công Nghệ & Đóng Góp</div>
<ul>
    <li>Python, Streamlit, TensorFlow/Keras, Pandas, Matplotlib, Custom CSS</li>
    <li>Multi-Page App, Clean Code, Đầy Đủ Documentation</li>
    <li><b>Github:</b> <a href="https://github.com/hwangseonit/DriverBehaviorDetection.git" target="_blank">hwangseonit</a></li>
    <li><b>Email:</b> AIGroup20@gmail.com</li>
</ul>

<div class="gioithieu-section-title">🌱 Thành Viên & Sứ Mệnh</div>
<ul>
    <li class="team">Nhóm Gồm Các Thành Viên Siêu Dễ Thương Và Nhiệt Huyết</li>
    <li>Mỗi Bạn Tự Chọn 1 Tính Năng Để Phát Triển & Bảo Vệ Cá Nhân</li>
    <li class="fun">🌈 Mục Tiêu: Học Mà Vui, Vui Mà Học!</li>
    <li>Luôn Chào Đón Đóng Góp Ý Tưởng Và Phản Hồi Từ Cộng Đồng</li>
</ul>

<div class="gioithieu-section-title">📅 Thông Tin Khác</div>
<ul>
    <li><b>Phiên Bản:</b> 2.5.5 (2025)</li>
    <li>Tham Gia <a href="https://github.com/hwangseonit/DriverBehaviorDetection.git" target="_blank">Github Project</a> Để Góp Ý Và Nhận Quà Tặng Đặc Biệt!</li>
    <li>💡 Fun Fact: Đội Nhóm Đã Uống Hơn 100 Cốc Trà Sữa Khi Làm App Này!</li>
</ul>

</div>
""", unsafe_allow_html=True)
