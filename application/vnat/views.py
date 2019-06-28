from flask import render_template, request, redirect, url_for
from flask_login import login_required, login_manager, current_user

from application import app, db
from application.vnat.models import Vna
from application.vnat.forms import VnaForm
from application.vnat.forms import EditVnaForm
from application.valmistelijat.models import Valmistelija

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
    valmistelijat = Valmistelija.query.all()
    form.valmistelija_id.choises = [(a.id, a.name) for a in users]

    if not form.validate():
        return render_template("vnat/new.html", form = form)

    asetus = Vna(form.name.data, form.kuvaus.data, form.valmistelija_id.data)
    asetus.account_id = current_user.id

    db.session().add(asetus)
    db.session().commit()

    return redirect(url_for("vnat_index"))


@app.route("/vnat/<vna_id>/", methods=["GET"])
@login_required
def get_vna(vna_id):
    vna = Vna.query.get(vna_id)
    form = VnaForm(obj=vna)
    return render_template("vnat/yksi.html", vna=Vna.query.get(vna_id), form=form)


@app.route("/vnat/<vna_id>/edit", methods=["GET","POST"])
@login_required
def edit_vna(vna_id):
    valmistelijat = Valmistelija.query.all()

    if request.method == "GET":
        form = EditVnaForm(obj=Vna.query.get(vna_id))
        return render_template("vnat/edit_vna.html", vna=Vna.query.get(vna_id), form = form)

    form = EditVnaForm(request.form)
    form.valmistelija_id.choises = [(a.id. a.name) for a in valmistelijat]

    if not form.validate():
        return render_template("vnat/edit_vna.html", vna=Vna.query.get(vna_id), form=form)

    vna = Vna.query.get(vna_id)

    vna.id = form.id.data
    vna.name = form.name.data
    vna.kuvaus = form.kuvaus.data
    vna.valmistelija_id = form.valmistelija_id.data
    db.session().commit()

    return redirect(url_for("vnat_index"))


@app.route("/vnat/<vna_id>/delete", methods=["POST"])
@login_required
def delete_vna(vna_id):
    c = Vna.query.get(vna_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("vnat_index"))
