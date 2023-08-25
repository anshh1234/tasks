show databases;
use sakila;
show tables;
-- data select
desc actor;
show columns from actor;
select * from actor;
select * from sakila.actor;
select ACTOR_id,first_name from actor;
-- only data item is case sensitive
desc actor_info;
select * from actor_info; -- projection is selecting a column

select actor_id,actor_id+5 from actor_info; -- projecting and working on data without original data being changed
-- selection is selecting a row
-- where clause for filtering data
select * from actor_info where actor_id=2;
select first_name from actor_info where actor_id<7;
select * from actor_info where first_name="nick";
-- DQL select statement
select database();
select * from language where language_id!=3; -- not equals to is != or <>
select * from language where name > 'I'; -- not case sensitive and uses character set (ascii )for comparison
select * from language where name > 'Iu';
select * from language where name > 'Italian';
select * from language where name > 'Italia';
select * from film;
-- like operator is used for pattern and % means 0 or more characters
select * from film where title like '%dinosaur'; -- dinosaur in end
select * from film where title like 'a%r'; -- start from a to r characters
select * from film where title like 'dinosaur%'; -- start from dinosaur
select * from film where title like '%dinosaur%'; -- gives any word in start and end but dinosaur in  middle 
select title,description,release_year from film where title like 'a%les'; 
select * from film where description like '%drama%';
select * from film where title like 'a_'; -- _ represents any blank character
select * from film where title like 'a__D%';
select title,film_id,description,release_year from film where title like '_c%';
select title,film_id,description,release_year from film where title like 'a%an';
select title,film_id,description,release_year from film where title like '%t___';
select title,film_id,description,release_year from film where title like '_f_i%egg';
select title,film_id,description,release_year from film where title like '__a__%';
