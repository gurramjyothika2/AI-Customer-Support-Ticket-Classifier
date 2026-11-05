"""
Predict the category of a new customer support ticket.

Run:
    python src/predict_ticket.py
"""

from pathlib import Path
import joblib

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "models" / "ticket_category_model.joblib"

TEAM_MAP = {
    "Billing": "Billing Support",
    "Technical": "Technical Support",
    "Delivery": "Logistics Support",
    "Account": "Account Support",
    "Product": "Product Support"
}

def predict(ticket_text):
    model = joblib.load(MODEL)
    category = model.predict([ticket_text])[0]

    text = ticket_text.lower()
    urgent_words = ["urgent", "immediately", "fraud", "charged twice", "cannot", "error", "damaged", "blocked"]
    priority = "High" if any(w in text for w in urgent_words) else "Medium"

    negative_words = ["frustrating", "angry", "wrong", "damaged", "defective", "error", "cannot", "delayed", "bad"]
    sentiment = "Negative" if any(w in text for w in negative_words) else "Neutral"

    return {
        "Category": category,
        "Priority": priority,
        "Sentiment": sentiment,
        "Recommended_Team": TEAM_MAP[category]
    }

if __name__ == "__main__":
    ticket = input("Enter customer support ticket: ").strip()
    result = predict(ticket)
    print("\nPrediction")
    print("-" * 30)
    for key, value in result.items():
        print(f"{key}: {value}")
