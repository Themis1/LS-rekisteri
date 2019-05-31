from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.vnat.models import VNa
from application.vnat.forms import VNaForm

@app.route("/vnat/", methods=["GET"])
def vnat_index():
    return render_template("vnat/list.html", vnat = VNa.query.all())

@app.route("/vnat/new/")
@login_required
def vnat_form():
    return render_template("vnat/new.html", form = VNaForm())



@app.route("/vnat/", methods=["POST"])
@login_required
def vnat_create():
    form = VNaForm(request.form)

    if not form.validate():
        return render_template("vnat/new.html", form = form)

    t = VNa(form.name.data)
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
    
    return redirect(url_for("vnat_index"))

@app.route("/vnat/<vna_id>", methods=["POST"])
@login_required
def vnat_set_done(vna_id):

    t = VNa.query.get(vna_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("vnat_index"))


@app.route("/vnat/", methods=["GET"])
def vnat_yksi(vna_id):
    id = VNa.query.get(vna_id)
    return render_template("vnat/yksi.html", vnat_id = id)


@app.route("/vnat/", methods=["POST"])
def vnat_save():
    uusi = VNa(request.form.get("name"))

    db.session().add(uusi)
    db.session().commit()
