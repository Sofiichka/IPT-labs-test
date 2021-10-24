USE [Commercial]
GO

INSERT INTO Specializations(Name, Cost) VALUES
('AppliedMaths',22500),
('Cybersecurity',31000),
('AppliedPhysics', 16800),
('Linguistics(English)', 18500),
('Linguistics(German)', 18500),
('Linguistics(French)', 18500),
('Journalistics', 37400),
('Physics', 28700),
('Arts', 42100),
('Economics', 37300);

INSERT INTO Student_Groups(Name, Specialization_FK, Course, Term) VALUES
('FI-92',1,3,1),
('FI-94',1,3,1),
('FI-02',10,2,1),
('FB-92',2,3,1),
('FF-11',3,1,1),
('FF-01',9,2,1),
('FI-93',1,3,1),
('FB-12',4,2,1),
('FA-12',8,1,1),
('FM-12',7,2,1);

INSERT INTO Students(Name, Surname, Sex, Group_FK, Birth, Billed_for_studying) VALUES
('Dmytro','Romanchenko','M', 1, '2002-07-19', 1),
('Sofia', 'Kozlovskaya', 'W', 1, '2002-04-13', 0),
('Egor', 'Panasuk', 'M', 2, '2001-05-22', 1),
('Anton', 'Yanushev', 'M', 1, '2002-08-16', 0),
('Dmytro', 'Zibarof', 'M', 4, '2002-01-01', 1),
('Ivan', 'Ponomarenko', 'M', 3, '2003-10-12', 1),
('Nikita', 'Shashenok', 'M', 6, '2001-11-21', 1),
('Alex', 'Oliynuk', 'M', 4, '2002-05-04', 0),
('Vlad', 'Vasiliev', 'M', 7, '2003-09-07', 1),
('Arsen', 'Alexin', 'M', 5, '2003-02-18', 0);