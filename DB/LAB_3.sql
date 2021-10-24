USE [Commercial]
GO

INSERT INTO Specializations(Name, Cost) VALUES
('AppliedMaths',22500), ('Cybersecurity',31000),('AppliedPhysics', 16800);

INSERT INTO Student_Groups(Name, Specialization_FK, Course, Term) VALUES
('FI-92',1,3,1),
('FI-94',1,3,1),
('FI-02',1,2,1),
('FB-92',2,3,1),
('FF-11',3,1,1),
('FF-01',3,2,1),
('FI-12',1,1,1)

INSERT INTO Students(Name, Surname, Sex, Group_FK, Birth, Billed_for_studying) VALUES
('Dmytro','Romanchenko','M', 1, '2002-07-19', 1),
('Sofia', 'Kozlovskaya', 'W', 1, '2002-04-13', 0),
('Egor', 'Panasuk', 'M', 2, '2001-05-22', 1),
('Anton', 'Yanushev', 'M', 1, '2002-08-16', 0),
('Dmytro', 'Zibarof', 'M', 4, '2002-01-01', 1),
('Maria', 'Cherednychenko', 'W', 3, '2003-10-12', 1)