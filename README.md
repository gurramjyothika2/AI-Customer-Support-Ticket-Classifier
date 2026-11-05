# AI-Powered Customer Support Ticket Classifier

## Project Overview
An end-to-end customer support analytics and machine learning project that automatically classifies support tickets using NLP and machine learning, stores ticket data in SQL, and provides a Power BI analytics dashboard.

## Key Features
- Customer support ticket dataset
- NLP text processing using TF-IDF
- Machine learning category classifier
- Priority and sentiment rule-based classification
- Recommended support-team routing
- SQL analysis queries
- Streamlit demo application
- Power BI dashboard guide

## Tech Stack
Python, Pandas, Scikit-learn, NLP, TF-IDF, Logistic Regression, SQL, Power BI, Streamlit

## Folder Structure

AI_Customer_Support_Ticket_Classifier/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── customer_support_tickets.csv
│
├── models/
│   └── ticket_category_model.joblib  (created after training)
│
├── src/
│   ├── train_model.py
│   └── predict_ticket.py
│
├── sql/
│   └── customer_support_analysis.sql
│
└── powerbi/
    └── POWER_BI_DASHBOARD_GUIDE.md

## How to Run

### 1. Install packages
pip install -r requirements.txt

### 2. Train the model
python src/train_model.py

This creates:
models/ticket_category_model.joblib

### 3. Test from command line
python src/predict_ticket.py

### 4. Run the web application
streamlit run app.py

## Example Ticket
"I was charged twice for my order and need a refund."

Expected classification:
- Category: Billing
- Priority: High
- Sentiment: Negative
- Recommended Team: Billing Support

## Business Value
The project demonstrates how customer support teams can automate first-level ticket routing, identify high-priority issues, monitor SLA performance, and analyze support workload.

## Resume Skills
Python, Pandas, Scikit-learn, NLP, Machine Learning, TF-IDF, Logistic Regression, SQL, Power BI, Data Analysis, Customer Support Analytics

## Important
This project uses a synthetic dataset created for portfolio and educational purposes. Do not claim that the data came from a real company.
