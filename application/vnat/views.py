from flask import render_template, request, redirect, url_for

from application import app, db
from application.vnat.models import VNa

@app.route("/vnat/", methods=["GET"])
def vnat_index():
    return render_template("vnat/list.html", vnat = VNa.query.all())



@app.route("/vnat/new/")
def vnat_form():
    return render_template("vnat/new.html")


@app.route("/vnat/", methods=["POST"])
def vnat_create():
    t = VNa(request.form.get("name"))

    db.session().add(t)
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
