from application import db
from application.models import Base

class Vna(Base):
    name = db.Column(db.String(300), nullable=False)
    kuvaus = db.Column(db.String(300), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)


    def __init__(self, name, kuvaus):
        self.name = name
        self.kuvaus = kuvaus
