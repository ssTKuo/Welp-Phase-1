# Tasks 2
```sql
create table member (
  id bigint primary key auto_incremeny,
  name varchar(255) not null,
  password varchar(255) not null,
  follow_count int unsigned not null default 0,
  time datetime not null default current_timestamp);
```
![Task 2_Create a new table named member](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%202_Create%20a%20new%20table%20named%20member.JPG?raw=true)

# Task 3
第一、二小題:  
INSERT a new row to the member table where name, username and password must
be set to test. INSERT additional 4 rows with arbitrary data.
```sql
insert into member (name, username, password) values ('test', 'test', 'test');
insert into member (name, username, password) values ('Kobe', 'Lakers', 'password20160413');
insert into member (name, username, password) values ('Timmy', 'Lakersfans', '19947788');
insert into member (name, username, password) values ('Anakin', 'thechosenone', 'blacksquadron');
insert into member (name, username, password) values ('Hamburglar', 'bigmac', 'LV-426');
select*from member;
+----+------------+--------------+------------------+----------------+---------------------+
| id | name       | username     | password         | follower_count | time                |
+----+------------+--------------+------------------+----------------+---------------------+
|  1 | test       | test         | test             |              0 | 2024-05-01 12:10:24 |
|  2 | Kobe       | Lakers       | password20160413 |              0 | 2024-05-01 13:43:16 |
|  3 | Timmy      | Lakersfans   | 19947788         |              0 | 2024-05-01 14:08:05 |
|  4 | Anakin     | thechosenone | blacksquadron    |              0 | 2024-05-01 14:08:05 |
|  5 | Hamburglar | bigmac       | LV-426           |              0 | 2024-05-01 14:08:12 |
```
![Task 3_1&2.JPG](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%203_1%262.JPG?raw=true)

第三小題:  
 SELECT all rows from the member table, in descending order of time.
```sql
SELECT * FROM member ORDER BY time DESC;
+----+------------+--------------+------------------+----------------+---------------------+
| id | name       | username     | password         | follower_count | time                |
+----+------------+--------------+------------------+----------------+---------------------+
|  5 | Hamburglar | bigmac       | LV-426           |              0 | 2024-05-01 14:08:12 |
|  3 | Timmy      | Lakersfans   | 19947788         |              0 | 2024-05-01 14:08:05 |
|  4 | Anakin     | thechosenone | blacksquadron    |              0 | 2024-05-01 14:08:05 |
|  2 | Kobe       | Lakers       | password20160413 |              0 | 2024-05-01 13:43:16 |
|  1 | test       | test         | test             |              0 | 2024-05-01 12:10:24 |
+----+------------+--------------+------------------+----------------+---------------------+
```
![Task 3_3](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%203_3.JPG?raw=true)

第四小題:   
SELECT total 3 rows, second to fourth, from the member table, in descending order
of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
```sql
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
+----+--------+--------------+------------------+----------------+---------------------+
| id | name   | username     | password         | follower_count | time                |
+----+--------+--------------+------------------+----------------+---------------------+
|  3 | Timmy  | Lakersfans   | 19947788         |              0 | 2024-05-01 14:08:05 |
|  4 | Anakin | thechosenone | blacksquadron    |              0 | 2024-05-01 14:08:05 |
|  2 | Kobe   | Lakers       | password20160413 |              0 | 2024-05-01 13:43:16 |
+----+--------+--------------+------------------+----------------+---------------------+
```
![Task 3_4](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%203_4.JPG?raw=true)

第五小題:   
SELECT rows where username equals to test.
```sql
 SELECT * FROM member WHERE username = 'test';
+----+------+----------+----------+----------------+---------------------+
| id | name | username | password | follower_count | time                |
+----+------+----------+----------+----------------+---------------------+
|  1 | test | test     | test     |              0 | 2024-05-01 12:10:24 |
+----+------+----------+----------+----------------+---------------------+
```
![Task 3_5](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%203_5.JPG?raw=true)

第六小題:   
 SELECT rows where name includes the es keyword.
```sql
SELECT * FROM member WHERE name LIKE '%es%';
+----+------+----------+----------+----------------+---------------------+
| id | name | username | password | follower_count | time                |
+----+------+----------+----------+----------------+---------------------+
|  1 | test | test     | test     |              0 | 2024-05-01 12:10:24 |
+----+------+----------+----------+----------------+---------------------+
```
![Task 3_6](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%203_6.JPG?raw=true)

第七小題:   
SELECT rows where both username and password equal to test.
```sql
SELECT * FROM member WHERE username = 'test' AND password = 'test';
+----+------+----------+----------+----------------+---------------------+
| id | name | username | password | follower_count | time                |
+----+------+----------+----------+----------------+---------------------+
|  1 | test | test     | test     |              0 | 2024-05-01 12:10:24 |
+----+------+----------+----------+----------------+---------------------+
```
![Task 3_7](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%203_7.JPG?raw=true)

第八小題:   
UPDATE data in name column to test2 where username equals to test.
```sql
UPDATE member SET name = 'test2' WHERE username = 'test';
+----+------------+--------------+------------------+----------------+---------------------+
| id | name       | username     | password         | follower_count | time                |
+----+------------+--------------+------------------+----------------+---------------------+
|  1 | test2      | test         | test             |              0 | 2024-05-01 12:10:24 |
|  2 | Kobe       | Lakers       | password20160413 |              0 | 2024-05-01 13:43:16 |
|  3 | Timmy      | Lakersfans   | 19947788         |              0 | 2024-05-01 14:08:05 |
|  4 | Anakin     | thechosenone | blacksquadron    |              0 | 2024-05-01 14:08:05 |
|  5 | Hamburglar | bigmac       | LV-426           |              0 | 2024-05-01 14:08:12 |
+----+------------+--------------+------------------+----------------+---------------------+
```
![Task 3_8](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%203_8.JPG?raw=true)

# Task 4
第一小題:   
SELECT how many rows from the member table.
```sql
select count(id) from member ;
+-----------+
| count(id) |
+-----------+
|         5 |
+-----------+
```
![Task 4_1](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%204_1.JPG?raw=true)

第二小題:   
SELECT the sum of follower_count of all the rows from the member table.
```sql
select SUM(follower_count) from member;
+---------------------+
| SUM(follower_count) |
+---------------------+
|                   0 |
+---------------------+
```
![Task 4_2](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%204_2.JPG?raw=true)

第三小題:   
SELECT the average of follower_count of all the rows from the member table.
```sql
select AVG(follower_count) from member;
+---------------------+
| AVG(follower_count) |
+---------------------+
|              0.0000 |
+---------------------+
```
![Task 4_3](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%204_3.JPG?raw=true)

第四小題:   
SELECT the average of follower_count of the first 2 rows, in descending order of
follower_count, from the member table.
```sql
select AVG(follower_count) AS AVG_follower_count
  from(
      select follower_count
      from member
      order by follower_count DESC
      limit 2
      ) as first_two_data;
+--------------------+
| AVG_follower_count |
+--------------------+
|             0.0000 |
+--------------------+
```
![Task 4_4](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%204_4.JPG?raw=true)


# Task5
第一小題:   
Create a new table named message, in the website database. designed as below:
```sql
CREATE TABLE message(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id BIGINT NOT NULL,
    content VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
INSERT INTO message (member_id, content, like_count) VALUES (1,' This is test',5);
INSERT INTO message (member_id, content, like_count) VALUES (2,'Lakers legendary players',824);
INSERT INTO message (member_id, content, like_count) VALUES (3,'I will definitely succeed',999);
INSERT INTO message (member_id, content, like_count) VALUES (4, 'You don''t know the power of the dark side', 789)
INSERT INTO message (member_id, content, like_count) VALUES (5,'I love BIGMAC',7);
select * from message;
+----+-----------+-------------------------------------------+------------+---------------------+
| id | member_id | content                                   | like_count | time                |
+----+-----------+-------------------------------------------+------------+---------------------+
|  1 |         1 | This is test                              |          5 | 2024-05-02 20:26:03 |
|  2 |         2 | Lakers legendary players                  |        824 | 2024-05-02 20:41:23 |
|  3 |         3 | I will definitely succeed                 |        999 | 2024-05-02 20:42:35 |
|  4 |         4 | You don't know the power of the dark side |        789 | 2024-05-02 20:55:37 |
|  5 |         5 | I love BIGMAC                             |          7 | 2024-05-02 21:04:10 |
+----+-----------+-------------------------------------------+------------+---------------------+
```
![Show Both Tables](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/showbothtables.JPG?raw=true)

第二小題:   
SELECT all messages, including sender names. We have to JOIN the member table
to get that.

```sql
SELECT message.content, member.name FROM message JOIN member ON message.member_id = member.id;
+-------------------------------------------+------------+
| content                                   | name       |
+-------------------------------------------+------------+
| This is test                              | test2      |
| Lakers legendary players                  | Kobe       |
| I will definitely succeed                 | Timmy      |
| You don't know the power of the dark side | Anakin     |
| I love BIGMAC                             | Hamburglar |
+-------------------------------------------+------------+
SELECT member.name, message.content FROM message JOIN member ON message.member_id = member.id;
+------------+-------------------------------------------+
| name       | content                                   |
+------------+-------------------------------------------+
| test2      | This is test                              |
| Kobe       | Lakers legendary players                  |
| Timmy      | I will definitely succeed                 |
| Anakin     | You don't know the power of the dark side |
| Hamburglar | I love BIGMAC                             |
+------------+-------------------------------------------+
SELECT * FROM message INNER JOIN member ON message.member_id = member.id;
+----+-----------+-------------------------------------------+------------+---------------------+----+------------+--------------+------------------+----------------+---------------------+
| id | member_id | content                                   | like_count | time                | id | name       | username     | password         | follower_count | time                |
+----+-----------+-------------------------------------------+------------+---------------------+----+------------+--------------+------------------+----------------+---------------------+
|  1 |         1 | This is test                              |          5 | 2024-05-02 20:26:03 |  1 | test2      | test         | test             |              0 | 2024-05-01 12:10:24 |
|  2 |         2 | Lakers legendary players                  |        824 | 2024-05-02 20:41:23 |  2 | Kobe       | Lakers       | password20160413 |              0 | 2024-05-01 13:43:16 |
|  3 |         3 | I will definitely succeed                 |        999 | 2024-05-02 20:42:35 |  3 | Timmy      | Lakersfans   | 19947788         |              0 | 2024-05-01 14:08:05 |
|  4 |         4 | You don't know the power of the dark side |        789 | 2024-05-02 20:55:37 |  4 | Anakin     | thechosenone | blacksquadron    |              0 | 2024-05-01 14:08:05 |
|  5 |         5 | I love BIGMAC                             |          7 | 2024-05-02 21:04:10 |  5 | Hamburglar | bigmac       | LV-426           |              0 | 2024-05-01 14:08:12 |
+----+-----------+-------------------------------------------+------------+---------------------+----+------------+--------------+------------------+----------------+---------------------+
```
![Task 5_2](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%205_2.JPG?raw=true)

第三小題:   
SELECT all messages, including sender names, where sender username equals to
test. We have to JOIN the member table to filter and get that.
```sql
SELECT member.name, message.content FROM message INNER JOIN member ON  message.member_id = member.id WHERE member.username = 'test';
+-------+--------------+
| name  | content      |
+-------+--------------+
| test2 | This is test |
+-------+--------------+
```
![Task 5_3](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/Task%205_3.JPG?raw=true)

第四、五小題:   
Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like
count of messages where sender username equals to test.

Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like
count of messages GROUP BY sender username.
```sql
select avg(message.like_count) from message inner join member on message.member_id = member.id where member.username = 'test';
+-------------------------+
| avg(message.like_count) |
+-------------------------+
|                  5.0000 |
+-------------------------+

 select member.username, AVG(message.like_count) as avg_likecount from message inner join member on message.member_id=member.id group by member.username;
+--------------+---------------+
| username     | avg_likecount |
+--------------+---------------+
| test         |        5.0000 |
| Lakers       |      824.0000 |
| Lakersfans   |      999.0000 |
| thechosenone |      789.0000 |
| bigmac       |        7.0000 |
+--------------+---------------+
```
![final](https://github.com/ssTKuo/Welp-Phase-1/blob/main/Week5/final.JPG?raw=true)















