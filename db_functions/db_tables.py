from sqlalchemy import (
    Column,
    Integer,
    String,
    ARRAY,
    JSON,
    ForeignKey,
    UniqueConstraint
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    profile_img = Column(String)
    
    cheeses = relationship(
        "cheese",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    
class cheese(Base):
    __tablename__ = "cheese"
    
    id= Column(Integer, primary_key=True)
    user_id= Column(ForeignKey("users.id"), nullable= False)
    name= Column(String)
    amount= Column(Integer)
    
    # one cheese type per user
    __table_args__ = (
        UniqueConstraint("user_id", "name", name="uq_user_cheese"),
    )
    
    user = relationship(
        "users",
        back_populates="cheeses"
    )
