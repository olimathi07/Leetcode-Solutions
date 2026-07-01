# Write your MySQL query statement below
SELECT us.product_id, 
       ROUND(SUM(pr.price * us.units) / SUM(us.units), 2) AS average_price
FROM UnitsSold us
JOIN Prices pr 
ON us.product_id = pr.product_id 
AND us.purchase_date BETWEEN pr.start_date AND pr.end_date
GROUP BY us.product_id;