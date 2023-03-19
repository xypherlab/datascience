--Create a table with table name yellevate_invoices
CREATE TABLE yellevate_invoices
(
	country VARCHAR,
	customer_id VARCHAR,
	invoice_number NUMERIC,
	invoice_date DATE,
	due_date DATE,
	invoice_amount_usd NUMERIC,
	disputed NUMERIC,
	dispute_lost NUMERIC,
	settled_date DATE,
	days_to_settle INTEGER,
	days_late INTEGER
);

--Make a query to check if table has been successfully created
SELECT *
FROM yellevate_invoices;


--Import csv data thru pgadmin
--Make a query to check if data has been successfully imported. 
SELECT *
FROM yellevate_invoices;

--Check for misspelled words
SELECT DISTINCT country
FROM yellevate_invoices;

--Check for null entries
SELECT *
FROM yellevate_invoices
WHERE NOT (yellevate_invoices IS NOT NULL);



--Check for unique list of clients (determine number of clients)
SELECT DISTINCT customer_id
FROM yellevate_invoices;

--processing time to settle invoice rounded to whole number
SELECT ROUND (AVG(days_to_settle),0) AS processing_time
FROM yellevate_invoices;

--processing time for company to settle dispute
SELECT ROUND (AVG(days_to_settle),0) processing_time
FROM yellevate_invoices
WHERE disputed = 1;

--percentage of disputes lost (using "with" clause)
WITH total AS 
    (
    SELECT count(disputed) as total_disputes
    FROM yellevate_invoices
    WHERE disputed = 1
    )
SELECT disputed, dispute_lost, 
    ROUND ((CAST (COUNT(yellevate_invoices.dispute_lost) AS NUMERIC) 
    / 
    CAST (total.total_disputes AS NUMERIC))*100,2) AS percentage_lost
FROM yellevate_invoices, total
WHERE dispute_lost = 1
GROUP BY disputed, dispute_lost, total.total_disputes;

--percentage of revenue lost
WITH total AS 
    (
    SELECT sum(invoice_amount_usd) AS total_amount
    FROM yellevate_invoices
    )
SELECT dispute_lost, 
    ROUND((SUM(yellevate_invoices.invoice_amount_usd) 
    /
    total.total_amount) *100,2) AS percentage_lost
FROM yellevate_invoices, total
WHERE dispute_lost = 1
GROUP BY dispute_lost, total.total_amount;




--country where there is highest loss of income
SELECT country, dispute_lost, SUM(invoice_amount_usd) AS loss_of_revenue
FROM yellevate_invoices
WHERE disputed = 1 and dispute_lost = 1
GROUP BY country, dispute_lost
ORDER BY loss_of_revenue DESC
LIMIT 1;

