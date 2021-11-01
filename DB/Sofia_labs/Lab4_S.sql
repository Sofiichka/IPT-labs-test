USE [Control]
GO

SELECT Room_Name, Units.Name FROM Units, Rooms WHERE Rooms.Unit = Units.ID GROUP BY  Units.Name, Room_Name;

SELECT SUM(Rooms.Area) Sum_area, [type] FROM Rooms GROUP BY  [type]

SELECT SUM(Rooms.Area) Sum_Area_on_University FROM Rooms 

SELECT SUM(Rooms.Seats) Sum_seats, Units.Name FROM Units, Rooms  WHERE Rooms.Unit = Units.ID GROUP BY Units.Name 