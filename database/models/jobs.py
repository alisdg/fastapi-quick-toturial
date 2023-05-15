from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

from database.base_class import Base


class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    company = Column(String(40), nullable=False)
    company_url = Column(Text)
    location = Column(Text)
    description = Column(Text)
    date_posted = Column(Date)
    is_active = Column(Boolean(), default=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="jobs")
