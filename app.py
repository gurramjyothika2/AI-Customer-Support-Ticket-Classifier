import streamlit as st
from pathlib import Path
import joblib

ROOT = Path(__file__).resolve().parent
MODEL = ROOT / "models" / "ticket_category_model.joblib"

TEAM_MAP = {
    "Billing": "Billing Support",
    "Technical": "Technical Support",
    "Delivery": "Logistics Support",
    "Account": "Account Support",
    "Product": "Product Support"
}

st.set_page_config(page_title="AI Customer Support Classifier", page_icon="🎫", layout="centered")

st.title("🎫 AI-Powered Customer Support Ticket Classifier")
st.write("Enter a customer support message and the model will classify the ticket.")

ticket = st.text_area(
    "Customer Ticket",
    placeholder="Example: I was charged twice for my order and need a refund."
)

if st.button("Classify Ticket"):
    if not ticket.strip():
        st.warning("Please enter a ticket.")
    else:
        model = joblib.load(MODEL)
        category = model.predict([ticket])[0]

        text = ticket.lower()
        urgent_words = ["urgent", "immediately", "fraud", "charged twice", "cannot", "error", "damaged", "blocked"]
        priority = "High" if any(w in text for w in urgent_words) else "Medium"

        negative_words = ["frustrating", "angry", "wrong", "damaged", "defective", "error", "cannot", "delayed", "bad"]
        sentiment = "Negative" if any(w in text for w in negative_words) else "Neutral"

        st.success("Ticket classified successfully!")
        col1, col2 = st.columns(2)
        col1.metric("Category", category)
        col2.metric("Priority", priority)

        st.metric("Sentiment", sentiment)
        st.info(f"Recommended Team: {TEAM_MAP[category]}")
