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


INSERT INTO Rooms(Room_Name,type, Area, Unit, Seats) VALUES
(1,'Library',22,5, 20),
(2,'Lab',31,1,4),
(3,'Audience',43,1,16),
(5,'Lab',24,4,6),
(221,'Audience',55,6,30),
(6,'Lab',41,7,10),
(9,'Lab',29,10,4),
(10,'Lab',31,9,6),
(124,'Security',8,8,2),
(42,'Audience',70,3,70);
