BEGIN IF NOT EXISTS
  (SELECT *
   FROM Services
   WHERE Name = "Service1"
     AND Verified = 1) BEGIN
INSERT INTO Services (Name, Verified)
VALUES ("Service1",
        1) END END BEGIN IF NOT EXISTS
  (SELECT *
   FROM Services
   WHERE Name = "Service2"
     AND Verified = 1) BEGIN
INSERT INTO Services (Name, Verified)
VALUES ("Service2",
        1) END END BEGIN IF NOT EXISTS
  (SELECT *
   FROM Services
   WHERE Name = "Service3"
     AND Verified = 1) BEGIN
INSERT INTO Services (Name, Verified)
VALUES ("Service3",
        1) END END