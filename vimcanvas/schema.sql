drop table if exists canvases;
drop table if exists users;

create table canvases (
  id integer not null primary key autoincrement,
  title text not null,
  active boolean not null default false,
  file_url text not null
);
create table users (
    username text not null,
    password text not null,
    is_admin boolean not null default false
);