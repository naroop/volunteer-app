USE dev;
DROP TABLE IF EXISTS users;
CREATE TABLE users
(
    FirstName     VARCHAR(30),
    LastName      VARCHAR(30),
    EmailAddress  VARCHAR(30) PRIMARY KEY,
    Cellphone     VARCHAR(10),
    HoursPerMonth INT,
    Address       VARCHAR(256),
    Password      VARCHAR(30)
);