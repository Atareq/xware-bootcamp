create database faculty_db

create table faculty {
    f_id int primary key not null,



}
create table student(stu_id int primary key ,f_name char ,l_name char ,f_phone char, l_phone char ,brith_date char);


create table faculty(f_id int primary key not null,f_name char not null);
create table depart(d_id int primary key not null , d_name char ,f_id int not null);
create table address(a_id int primary key not null,governorator char,city char , line_1 char not null, line_2 char );
create table student_address(stu_a_id int primary key not null,a_id int ,stu_id int );
create table student(stu_id int primary key ,f_name char ,l_name char ,f_phone char, l_phone char ,brith_date char);
create table course_table(c_id int primary key not null, sub_id int ,duration int ,p_id int);
create table subject(sub_id int primary key not null , sub_name char, sub_code int , f_id int );
