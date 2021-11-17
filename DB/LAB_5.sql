USE [Commercial]
GO

SELECT Name, Cost FROM Specializations 
WHERE Cost > (SELECT AVG(Cost) FROM Specializations)
GO

--Выбор студентов, у которых возраст максимальный
SELECT Students.Name, Students.Surname, (YEAR(GETDATE()) - YEAR(Students.Birth)) AS Age 
FROM Students WHERE DATEPART(YEAR, Students.Birth) = (SELECT MIN(DATEPART(year, Birth)) FROM Students)
GO
--Выбор студентов, у которых возраст больше среднего и они принадлежат к группе ФИ-94, номер 2
SELECT Students.Name, Students.Surname, (YEAR(GETDATE()) - YEAR(Students.Birth)) AS Age FROM Students WHERE (YEAR(Students.Birth) < 
(SELECT AVG(YEAR(Birth)) FROM Students)) AND Students.Group_FK = '2'