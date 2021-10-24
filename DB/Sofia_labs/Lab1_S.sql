USE MASTER
DROP DATABASE Control
GO

CREATE DATABASE Control
GO

USE CONTROL

CREATE TABLE Units(
    ID INT IDENTITY PRIMARY KEY,
    Name VARCHAR(30) NOT NULL,
    Unit_type VARCHAR(20) NOT NULL
);

CREATE TABLE Rooms (
    Room_ID INT IDENTITY PRIMARY KEY,
    type VARCHAR(15) NOT NULL,
    Area INT,
    Seats INT,
    Unit INT FOREIGN KEY REFERENCES Units(ID)
);
