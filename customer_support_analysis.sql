-- AI-Powered Customer Support Ticket Classifier
-- Compatible with MySQL 8+ with minor adjustments for other SQL databases.

CREATE DATABASE IF NOT EXISTS customer_support_ai;
USE customer_support_ai;

CREATE TABLE customer_support_tickets (
    Ticket_ID VARCHAR(20) PRIMARY KEY,
    Ticket_Text TEXT NOT NULL,
    Category VARCHAR(50),
    Priority VARCHAR(20),
    Sentiment VARCHAR(20),
    Channel VARCHAR(30),
    Customer_Type VARCHAR(30),
    Resolution_Time_Hours DECIMAL(10,2),
    SLA_Status VARCHAR(30),
    Recommended_Team VARCHAR(50)
);

-- After importing customer_support_tickets.csv, run these analysis queries.

-- 1. Total tickets
SELECT COUNT(*) AS Total_Tickets
FROM customer_support_tickets;

-- 2. Tickets by category
SELECT Category, COUNT(*) AS Ticket_Count
FROM customer_support_tickets
GROUP BY Category
ORDER BY Ticket_Count DESC;

-- 3. Tickets by priority
SELECT Priority, COUNT(*) AS Ticket_Count
FROM customer_support_tickets
GROUP BY Priority
ORDER BY Ticket_Count DESC;

-- 4. Average resolution time by category
SELECT Category, ROUND(AVG(Resolution_Time_Hours), 2) AS Avg_Resolution_Hours
FROM customer_support_tickets
GROUP BY Category
ORDER BY Avg_Resolution_Hours DESC;

-- 5. SLA breach percentage
SELECT
    ROUND(
        100.0 * SUM(CASE WHEN SLA_Status = 'Breached' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS SLA_Breach_Percentage
FROM customer_support_tickets;

-- 6. Negative sentiment by category
SELECT Category, COUNT(*) AS Negative_Tickets
FROM customer_support_tickets
WHERE Sentiment = 'Negative'
GROUP BY Category
ORDER BY Negative_Tickets DESC;

-- 7. Channel performance
SELECT Channel,
       COUNT(*) AS Total_Tickets,
       ROUND(AVG(Resolution_Time_Hours), 2) AS Avg_Resolution_Hours
FROM customer_support_tickets
GROUP BY Channel
ORDER BY Total_Tickets DESC;

-- 8. High-priority SLA breaches
SELECT Ticket_ID, Category, Priority, Resolution_Time_Hours
FROM customer_support_tickets
WHERE Priority = 'High'
  AND SLA_Status = 'Breached'
ORDER BY Resolution_Time_Hours DESC;
