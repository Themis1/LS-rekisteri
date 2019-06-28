from application import db
from application.models import Base

class Vna(Base):
    name = db.Column(db.String(300), nullable=False)
    kuvaus = db.Column(db.String(300), nullable=False)
    valmistelija_id = db.Column(db.Integer. db.ForegnKey("valmistelija.id"), nullable=False, primary_key=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)


    def __init__(self, name, kuvaus, valmistelija_id):
        self.name = name
        self.kuvaus = kuvaus
        self.valmistelija_id = valmistelija_id
