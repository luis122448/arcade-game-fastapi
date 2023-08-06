from config.postgres import base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class VideoGameModel(base):

    __tablename__ = 'tbl_videogame'
    __table_args__ = {'schema':'arcade_game'}
    idgame = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(250))
    timelimit = Column(Integer)
    maxscore = Column(Integer)
    minscore = Column(Integer)
    maxranking = Column(Integer)