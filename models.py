from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from database import Base, session


class Pet(Base):
    __tablename__ = "pet"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    # breed_name = relationship("Breed", backref="pet", cascade="all, delete-orphan", lazy="joined")
    breed_id = Column(String(50), ForeignKey("breed.id", ondelete="CASCADE"), nullable=False)

    def __str__(self):
        return f'{self.id}, {self.name}, {self.breed_name}'

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.breed_id}"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Breed(Base):
    __tablename__ = "breed"
    name = Column(String(50))
    id = Column(Integer, autoincrement=True, primary_key=True)
    pet = relationship("Pet", backref="breed", cascade="all, delete-orphan", lazy="joined")

    def __str__(self):
        return f'{self.id}, {self.name}'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
