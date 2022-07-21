from sqlalchemy import Column, Integer, String
from database import Base, session


class Pet(Base):
    __tablename__ = "Pet"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"{self.id}, {self.name}"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
