from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from tables.User import User

Base = declarative_base()


class UserDetails(Base):
    __tablename__ = 'UserDetails'

    firstName = Column(String(30))
    lastName = Column(String(30))
    emailAddress = Column(String(30), ForeignKey(User.emailAddress), primary_key=True)
    cellPhone = Column(String(10))
    hoursPerMonth = Column(Integer)
    address = Column(String(256))

    # Converts the User object to a dictionary
    def asDict(self) -> dict:
        userDict = {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "emailAddress": self.emailAddress,
            "cellPhone": self.cellPhone,
            "hoursPerMonth": self.hoursPerMonth,
            "address": self.address,
        }
        return userDict
