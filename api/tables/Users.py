from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    firstName = Column(String(30))
    lastName = Column(String(30))
    emailAddress = Column(String(30), primary_key=True)
    cellPhone = Column(String(10))
    hoursPerMonth = Column(Integer)
    address = Column(String(256))
    password = Column(String(30))

    # Converts the User object to a dictionary
    def asDict(self) -> dict:
        userDict = {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "emailAddress": self.emailAddress,
            "cellPhone": self.cellPhone,
            "hoursPerMonth": self.hoursPerMonth,
            "address": self.address,
            "password": self.password
        }
        return userDict
