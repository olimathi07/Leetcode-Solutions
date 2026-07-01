# Write your MySQL query statement below
DELETE FROM Person
WHERE Id NOT IN (
    SELECT MIN(Id)
        FROM (
                SELECT Id, Email
                        FROM Person
                            ) AS temp
                                GROUP BY Email
                                );