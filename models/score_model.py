from config.postgres import base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func

class ScoreModel(base):

    __tablename__ = 'tbl_score'
    __table_args__ = {'schema':'arcade_game'}
    idscore = Column(Integer, primary_key=True)
    idgame = Column(Integer, primary_key=True)
    ranking = Column(Integer)
    username = Column(String(50))
    score = Column(Integer)
    timetotal = Column(Integer)
    registdate = Column(DateTime, default=func.now())