from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    vnat = db.relationship("VNa", backref='account', lazy=True)

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
    def find_users_with_no_vnas():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                    " LEFT JOIN VNa ON VNa.account_id = Account.id"
                    " WHERE (VNa.done IS null OR VNa.done = 1)"
                    " GROUP BY Account.id"
                    " HAVING COUNT(VNa.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
