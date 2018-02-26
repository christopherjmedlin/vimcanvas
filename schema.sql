drop table if exists canvases;
drop table if exists users;

create table canvases (
  canvas_id int primary key not null auto_increment,
  title text not null,
  active boolean not null,
  file_url text not null
);
create table users (
  user_id int primary key not null auto_increment,
  username text not null,
  password text not null,
  is_admin boolean not null
);