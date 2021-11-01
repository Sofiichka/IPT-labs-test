USE [Control]
GO

INSERT INTO Units(Name, Unit_type) VALUES
('IS','Department'),
('MMDA','Department'),
('AFNM', 'Department'),
('STIS','Department'),
('FL', 'Facultie'),
('IPT', 'Facultie'),
('IASA', 'Institue'),
('Security', 'Security'),
('Library', 'Library'),
('Library', 'Library');


INSERT INTO Rooms(Room_Name,type, Area, Unit) VALUES
(1,'Library',22,5),
(2,'Lab',31,1),
(3,'Audience',43,1),
(5,'Lab',24,4),
(221,'Audience',55,6),
(6,'Lab',41,7),
(9,'Lab',29,10),
(10,'Lab',31,9),
(124,'Security',8,8),
(42,'Audience',70,3);
