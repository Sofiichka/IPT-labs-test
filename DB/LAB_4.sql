USE [Commercial]
GO

SELECT Name, Surname FROM Students WHERE (Billed_for_studying = 0)
GO

SELECT SUM(Cost) as summirized_debt FROM Students, Student_Groups, Specializations 
    WHERE (Billed_for_studying = 0) AND Group_FK = Student_Gr_ID AND Specialization_FK = Spec_ID