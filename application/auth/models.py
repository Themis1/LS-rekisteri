from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    vnat = db.relationship("Vna", backref='account', lazy=True)
    mmmat = db.relationship("Mmma", backref='account', lazy=True)

    def __init__(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def find_users_with_no_vnas(done=0):
        stmt = text("SELECT Account.id, Account.name FROM Account"
                    " LEFT JOIN Vna ON Vna.account_id = Account.id"
                    " LEFT JOIN Mmma ON Mmma.account_id = Account.id"
                    " WHERE ((Vna.done IS null OR Vna.done = :done) AND (Mmma.done IS null OR Mmma.done = :done))"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Vna.id) = 0").params(done=done)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
