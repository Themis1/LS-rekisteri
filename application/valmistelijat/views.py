from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.valmistelijat.models import Valmistelija
from application.valmistelijat.forms import ValmistelijaForm
from application.valmistelijat.forms import EditValmistelijaForm

@app.route("/valmistelijat/", methods=["GET"])
def valmistelija_index():
    return render_template("valmistelijat/list.html", valmistelijat = Valmistelija.query.all())



@app.route("/valmistelijat/new/")
@login_required
def valmistelija_form():
    return render_template("valmistelijat/new.html", form = ValmistelijaForm())



@app.route("/valmistelijat/", methods=["POST"])
@login_required
def valmistelija_create():
    form = ValmistelijaForm(request.form)

    if not form.validate():
        return render_template("valmistelijat/new.html", form = form)

    uusi = Valmistelija(form.name.data, form.titteli.data, form.email.data, form.puh.data)
    uusi.account_id = current_user.id

    db.session().add(uusi)
    db.session().commit()
    
    return redirect(url_for("valmistelija_index"))

@app.route("/valmistelijat/<valmistelija_id>/", methods=["GET"])
@login_required
def get_valmistelija(valmistelija_id):
    valmistelija = Valmistelija.query.get(valmistelija_id)
    form = ValmistelijaForm(obj=valmistelija)
    return render_template("valmistelijat/valmistelija.html", valmistelija=Valmistelija.query.get(valmistelija_id), form=form)


@app.route("/valmistelijat/<valmistelija_id>/edit", methods=["GET","POST"])
def edit_valmistelija(valmistelija_id):

    if request.method == "GET":
        form = EditValmistelijaForm(obj=Valmistelija.query.get(valmistelija_id))
        return render_template("valmistelijat/edit_valmistelija.html", valmistelija=Valmistelija.query.get(valmistelija_id), form = form)
 
    form = EditValmistelijaForm(request.form)

    if not form.validate():
        return render_template("valmistelijat/edit_valmistelija.html", valmistelija=Valmistelija.query.get(valmistelija_id), form=form)

    valmistelija = Valmistelija.query.get(valmistelija_id)
    valmistelija.name = form.name.data
    valmistelija.email = form.email.data
    valmistelija.puh = form.puh.data


    db.session().commit()

    return redirect(url_for("valmistelija_index"))


@app.route("/valmistelijat/<valmistelija_id>/delete", methods=["POST"])
@login_required
def delete_valmistelija(valmistelija_id):

    c = Valmistelija.query.get(valmistelija_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("valmistelija_index"))

