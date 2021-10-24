USE MASTER
DROP DATABASE Commercial
GO

CREATE DATABASE Commercial
GO

USE Commercial
GO

CREATE TABLE Specializations(
    Spec_ID INT IDENTITY PRIMARY KEY,
    Name VARCHAR(35) NOT NULL,
    Cost money 
);
CREATE TABLE Student_Groups(
    Student_Gr_ID INT IDENTITY PRIMARY KEY ,
    Name NVARCHAR(5) NOT NULL,
    Specialization_FK INT FOREIGN KEY REFERENCES Specializations(Spec_ID),
    Course INT,
    Term INT
);

CREATE TABLE Students(
    ID INT IDENTITY PRIMARY KEY,
    Name  NVARCHAR(15) NOT NULL,
    Surname VARCHAR(35) NOT NULL,
    Middlename VARCHAR(25),
    Sex CHAR(1),
    Group_FK INT FOREIGN KEY REFERENCES Student_Groups(Student_Gr_ID),
    Birth DATE NOT NULL,
    Billed_for_studying BIT
);

