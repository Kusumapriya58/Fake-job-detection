# train_model.py
import pandas as pd
import numpy as np
import re
import string
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("fake_job_postings.csv")  # Use Kaggle dataset
df = df[['description', 'fraudulent']]
df.dropna(inplace=True)

# -----------------------------
# 2. Clean Text
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\d+", "", text)
    return text

df['cleaned'] = df['description'].apply(clean_text)

# -----------------------------
# 3. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    df['cleaned'], df['fraudulent'], test_size=0.2, random_state=42
)

# -----------------------------
# 4. TF-IDF Vectorizer
# -----------------------------
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# -----------------------------
# 5. Train Model
# -----------------------------
model = LogisticRegression(max_iter=300)
model.fit(X_train_tfidf, y_train)

# -----------------------------
# 6. Evaluate
# -----------------------------
pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))

# -----------------------------
# 7. Save Model
# -----------------------------
joblib.dump(model, "fake_job_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model and vectorizer saved successfully!")