create database students;

USE students;

CREATE TABLE Students (
    Name VARCHAR(100) NOT NULL,
    Age INT(3),
    Gender VARCHAR(10)
);


INSERT INTO students (Name, Age, Gender) VALUES 
("Brian Wanyonyi", "23", "M"),
("Winnie Wanjiku", "22", "F"),
("Claudia Jelagat", "22", "F"),
("Jacob Kipchumba", "24", "M"),
("Tony Buluma", "24", "M"),
("Kevin Ching", "67", "M");

SELECT *
FROM students
WHERE Age = "22";

SELECT *
FROM Students
WHERE Name LIKE '%Wan%';
