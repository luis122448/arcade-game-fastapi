from models.score_model import ScoreModel
from schemas.score_schema import ScoreSchema, ScoreSaveSchema
from typing import List

class ScoreService():

    def __init__(self, db):
        self.db = db

    def findAll(self, idgame: int):
        scores = self.db.query(ScoreModel).filter(ScoreModel.idgame == idgame).order_by(ScoreModel.ranking.asc()).all()
        return scores
    
    def findById(self,idgame: int, idscore: int):
        score = self.db.query(ScoreModel).filter(ScoreModel.idgame == idgame, ScoreModel.idscore == idscore).first()
        return score
    
    def create(self, data: ScoreSaveSchema):

        top_10_scores: List[ScoreModel] =  self.db.query(ScoreModel).filter(ScoreModel.idgame == data.idgame).order_by(ScoreModel.ranking.asc()).all()
        updateOk = 'N'
        newScore = None

        if len(top_10_scores) <= 10 or data.score > top_10_scores[-1].score:
            # Entra dentro del TOP10
            if len(top_10_scores) == 10:
                self.db.delete(top_10_scores[-1])

            for i in range(len(top_10_scores)-1):
                if data.score >= top_10_scores[0].score and updateOk == 'N':
                    new_ranking = 1
                    updateOk = 'Y'
                # print('Score : ' + str(data.score), 'Score T10 : ' + str(top_10_scores[i].score), 'Score T10 + 1 : ' + str(top_10_scores[i+1].score))
                if updateOk == 'Y':
                    tmpScore : ScoreModel = self.db.query(ScoreModel).filter(ScoreModel.idgame == top_10_scores[i].idgame, ScoreModel.idscore == top_10_scores[i].idscore).first()
                    tmpScore.ranking = top_10_scores[i].ranking + 1
                if data.score <= top_10_scores[i].score and data.score >= top_10_scores[i+1].score and updateOk == 'N':
                    # print('Insertar en la posicion: ', i+1)
                    new_ranking = i + 1
                    updateOk = 'Y'

            newScore = ScoreModel(
                idgame = data.idgame,
                idscore = 0,
                ranking = new_ranking,
                username = data.username,
                score = data.score,
                timetotal = data.timetotal,
                registdate = data.registdate
            )
            self.db.add(newScore)
            self.db.commit()
            return newScore

        else:
            return newScore  # No entra dentro del Ranking T10
        
    def update(self, idgame: int, idscore: int, data: ScoreSchema):
        score : ScoreModel = self.db.query(ScoreModel).filter(ScoreModel.idgame == idgame, ScoreModel.idscore == idscore).first()
        score.ranking = data.ranking
        self.db.commit()
        return score
    
    def delete(self, idgame: int, idscore: int):
        score : ScoreModel = self.db.query(ScoreModel).filter(ScoreModel.idgame == idgame, ScoreModel.idscore == idscore).first()
        self.db.delete(score)
        self.db.commit()
        return True