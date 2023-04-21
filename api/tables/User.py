from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    emailAddress = Column(String(30), primary_key=True)
    password = Column(String(72))
    salt = Column(Integer)

    # Converts the User object to a dictionary
    def asDict(self) -> dict:
        userDict = {
            "emailAddres": self.emailAddress,
            "password": self.password,
            "salt": self.salt
        }
        return userDict
