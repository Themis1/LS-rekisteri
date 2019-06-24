from application import db
from application.models import Base

class Mmma(Base):
    name = db.Column(db.String(144), nullable=False)
    kuvaus = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)


    def __init__(self, name, kuvaus):
        self.name = name
        self.kuvaus = kuvaus

