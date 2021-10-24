USE [Control]
GO

INSERT INTO Units(Name, Unit_type) VALUES
('IS','Department'),
('MMDA','Department'),
('AFNM', 'Department'),
('STIS','Department'),
('Library', 'Library');

INSERT INTO Rooms(type, Area, Unit) VALUES
('Library',22,5),
('Lab',31,1),
('Audience',43,1),
('Lab',24,3),
('Audience',42,2);
