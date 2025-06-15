# 🚦 AI Driver Behavior Classifier PRO

An advanced AI-powered application for classifying driver behavior using deep learning models (DenseNet, EfficientNet, ResNet). Built with **Streamlit**, it offers a sleek, modern UI with real-time image/video prediction, interactive dashboards, and historical logs.

![App Screenshot](https://cdn-icons-png.flaticon.com/512/854/854878.png)

---

## 🌟 Features

- 🖼️ **Image & Video Behavior Detection**  
  Upload driver images/videos to detect behaviors in real-time.

- 🧠 **Multiple AI Models Supported**  
  Switch between DenseNet, ResNet, and EfficientNet.

- 📊 **Live Dashboard Analytics**  
  View prediction distribution and historical logs via interactive charts.

- 💾 **Auto Logging**  
  Every prediction is stored with timestamp for easy tracking.

- 🧩 **Modular UI with Streamlit Multi-page App**  
  Clean navigation between "Nhận diện", "Dashboard", "History", and "About".

---

## 📁 Folder Structure

```
Driver Behavior Detection/
├── App.py                 # Main entry point
├── pages/                 # Sub-pages for Streamlit
│   ├── 1_Nhan_dien.py
│   ├── 2_Dashboard.py
│   ├── 3_History.py
│   └── 4_About.py
├── model/                 # Pretrained model files (.h5)
│   ├── best_model_densenetPMai.h5
│   ├── best_model_efficientnet.h5
│   └── best_model_resnet.h5
├── history.csv            # Optional: saved prediction logs
├── requirements.txt
├── runtime.txt
├── Procfile
└── README.md
```

---

## 🚀 Installation & Run Locally

### 🔧 Prerequisites

- Python 3.10
- Pip

### 📥 Setup

```bash
git clone https://github.com/yourusername/driver-behavior-app.git
cd driver-behavior-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deploy on Streamlit Cloud

1. Push your repo to GitHub
2. Go to [https://railway.com/](https://railway.com/)
3. Select your repo & choose `app.py` as the entry point
4. Click **Deploy**

📎 You’ll get a live link like:

```
https://web-production-c3ee.up.railway.app/
```

---

## 🧠 Technologies Used

- **Python**
- **Streamlit**
- **TensorFlow / Keras**
- **OpenCV**
- **Pandas**
- **Custom CSS (Inter font + animations)**

---

## 👨‍💻 Authors

- **Group20AI** – Group 20 Artificial Intelligence
- Contributors: Contributions of all members of the AI ​​20 team!

---

## 💌 Feedback & Contact

- 📬 Email: AI20@hvnh.edu.vn
- 🔗 GitHub: [github.com/hwangseonit](https://github.com/hwangseonit)

---

> “Your driving behavior, decoded by AI – beautifully, instantly, intelligently.”
