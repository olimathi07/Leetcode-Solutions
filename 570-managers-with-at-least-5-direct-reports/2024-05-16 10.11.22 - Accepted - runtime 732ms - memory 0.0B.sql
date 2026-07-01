# Write your MySQL query statement below
SELECT e.name
FROM Employee e
JOIN (
    SELECT managerId, COUNT(*) AS num_reports
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
) AS report_counts
ON e.id = report_counts.managerId
WHERE report_counts.num_reports >= 5;