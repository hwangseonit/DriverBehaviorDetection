import streamlit as st
st.set_page_config(page_title="🖼️ Nhận Diện", layout="centered")
import numpy as np
from PIL import Image
import cv2
import tempfile
import os
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import requests
from io import BytesIO

# ==== Download Model ====
def download_model_if_not_exists(drive_url, save_path):
    if not os.path.exists(save_path):
        import gdown
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with st.spinner(f"Đang tải {os.path.basename(save_path)} từ Google Drive..."):
            gdown.download(drive_url, save_path, quiet=False)

MODEL_LINKS = {
    'DenseNet': 'https://drive.google.com/uc?id=1oZmWHY5rub52FnHm1J2IM2kXTZRs6_Ew',
    'EfficientNet': 'https://drive.google.com/uc?id=14EGEXZO3L1m8Wbq_fRxLj1uaj-8ewoAf',
    'ResNet': 'https://drive.google.com/uc?id=1MRfaHl_UtMoA9__ok8lZcb2zSELRxmAG'
}
MODEL_PATHS = {
    'DenseNet': 'model/best_model_densenetPMai.h5',
    'EfficientNet': 'model/best_model_efficientnet.h5',
    'ResNet': 'model/best_model_resnet.h5'
}

for name in MODEL_LINKS:
    download_model_if_not_exists(MODEL_LINKS[name], MODEL_PATHS[name])

# ===== BỎ CÁC HÀM TIỀN XỬ LÝ CỦA KERAS, CHỈ CHUẨN HÓA ẢNH VỀ [0, 1] =====

st.markdown("<h1>🚗 Nhận Diện</h1>", unsafe_allow_html=True)

# Thêm mapping nhãn đẹp cho hiển thị và DataFrame
PRETTY_LABELS = {
    "other_activities": "Other",
    "safe_driving": "Safe",
    "talking_phone": "Talking",
    "texting_phone": "Texting",
    "turning": "Turning"
}
PRETTY_LABEL_LIST = ["Other", "Safe", "Talking", "Texting", "Turning"]

def save_history(image, predicted_class, confidence, df, mode="Ảnh"):
    if "history" not in st.session_state:
        st.session_state["history"] = []
    # Lưu ảnh dạng bytes để trang khác có thể hiển thị lại
    buf = BytesIO()
    image.save(buf, format="PNG")
    img_bytes = buf.getvalue()
    st.session_state["history"].append({
        "image_bytes": img_bytes,
        "label": predicted_class,
        "confidence": confidence,
        "details": df,
        "mode": mode
    })

    # Map nhãn model sang nhãn dashboard
    mapping = PRETTY_LABELS
    dashboard_class = mapping.get(str(predicted_class).lower(), str(predicted_class).title())

    # ===== GHI RA FILE CSV ĐỂ DASHBOARD ĐỌC ĐƯỢC =====
    csv_file = "history.csv"
    csv_row = {
        "predict": dashboard_class,
        "confidence": confidence,
        "loai_du_doan": mode
    }
    if os.path.isfile(csv_file):
        pd.DataFrame([csv_row]).to_csv(csv_file, mode='a', header=False, index=False)
    else:
        pd.DataFrame([csv_row]).to_csv(csv_file, mode='w', header=True, index=False)

# ===== CSS=====
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
.stButton>button {
    background: linear-gradient(to right, #06b6d4, #3b82f6);
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 12px;
    padding: 0.7rem 1.5rem;
    margin-top: 1rem;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
}
.stRadio > div {
    flex-direction: row !important;
    justify-content: center;
    gap: 1.5rem;
}
.stRadio > div > label {
    background: rgba(255,255,255,0.1);
    padding: 0.5rem 1rem;
    border-radius: 10px;
    color: white;
    font-weight: 500;
}
.stRadio > div > label:hover {
    background: rgba(255,255,255,0.2);
}
</style>
""", unsafe_allow_html=True)

CLASS_NAMES = ['other_activities', 'safe_driving', 'talking_phone', 'texting_phone', 'turning']

@st.cache_resource
def load_models():
    try:
        return {
            'DenseNet': load_model('model/best_model_densenetPMai.h5'),
            'EfficientNet': load_model('model/best_model_efficientnet.h5'),
            'ResNet': load_model('model/best_model_resnet.h5')
        }
    except Exception as e:
        st.error(f"❌ Lỗi khi tải mô hình: {str(e)}")
        return {}

# ===== TIỀN XỬ LÝ: CHỈ CHIA 255 =====
def preprocess_image(image, model_name):
    try:
        if image.mode != "RGB":
            image = image.convert("RGB")
        image = image.resize((224, 224))
        arr = img_to_array(image)
        arr = arr / 255.0
        return np.expand_dims(arr, axis=0)
    except Exception as e:
        st.error(f"Lỗi tiền xử lý ảnh: {e}")
        return None

def predict(model, img_array):
    predictions = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(predictions)]
    # Map xác suất sang nhãn đẹp cho DataFrame
    pretty_probs = {PRETTY_LABELS[cls]: float(predictions[0][i]) for i, cls in enumerate(CLASS_NAMES)}
    pretty_probs_ordered = [pretty_probs[label] for label in PRETTY_LABEL_LIST]
    return predicted_class, [pretty_probs_ordered]

def query_dify_bot(prompt):
    url = "https://api.dify.ai/v1/chat-messages"
    headers = {
        "Authorization": "Bearer app-xdnSPczSr0oelVVUQc1G1TVF",  # Nên dùng biến môi trường
        "Content-Type": "application/json"
    }
    data = {
        "user": "streamlit-user",
        "conversation_id": None,
        "inputs": {},
        "query": prompt,
        "response_mode": "blocking"
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=20)
        if response.status_code == 200:
            return response.json().get("answer", "⚠️ Không có phản hồi từ AI.")
        else:
            return f"⚠️ Lỗi AI: {response.status_code} - {response.text}"
    except Exception as e:
        return f"❌ Lỗi kết nối tới AI: {str(e)}"

def clear_prediction_state():
    for key in ["predicted_class", "confidence", "df"]:
        if key in st.session_state:
            del st.session_state[key]

models = load_models()
if not models:
    st.stop()

model_choice = st.selectbox("🧠 Chọn mô hình", list(models.keys()))
option = st.radio("📂 Chọn loại đầu vào", ["Ảnh", "Video"])

if option == "Ảnh":
    uploaded_image = st.file_uploader("🖼️ Tải ảnh", type=["jpg", "jpeg", "png"])
    # Xóa kết quả khi không còn ảnh
    if not uploaded_image:
        clear_prediction_state()
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Ảnh đã tải", use_container_width=True)
        if st.button("🚀 Dự đoán từ ảnh"):
            model = models[model_choice]
            input_array = preprocess_image(image, model_choice)
            if input_array is not None:
                predicted_class, pretty_predictions = predict(model, input_array)
                pretty_label = PRETTY_LABELS.get(predicted_class, predicted_class)
                confidence = float(np.max(pretty_predictions))
                st.session_state.predicted_class = pretty_label
                st.session_state.confidence = confidence
                st.session_state.df = pd.DataFrame(pretty_predictions, columns=PRETTY_LABEL_LIST)
                save_history(image, pretty_label, confidence, st.session_state.df, mode="Ảnh")

elif option == "Video":
    uploaded_video = st.file_uploader("📹 Tải video", type=["mp4", "avi", "mov"])
    # Xóa kết quả khi không còn video
    if not uploaded_video:
        clear_prediction_state()
    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        cap = cv2.VideoCapture(tfile.name)
        model = models[model_choice]
        frame_count = 0
        predictions_accum = []
        first_frame_img = None
        with st.spinner("⏳ Đang xử lý video..."):
            while cap.isOpened() and frame_count < 30:
                ret, frame = cap.read()
                if not ret:
                    break
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img_pil = Image.fromarray(frame_rgb)
                if first_frame_img is None:
                    first_frame_img = img_pil.copy()  # Lưu frame đầu làm đại diện
                input_array = preprocess_image(img_pil, model_choice)
                if input_array is not None:
                    _, pretty_probs = predict(model, input_array)
                    predictions_accum.append(pretty_probs[0])
                frame_count += 1
        cap.release()
        os.unlink(tfile.name)
        if predictions_accum:
            avg_pred = np.mean(predictions_accum, axis=0)
            idx = int(np.argmax(avg_pred))
            pretty_label = PRETTY_LABEL_LIST[idx]
            confidence = float(np.max(avg_pred))
            st.session_state.predicted_class = pretty_label
            st.session_state.confidence = confidence
            st.session_state.df = pd.DataFrame([avg_pred], columns=PRETTY_LABEL_LIST)
            if first_frame_img is not None:
                save_history(first_frame_img, pretty_label, confidence, st.session_state.df, mode="Video")

# ===== Hiển thị kết quả =====
if "predicted_class" in st.session_state:
    st.markdown(f'<div class="result-label">🚩 {st.session_state.predicted_class.upper()}</div>', unsafe_allow_html=True)
    st.progress(st.session_state.confidence, text=f"Độ tin cậy: {st.session_state.confidence:.2%}")
    with st.expander("📊 Xem chi tiết phân bố dự đoán"):
        df = st.session_state.df
        st.dataframe(df.style.format("{:.2%}"))

    # ===== AI Trợ lý =====
    st.subheader("🤖 AI Trợ Lý Giải Thích")
    user_question = st.text_input("💬 Câu hỏi của bạn về hành vi này")
    ask = st.button("📨 Gửi câu hỏi")
    if ask and user_question:
        with st.spinner("🤖 AI đang suy nghĩ..."):
            ai_answer = query_dify_bot(f"Người dùng hỏi: {user_question}. Kết quả phân loại hành vi là: {st.session_state.predicted_class}")
            st.markdown(f"<div class='result-box'>{ai_answer}</div>", unsafe_allow_html=True)
