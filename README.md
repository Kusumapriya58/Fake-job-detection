🚀 Fake Job Detection Using NLP

A Machine Learning project that detects fake job postings using Natural Language Processing (NLP) with a Flask-based web interface and admin dashboard.


---

📌 Table of Contents

Project Overview

Features

Tech Stack

Project Structure

Installation

Model Training

Run the Web App

How It Works

Admin Panel

Dataset

Future Enhancements

Author



---

📖 Project Overview

Fake job postings are increasing across online platforms and often cause financial & personal risk to job seekers.
This project uses Machine Learning + NLP to classify job descriptions as:

🟢 Real Job Post

🔴 Fake Job Post


A Flask web app allows users to paste job text and get predictions in real-time with confidence scores.


---

⭐ Features

🧠 Machine Learning

Logistic Regression classifier

TF-IDF vectorizer

90%+ accuracy

Predicts real vs fake job posts


🌐 Web Interface (Flask)

Simple & clean dark-theme UI

Paste job description → Get prediction instantly


🔐 Admin Panel

Login system

Admin dashboard

Fake/real job statistics


📊 Dashboard Stats

Total predictions

Fake vs Real detected



---

🛠 Tech Stack

Component	Technology

Programming	Python
Web Framework	Flask
NLP	TF-IDF Vectorizer
Machine Learning	Logistic Regression
Dataset	Fake Job Postings Dataset (Kaggle)
UI	HTML, CSS (Dark UI)



---

📂 Project Structure

project/
│── app.py
│── train_model.py
│── fake_job_model.pkl
│── vectorizer.pkl
│── fake_job_postings.csv
│── templates/
│     ├── index.html
│     ├── result.html
│     ├── admin.html
│     └── dashboard.html
│── static/
│     └── (optional CSS)
│── README.md


---

⚙ Installation

⿡ Clone the Repository

git clone https://github.com/your-username/fake-job-detection.git
cd fake-job-detection

⿢ Install Dependencies

pip install flask scikit-learn joblib pandas numpy


---

🧪 Model Training

Run the training script:

python train_model.py

It will generate:

fake_job_model.pkl
vectorizer.pkl

These files are used during prediction in the web app.


---

🚀 Run the Web App

Start the Flask app:

python app.py

Then open browser:

http://127.0.0.1:5000/


---

🔍 How It Works

✨ Input

User pastes a job description text.

⚙ Processing

1. Text cleaned (punctuation, URLs, HTML, lowercase).


2. TF-IDF features generated.


3. Model predicts Real or Fake.


4. Shows the confidence percentage.



📤 Output

Example:

Prediction: FAKE JOB POST  
Confidence: 92.13%


---

🔐 Admin Panel

Login

Username: admin  
Password: admin123

Dashboard Displays

Total predictions

Fake jobs detected

Real jobs detected



---

📊 Dataset

This project uses the Fake Job Postings dataset from Kaggle.
It contains job descriptions labeled as:

0 → Real

1 → Fake



---

🚧 Future Enhancements

Add deep learning (BERT / LSTM)

Add MySQL/MongoDB logging

Add chart-based analytics

Deploy on Render / Railway / AWS

Add email alert for suspicious posts





