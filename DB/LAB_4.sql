USE [Commercial]
GO

SELECT Name, Surname FROM Students WHERE (Billed_for_studying = 0)
GO

SELECT Student_Groups.Name, SUM(Cost) as SUM_DEBT 
FROM Student_Groups INNER JOIN Specializations on Specializations.Spec_ID = Student_Groups.Specialization_FK
GROUP BY Student_Groups.Name