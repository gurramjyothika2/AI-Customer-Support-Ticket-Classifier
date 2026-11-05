# Power BI Dashboard Guide

## Dashboard title
AI-Powered Customer Support Analytics

## Import
1. Open Power BI Desktop.
2. Select Get Data > Text/CSV.
3. Choose `data/customer_support_tickets.csv`.
4. Load the table.

## KPI Cards
Create these measures:

Total Tickets =
COUNTROWS(customer_support_tickets)

High Priority Tickets =
CALCULATE(
    COUNTROWS(customer_support_tickets),
    customer_support_tickets[Priority] = "High"
)

Average Resolution Hours =
AVERAGE(customer_support_tickets[Resolution_Time_Hours])

SLA Breach % =
DIVIDE(
    CALCULATE(
        COUNTROWS(customer_support_tickets),
        customer_support_tickets[SLA_Status] = "Breached"
    ),
    COUNTROWS(customer_support_tickets),
    0
)

Negative Sentiment % =
DIVIDE(
    CALCULATE(
        COUNTROWS(customer_support_tickets),
        customer_support_tickets[Sentiment] = "Negative"
    ),
    COUNTROWS(customer_support_tickets),
    0
)

## Recommended visuals

1. KPI cards:
   - Total Tickets
   - High Priority Tickets
   - Average Resolution Hours
   - SLA Breach %
   - Negative Sentiment %

2. Clustered column chart:
   - Axis: Category
   - Values: Count of Ticket_ID

3. Donut chart:
   - Legend: Priority
   - Values: Count of Ticket_ID

4. Column chart:
   - Axis: Category
   - Values: Average Resolution_Time_Hours

5. Donut chart:
   - Legend: Sentiment
   - Values: Count of Ticket_ID

6. Bar chart:
   - Axis: Channel
   - Values: Count of Ticket_ID

7. Table:
   - Ticket_ID
   - Ticket_Text
   - Category
   - Priority
   - Sentiment
   - SLA_Status
   - Resolution_Time_Hours

## Suggested slicers
- Category
- Priority
- Channel
- Customer_Type
- SLA_Status

## Suggested dashboard layout

Top: KPI cards
Middle left: Tickets by Category
Middle right: Tickets by Priority
Bottom left: Average Resolution Time by Category
Bottom middle: Sentiment Distribution
Bottom right: SLA Status
Bottom: Detailed ticket table
