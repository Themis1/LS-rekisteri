from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.valmistelijat.models import Valmistelija
from application.valmistelijat.forms import ValmistelijaForm

@app.route("/valmistelijat/", methods=["GET"])
def valmistelijat_index():
    return render_template("valmistelijat/list.html", valmistelijat = Valmistelija.query.all())

@app.route("/valmistelijat/new/")
@login_required
def valmistelijat_form():
    return render_template("valmistelijat/new.html", form = ValmistelijaForm())



@app.route("/valmistelijat/", methods=["POST"])
@login_required
def valmistelijat_create():
    form = ValmistelijaForm(request.form)

    if not form.validate():
        return render_template("valmistelijat/new.html", form = form)

    t = Valmistelija(form.name.data)
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
    
    return redirect(url_for("valmistelijat_index"))

@app.route("/valmistelijat/<valmistelija_id>", methods=["POST"])
@login_required
def valmistelijat_set_done(valmistelija_id):

    t = Valmistelija.query.get(valmistelija_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("valmistelijat_index"))


@app.route("/valmistelijat/", methods=["GET"])
def valmistelijat_yksi(valmistelija_id):
    id = Valmistelija.query.get(valmistelija_id)
    return render_template("valmistelijat/yksi.html", valmistelijat_id = id)


@app.route("/valmistelijat/", methods=["POST"])
def valmistelijat_save():
    uusi = Valmistelija(request.form.get("name"))

    db.session().add(uusi)
    db.session().commit()
