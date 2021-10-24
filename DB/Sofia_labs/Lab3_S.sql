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


INSERT INTO Rooms(type, Area, Unit) VALUES
('Library',22,5),
('Lab',31,1),
('Audience',43,1),
('Lab',24,4),
('Audience',55,6),
('Lab',41,7),
('Lab',29,10),
('Lab',31,9),
('Security',8,8),
('Audience',70,3);
