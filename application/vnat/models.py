from application import db
from sqlalchemy.sql import text
from application.models import Base

class Vna(Base):
    __tablename__ = "vnat"
    name = db.Column(db.String(300), nullable=False)
    kuvaus = db.Column(db.String(300), nullable=False)
    valmistelija_id = db.Column(db.Integer, db.ForeignKey("valmistelija.id"), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    valmistelijat = db.relationship("Valmistelija", backref="vnat", lazy = True)

    @staticmethod
    def create_default_valmistelija(account_id):
        defaultValmistelijat = ["Osastopäällikkö", "Yksikköpäällikkö"]

        for cat in defaultValmistelijat:
            c = Valmistelija()
            c.account_id = account_id
            c.name = cat
            db.session().add(c)
            db.session().commit()

    def __init__(self, name, kuvaus, valmistelija_id):
        self.name = name
        self.kuvaus = kuvaus
        self.valmistelija_id = valmistelija_id
