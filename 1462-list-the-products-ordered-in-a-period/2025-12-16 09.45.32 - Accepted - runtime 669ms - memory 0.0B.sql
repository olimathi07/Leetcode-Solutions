select products.product_name,sum(orders.unit) as unit from products inner join orders 
on products.product_id=orders.product_id 
where month(order_date)=02 and year(order_date)=2020
group by products.product_name
having unit>=100;