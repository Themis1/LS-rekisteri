from application import db
from application.models import Base

class Valmistelija(Base):
    name = db.Column(db.String(32), nullable=False)
    titteli = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), nullable=False)
    puh = db.Column(db.String(32), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)


    def __init__(self, name, titteli, email, puh):
        self.name = name
        self.titteli = titteli
        self.email = email
        self.puh = puh
