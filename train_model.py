"""
AI-Powered Customer Support Ticket Classifier
Train and save a ticket-category model.

Run:
    pip install -r requirements.txt
    python src/train_model.py
"""

from pathlib import Path
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "customer_support_tickets.csv"
MODEL_DIR = ROOT / "models"
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
X_train, X_test, y_train, y_test = train_test_split(
    df["Ticket_Text"], df["Category"], test_size=0.20, random_state=42, stratify=df["Category"]
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english", ngram_range=(1, 2))),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)
pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, pred):.2%}")
print("\nClassification Report:\n")
print(classification_report(y_test, pred))

joblib.dump(model, MODEL_DIR / "ticket_category_model.joblib")
print(f"\nModel saved to: {MODEL_DIR / 'ticket_category_model.joblib'}")
