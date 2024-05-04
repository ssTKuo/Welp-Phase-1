# Week 5 Tasks 2
```sql
create table member (
  id bigint primary key auto_incremeny,
  name varchar(255) not null,
  password varchar(255) not null,
  follow_count int unsigned not null default 0,
  time datetime not null default current_timestamp);
![Task 2_Create a new table named member]()
