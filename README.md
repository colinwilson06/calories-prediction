# 🔥 Calories Prediction App 🥗⚡

[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://calories-prediction-9k3nbthttphmqysnzlwsnz.streamlit.app/)
[![YouTube Demo](https://img.shields.io/badge/Demo-Video-green)](https://youtu.be/082eVOTRcy8?si=6U7zqx-Dav3cKDxZ)

A **machine learning web application** that predicts the number of calories burned based on user inputs.  
Built with **Streamlit** for interactivity and deployed for instant access on the web.  

---

## ✨ Features
- ✅ Simple and intuitive web interface  
- ✅ Input activity parameters → instant calorie prediction  
- ✅ Powered by **XGBoost** & **Scikit-learn**  
- ✅ Lightweight and fast inference  
- ✅ Deployed and accessible online via Streamlit  

---

## 🎬 Demo

- 🌍 **Live App**: [Open Here](https://calories-prediction-9k3nbthttphmqysnzlwsnz.streamlit.app/)  
- 🎥 **Video Walkthrough**: [Watch on YouTube](https://youtu.be/082eVOTRcy8?si=6U7zqx-Dav3cKDxZ)  
- 🖼️ **Screenshots**: See [`/screenshots`](./screenshots)  

Example Screenshot:  
![App Screenshot](./screenshots/example.png)

---

## 🛠️ Tech Stack
- **Python**  
- **Streamlit** (Frontend/UI)  
- **Pandas, NumPy** (Data processing)  
- **Scikit-learn** (Preprocessing & pipeline)  
- **XGBoost** (Prediction model)  
- **Joblib** (Model serialization)  

---

## 🚀 How to Run Locally

### Step 1: Clone the repository
```bash
git clone https://github.com/colinwilson06/calories-prediction.git
cd calories-prediction
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the application
```bash
streamlit run app.py
```
**You can also run it directly without installation from here:** 


## 📂 Project Structure
```bash
calories-prediction/
│
├── demo/               # demo video files
├── screenshots/        # app screenshots
├── app.py              # main Streamlit app
├── model.pkl           # trained ML model
├── scaler_X.pkl        # input scaler
├── scaler_y.pkl        # output scaler
├── requirements.txt    # dependencies
└── README.md           # documentation
```

## 📊 Model Overview

- Algorithm: XGBoost Regressor
- Preprocessing: Scaling input & output features using Scikit-learn
- Output: Predicted calories burned displayed directly on screen

(Future work: support multiple models, visual error metrics, and custom dataset uploads)


👤 Author
Created by Colin Wilson 👨‍💻
