from flask import Flask
app = Flask(__name__)

from functools import wraps

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vnat.db"
    app.config["SQLALCHEMY_EHCO"] = True


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from os import urandom
app.config["SECRET_KEY"] = os.urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisaan, jos haluat jatkaa elamaa."

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            unauthorized  = False

            if role != "ANY":
                unauthorized = True

                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


from application import views

from application.vnat import models
from application.vnat import views

from application.auth import models
from application.auth import views

from application.mmmat import models
from application.mmmat import views

from application.valmistelijat import models
from application.valmistelijat import views


from sqlalchemy import event
from sqlalchemy.engine import Engine
from application.auth.models import Role, User
from application.valmistelijat.models import Valmistelija

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

@event.listens_for(Role.__table__, 'after_create')
def insert_initial_roles(*args, **kwargs):
    db.session.add(Role("ADMIN", True))
    db.session.add(Role("USER", False))
    db.session.commit()

@event.listens_for(User.__table__, 'after_create')
def insert_initial_superuser(*args, **kwargs):
    if os.environ.get("HEROKU"):
        super_user = User(
            os.environ.get("SU_NAME"),
            os.environ.get("SU_USERNAME"),
            os.environ.get("SU_PASSWD"),
            os.environ.get("SU_EMAIL"))
    else:
        super_user = User(
            "ADMIN",
            "admin",
            "admin",
            "admin@admin.com")
    db.session.add(super_user)
    db.session.commit()

@event.listens_for(Valmistelija.__table__, 'after_create')
def insert_initial_valmistelija(*args, **kwargs):
    valmistelija = Valmistelija(
            "ei tiedossa",
            "   ",
            "   ",
            "   ",
            "   ")
    db.session.add(valmistelija)
    db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
    # Set roles for default user with id = 1,
    # including ADMIN-role.gur
    su_user = User.query.get(1)
    su_user.set_default_role()
    su_role = Role.query.filter_by(superuser=True).first()
    if su_role.name not in su_user.get_roles():
        su_user.roles.append(su_role)
        db.session.commit()

except:
    pass
