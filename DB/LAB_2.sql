USE Commercial
GO
----1
ALTER TABLE Student_Groups
ADD CONSTRAINT Course_MinMax CHECK(Course BETWEEN 1 AND 6)
GO
ALTER TABLE Student_Groups
ADD CONSTRAINT TermMinMax CHECK(Term BETWEEN 1 AND 2)

----2
ALTER TABLE Students
NOCHECK CONSTRAINT ALL

ALTER TABLE Students
ADD CONSTRAINT Group_FK FOREIGN KEY (Group_FK) REFERENCES Student_Groups(Student_Gr_ID) ON DELETE CASCADE;
GO

ALTER TABLE Student_Groups
NOCHECK CONSTRAINT ALL

ALTER TABLE Student_Groups
ADD CONSTRAINT Specialization_FK FOREIGN KEY (Specialization_FK) REFERENCES Specializations(Spec_ID) ON DELETE CASCADE;
GO

----3
ALTER TABLE Student_Groups
NOCHECK CONSTRAINT TermMinMax;


INSERT INTO Student_Groups(Name, Specialization_FK, Term) VALUES('FI-92',113,3);
GO
SELECT Name, Specialization_FK, Term FROM Student_Groups;

----INSERT INTO Students(Name,Surname, Group_FK, Birth) VALUES('Ivan','Tachyni',2, '10-02-2005');
ALTER TABLE Student_Groups WITH CHECK
CHECK CONSTRAINT TermMinMax;
GO
DELETE FROM Student_Groups WHERE Specialization_FK BETWEEN 0 AND 3;

----4
ALTER TABLE Student_Groups WITH CHECK
CHECK CONSTRAINT ALL

SELECT * FROM Student_Groups;

----5
ALTER TABLE Student_Groups
NOCHECK CONSTRAINT TermMinMax;

INSERT INTO Specializations(Name) VALUES ('AppliedMaths');
INSERT INTO Student_Groups(Name, Specialization_FK, Term) VALUES ('FI-92',1,3);

ALTER TABLE Student_Groups
CHECK CONSTRAINT TermMinMax;

----6
ALTER TABLE Students
ADD Single VARCHAR(3) NOT NULL;

ALTER TABLE Students
ADD CONSTRAINT Single DEFAULT 'yes' FOR Single

ALTER TABLE Students
DROP CONSTRAINT Single;

ALTER TABLE Students
DROP COLUMN  Single;

----7
EXEC SP_RENAME 'Student_Groups', 'Groups';

----8
EXEC SP_RENAME 'Groups', 'Student_Groups';	