from application import db

class VNa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    number = db.Column(db.String(9), nullable=False)
    type = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, number, type):
        self.name = name
        self.number = number
        self.type = type
        self.done = false
