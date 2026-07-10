# 🩺 Medical Diagnosis Prediction System

An end-to-end Machine Learning web application that predicts whether a person is **Healthy**, **at risk of Heart Disease**, or **at risk of Diabetes** using a **Decision Tree Classifier**.

The application is built with **Flask** and provides an interactive web interface where users can enter medical parameters and receive an instant prediction.

---

## 📌 Features

- Predicts three possible outcomes:
  - ✅ Healthy
  - ❤️ Heart Disease Risk
  - 🩸 Diabetes Risk
- User-friendly web interface
- Real-time prediction using a trained ML model
- Flask-based backend
- Responsive frontend
- Clean project structure

---

## 🎯 Model Information

| Attribute | Details |
|-----------|---------|
| Algorithm | Decision Tree Classifier |
| Model Accuracy | **91.48%** |
| Dataset | Kaggle - medical_diagnosis_1200rows |
| Problem Type | Multi-Class Classification |

---

## 🛠 Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML5
- CSS3

---

## 📂 Project Structure

```
Medical-Diagnosis-Prediction/
│
├── app.py                 # Flask application
├── model.py               # Model training script
├── model.pkl              # Saved ML model
├── requirements.txt
│
├── templates/
│   ├── index.html         # User input page
│   └── result.html        # Prediction page
│
├── static/
│   └── style.css
│
├── dataset/
│   └── medical_diagnosis_1200rows.csv
│
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Medical-Diagnosis-Prediction.git
```

Move into the project directory

```bash
cd Medical-Diagnosis-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 🚀 How It Works

1. User enters medical information.
2. Flask receives the input.
3. Input data is processed.
4. The trained Decision Tree model makes a prediction.
5. The prediction is displayed on the result page.

---

## 📸 Screenshots

### Home Page

> Add a screenshot here

```
images/home.png
```

---

### Prediction Result

> Add a screenshot here

```
images/result.png
```

---

## 📊 Workflow

```
User Input
      │
      ▼
Flask Backend
      │
      ▼
Data Preprocessing
      │
      ▼
Decision Tree Model
      │
      ▼
Prediction
      │
      ▼
Result Page
```

---

## 🎓 Learning Outcomes

Through this project I gained hands-on experience with:

- Machine Learning Classification
- Decision Tree Algorithm
- Data Preprocessing
- Model Serialization using Pickle
- Flask Web Development
- Model Deployment
- Frontend-Backend Integration

---

## 🔮 Future Improvements

- Support additional diseases
- Improve prediction accuracy using ensemble models
- Add probability/confidence score
- User authentication
- Database integration
- Medical report generation
- Deploy on Render or Railway
- Docker support

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is developed for educational purposes.

---

## 👨‍💻 Author

**Darshan Patil**

GitHub: https://github.com/darshan1845

LinkedIn: https://www.linkedin.com/in/darshanpatil1

---

### ⭐ If you found this project useful, don't forget to give it a Star!
