use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
select name from store;

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale;

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select s.store_id from store as s inner join sale as c on s.store_id = c.store_id group by store_id;

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select s.store_id from store as s left join sale as c on s.store_id = c.store_id WHERE c.store_id is NULL group by store_id;

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет. select p.name, avg(sum(s.total)/sum(s.quantity)) as 'avg(total/quantity)' from product as p join sale as s on p.product_id = s.product_id group by p.product_id;
select p.name, avg(s.total/s.quantity) as 'avg(total/quantity)' from product as p join sale as s on p.product_id = s.product_id group by p.product_id;

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select name from (select p.name from product as p join sale as s on p.product_id = s.product_id join store on s.store_id = store.store_id  group by p.name, store.store_id) as j group by name having count(*)=1;

-- 8. Получить названия всех складов, с которых продавался только один продукт
select * from store;

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select * from store;

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select * from store;
