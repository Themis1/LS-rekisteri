from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.vnat.models import Vna
from application.vnat.forms import VnaForm

@app.route("/vnat/", methods=["GET"])
def vnat_index():
    return render_template("vnat/list.html", vnat = Vna.query.all())

@app.route("/vnat/new/")
@login_required
def vnat_form():
    return render_template("vnat/new.html", form = VnaForm())



@app.route("/vnat/", methods=["POST"])
@login_required
def vnat_create():
    form = VnaForm(request.form)

    if not form.validate():
        return render_template("vnat/new.html", form = form)

    t = Vna(form.name.data)
    t.kuvaus = form.kuvaus.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
    
    return redirect(url_for("vnat_index"))

@app.route("/vnat/", methods=["GET"])
def vnat_yksi(vna_id):
    id = Vna.query.get(vna_id)
    return render_template("vnat/yksi.html", vnat_id = id)


@app.route("/vnat/", methods=["POST"])
def vnat_save():
    uusi = Vna(request.form.get("name"))
    uusi.kuvaus = Vna(request.form.get("kuvaus"))

    db.session().add(uusi)
    db.session().commit()

@app.route("/vnat/<vna_id>/", methods=["POST"])
@login_required
def delete_vna(vna_id):
    c = Vna.query.get(vna_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("vnat_index"))
