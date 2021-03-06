USE CONTROL
GO
----1
ALTER TABLE Rooms
ADD CONSTRAINT RoomAreaMin CHECK(Area > 0)
GO
ALTER TABLE Rooms
ADD CONSTRAINT SeatsMin CHECK(Seats > 0)

----2
ALTER TABLE Rooms
NOCHECK CONSTRAINT ALL

ALTER TABLE Rooms
ADD CONSTRAINT Unit FOREIGN KEY (Unit) REFERENCES Units(ID) ON DELETE CASCADE;
GO

----3
ALTER TABLE Rooms
NOCHECK CONSTRAINT RoomAreaMin;


INSERT INTO Rooms(type, Area, Seats) VALUES('Lab',0,-5);
GO
SELECT type, Area, Seats FROM Rooms;


ALTER TABLE Rooms WITH CHECK
CHECK CONSTRAINT RoomAreaMin;
GO
DELETE FROM Rooms WHERE Area = 0;

----4
ALTER TABLE Rooms WITH CHECK
CHECK CONSTRAINT ALL

SELECT * FROM Rooms;
GO
----5
ALTER TABLE Rooms
NOCHECK CONSTRAINT RoomAreaMin;

INSERT INTO Units(Name, Unit_type) VALUES ('MMDA','Faculty');
INSERT INTO Rooms(type, Area, Seats) VALUES ('Lab',15,-4);
GO
ALTER TABLE Rooms
CHECK CONSTRAINT RoomAreaMin;
GO

----6
ALTER TABLE Rooms
ADD Single VARCHAR(3) NOT NULL;

ALTER TABLE Rooms
ADD CONSTRAINT Single DEFAULT 'yes' FOR Single

ALTER TABLE Rooms
DROP CONSTRAINT Single;

ALTER TABLE Rooms
DROP COLUMN  Single;

----7
EXEC SP_RENAME 'Rooms', 'Rooms_11k';

----8
EXEC SP_RENAME 'Rooms_11k', 'Rooms';	