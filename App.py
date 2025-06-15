import streamlit as st

st.set_page_config(
    page_title="🚗 AI Driver Behavior Classifier PRO",
    page_icon="🚦",
    layout="wide"
)

# ==== Custom CSS for beautiful hero section and how-to ====
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
    /* CSS for Hero Section */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700;900&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', 'Segoe UI', Arial, sans-serif;
        background: #fcfcff;
    }
    .hero-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 0.8em;
        margin-bottom: 1.2em;
        gap: 0.8em;
    }
    .hero-logo {
        width: 112px;
        height: 112px;
        margin-bottom: -0.5em;
        filter: drop-shadow(0 8px 32px #6366f122);
        background: rgba(255,255,255,0.9);
        border-radius: 50%;
        padding: 10px;
        border: 2.5px solid #e0e7ffcc;
        z-index: 2;
        position: relative;
        object-fit: contain;
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: 900;
        letter-spacing: 2px;
        background: linear-gradient(90deg, #6a8cff 30%, #a084ee 60%, #7f53ac 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-top: 0.1em;
        margin-bottom: 0.5em;
        filter: drop-shadow(0 6px 36px #6366f133);
        text-shadow: 0 2px 8px #c7d2fe44;
        text-transform: capitalize;
    }
    .hero-badge {
        display: inline-block;
        padding: 0.6em 1.6em;
        font-size: 1.1rem;
        font-weight: 700;
        background: linear-gradient(90deg, #6366f1 10%, #a084ee 100%);
        color: #fff;
        border-radius: 1.6em;
        box-shadow: 0 6px 32px #6366f143, 0 3px 0 #a5b4fc55;
        margin-bottom: 0.3em;
        letter-spacing: 0.5px;
        text-align: center;
        filter: blur(0px);
        transition: filter 0.23s;
        text-transform: capitalize;
    }
    .hero-badge:hover {
        filter: blur(1.2px) brightness(1.03);
    }
    .hero-desc-row {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1.2em 1.7em;
        background: linear-gradient(90deg,rgba(99,102,241,0.08) 0%,rgba(236,72,153,0.07) 100%);
        border-radius: 18px;
        box-shadow: 0 3px 30px #a084ee22, 0 2.5px 0 #fbc2eb25;
        gap: 1.1em;
        font-size: 1.15rem;
        font-weight: 500;
        margin-top: 0.4em;
        margin-bottom: 0.6em;
        color: #3b2f63;
        border: 2.2px solid #f3e8ff;
        text-align: center;
        max-width: 800px;
        width: 95vw;
        text-transform: none;
        transition: box-shadow 0.18s;
    }
    .hero-desc-row:hover {
        box-shadow: 0 8px 38px #a084ee44, 0 4px 0 #fbc2eb49;
    }
    .desc-icon {
        font-size: 1.45em;
        margin-right: 0.4em;
        margin-left: 0.1em;
        vertical-align: -0.16em;
    }
    .desc-arrow {
        font-size: 1.19em;
        margin: 0 0.45em;
        vertical-align: -0.06em;
        color: #6366f1;
    }
    /* Feature card giữ nguyên đẹp */
    .feature-card {
        background: rgba(255,255,255,0.64);
        border-radius: 22px;
        box-shadow: 0 2px 24px 0 #6366f122, 0 0.5px 0 #a5b4fc22;
        padding: 1.3em 2.2em 1.3em 1.7em;
        margin-bottom: 2.1em;
        display: flex;
        align-items: center;
        gap: 1.2em;
        text-transform: capitalize;
        max-width: 650px;
        margin-left: auto;
        margin-right: auto;
        transition: transform 0.19s, box-shadow 0.22s, background 0.19s;
        cursor: pointer;
        border: 1.5px solid #e0e7ff88;
        backdrop-filter: blur(3.5px);
        -webkit-backdrop-filter: blur(3.5px);
    }
    .feature-card:hover {
        transform: translateY(-7px) scale(1.045) rotate(-1.5deg);
        box-shadow: 0 14px 40px 0 #6366f1bb, 0 2.5px 0 #a5b4fc33;
        background: linear-gradient(112deg, #e0e7ff 70%, #fff0 100%);
        border: 2.5px solid #6366f1bb;
    }
    .feature-icon {
        font-size: 2.7rem;
        margin-right: 0.4em;
        min-width: 2.9em;
        text-align: center;
        filter: drop-shadow(0 2px 8px #6366f133);
        transition: filter 0.25s, transform 0.18s;
    }
    .feature-card:hover .feature-icon {
        filter: drop-shadow(0 8px 20px #6366f1cc);
        transform: scale(1.11) rotate(7deg);
    }
    /* How-to Section CSS */
    .howto-section {
        margin: 2.3em auto 0.4em auto;
        max-width: 600px;
        padding: 1.8em 2.2em 1.5em 2.2em;
        border-radius: 18px;
        background: rgba(255,255,255,0.68);
        box-shadow: 0 2px 24px #6366f111, 0 1.5px 0 #a5b4fc18;
        position: relative;
        border: 2px solid #e0e7ffbb;
        backdrop-filter: blur(3px);
    }
    .howto-title {
        color: #4338ca;
        font-size: 1.32rem;
        font-weight: 700;
        letter-spacing: 1px;
        margin-bottom: 1.2em;
        text-align:center;
        text-transform: capitalize;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.38em;
    }
    .howto-title .howto-icon {
        font-size: 1.38em;
        filter: drop-shadow(0 2px 7px #6366f199);
        margin-right: 0.16em;
    }
    .howto-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .howto-list li {
        font-size: 1.09rem;
        color: #312e81;
        margin-bottom: 1em;
        background: linear-gradient(90deg, #e0e7ff 60%, #fbc2eb44 100%);
        border-radius: 11px;
        font-weight: 500;
        padding: 0.88em 1.2em 0.88em 0.9em;
        box-shadow: 0 1.5px 7px #6366f108;
        display: flex;
        align-items: flex-start;
        gap: 0.75em;
        text-transform: capitalize;
        position: relative;
    }
    .howto-list li:last-child {margin-bottom:0;}
    .howto-list .li-bullet {
        font-size: 1.22em;
        margin-right: 0.46em;
        margin-top: 0.12em;
        min-width: 1.5em;
        text-align: center;
        color: #6366f1;
        filter: drop-shadow(0 1.5px 7px #6366f144);
    }
    @media (max-width: 900px) {
        .hero-title { font-size: 1.45rem; }
        .hero-badge { font-size: 0.95rem;}
        .feature-card { padding: 1em; flex-direction: column; gap:0.7em; }
        .feature-icon { font-size: 2.1rem; }
        .howto-title {font-size: 1.1rem;}
        .howto-section {padding: 1.1em 0.7em;}
    }
    @media (max-width: 600px) {
        .hero-logo { width: 70px; height: 70px;}
        .hero-title { font-size: 1.05rem; }
        .hero-badge { font-size: 0.75rem; }
        .feature-card { padding: 0.7em; }
        .feature-icon { font-size: 1.3rem; }
        .howto-title {font-size: 0.97rem;}
        .howto-section {padding: 0.7em 0.2em;}
    }
    </style>
""", unsafe_allow_html=True)

# ==== Hero Section HTML ====
st.markdown(f'''
<div class="hero-section">
    <img src="https://cdn-icons-png.flaticon.com/512/854/854878.png" class="hero-logo"/>
    <div class="hero-title">
        AI Driver Behavior Classifier
    </div>
    <div class="hero-badge">
        Nền Tảng AI Nhận Diện Hành Vi Lái Xe Chuyên Nghiệp
    </div>
    <div class="hero-desc-row">
        <span class="desc-icon">✨</span>
        Upload Ảnh, Chọn Mô Hình
        <span class="desc-arrow">▶️</span>
        Nhận Kết Quả Cực Nhanh, Cực Kỳ Chính Xác!
    </div>
</div>
''', unsafe_allow_html=True)

# FEATURE CARDS
features = [
    {"icon": "🚗", "title": "Nhận Diện Hành Vi Lái Xe", "desc": "Chỉ Cần Tải Ảnh Hoặc Video, AI Sẽ Dự Đoán Các Hành Vi Tài Xế: Sử Dụng Điện Thoại, Buồn Ngủ, Không Tập Trung, V.V..."},
    {"icon": "📊", "title": "Dashboard Thống Kê Trực Quan", "desc": "Biểu Đồ, Thống Kê Hành Vi Theo Thời Gian, Mô Hình, So Sánh Tốc Độ Và Độ Chính Xác."},
    {"icon": "🕓", "title": "Lịch Sử Dự Đoán", "desc": "Lưu Lại Các Lần Nhận Diện, Dễ Dàng Tra Cứu Và So Sánh Kết Quả."},
    {"icon": "⚡", "title": "Xử Lý Nhanh, Giao Diện Thân Thiện", "desc": "Không Cần Cài Đặt Phức Tạp, Mọi Thao Tác Chỉ Với Vài Cú Click!"}
]
for f in features:
    st.markdown(
        f"""<div class="feature-card">
            <span class="feature-icon">{f['icon']}</span>
            <div>
                <b>{f['title']}</b><br>{f['desc']}
            </div>
        </div>""", unsafe_allow_html=True)

# HOWTO SECTION - hướng dẫn đẹp
st.markdown('''
<div class="howto-section">
    <div class="howto-title"><span class="howto-icon">📝</span> Cách Sử Dụng</div>
    <ul class="howto-list">
        <li><span class="li-bullet">1️⃣</span>Chọn Mục 'Nhận Diện' Ở Sidebar Để Upload Ảnh/Video Hành Vi Lái Xe.</li>
        <li><span class="li-bullet">2️⃣</span>Chọn Mô Hình AI Phù Hợp (MobileNet, EfficientNet...).</li>
        <li><span class="li-bullet">3️⃣</span>Nhấn Nhận Diện Để Xem Kết Quả.</li>
        <li><span class="li-bullet">4️⃣</span>Xem Dashboard Để Thống Kê Lịch Sử, Đánh Giá Hiệu Quả Mô Hình.</li>
    </ul>
</div>
''', unsafe_allow_html=True)