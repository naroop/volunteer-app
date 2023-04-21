USE loginTest;
DROP TABLE IF EXISTS UserDetails;
DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
    EmailAddress VARCHAR(30) PRIMARY KEY,
    Password VARCHAR(72),
    Salt VARCHAR(30)
);
CREATE TABLE UserDetails (
    EmailAddress VARCHAR(30) PRIMARY KEY,
    FirstName VARCHAR(30),
    LastName VARCHAR(30),
    Cellphone VARCHAR(10),
    HoursPerMonth INT,
    Address VARCHAR(256),
    FOREIGN KEY (EmailAddress) REFERENCES Users(EmailAddress)
);
INSERT INTO Users(EmailAddress, Password, Salt)
VALUES(
        "sgoggins@mail.com",
        "$2b$04$yTg/XICu.Gk.Vd7VKBhKrOrY0ZvuZ7lFwHR4zs5Q6VV.tPuOSdan.",
        "$2b$04$yTg/XICu.Gk.Vd7VKBhKrO"
    );
INSERT INTO UserDetails(
        EmailAddress,
        FirstName,
        LastName,
        Cellphone,
        HoursPerMonth,
        Address
    )
VALUES(
        "sgoggins@mail.com",
        "Sean",
        "Goggins",
        "1010101010",
        50,
        "456 Providence Ave, Columbia MO, 65203"
    );