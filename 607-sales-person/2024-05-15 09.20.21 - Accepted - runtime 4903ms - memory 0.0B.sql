# Write your MySQL query statement below
/* Write your T-SQL query statement below */
select name 
from SalesPerson  
where sales_id IN
    (
        select sales_id 
            from SalesPerson
            except 
                select s.sales_id 
                    from SalesPerson s
                        join Orders o
                            on s.sales_id =o.sales_id 
                                join company c
                                    on o.com_id= c.com_id
                                        where c.name='RED'
                                            )