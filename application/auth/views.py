from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import SignUpForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    print("Käyttäjä " + user.name + " tunnistettiin")
    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    

@app.route("/auth/signup", methods = ["GET", "POST"])
def auth_signup():
    if request.method == "GET":
        return render_template("auth/signup.html", form = SignUpForm())

    form = SignUpForm(request.form)

    if not form.validate():
        return render_template("auth/signup.html", form = SignUpForm())

    if (User.query.filter_by(username=form.username.data).first() != None):
        return render_template("auth/signup.html", form = form, error="Käyttäjätunnus varattu")

    # mahdolliset validoinnit
    t = User(form.name.data)
    t.username = form.username.data
    t.password = form.password.data

    db.session().add(t)
    db.session().commit()

    print("Rekisteröinti onnistui")
    return redirect(url_for("index"))
