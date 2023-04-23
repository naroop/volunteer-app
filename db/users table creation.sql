USE loginTest;
DROP TABLE IF EXISTS UserDetails;
DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
    emailAddress VARCHAR(30) PRIMARY KEY,
    password VARCHAR(72),
    salt VARCHAR(30)
);
CREATE TABLE UserDetails (
    firstName VARCHAR(30),
    lastName VARCHAR(30),
    emailAddress VARCHAR(30) PRIMARY KEY,
    cellPhone VARCHAR(10),
    hoursPerMonth INT,
    address VARCHAR(256),
    FOREIGN KEY (emailAddress) REFERENCES Users(emailAddress)
);
INSERT INTO Users(EmailAddress, Password, Salt)
VALUES(
        "sgoggins@mail.com",
        "$2b$04$yTg/XICu.Gk.Vd7VKBhKrOrY0ZvuZ7lFwHR4zs5Q6VV.tPuOSdan.",
        "$2b$04$yTg/XICu.Gk.Vd7VKBhKrO"
    );
INSERT INTO UserDetails(
        emailAddress,
        firstName,
        lastName,
        cellPhone,
        hoursPerMonth,
        address
    )
VALUES(
        "sgoggins@mail.com",
        "Sean",
        "Goggins",
        "1010101010",
        50,
        "456 Providence Ave, Columbia MO, 65203"
    );