from flask import render_template, request, redirect, url_for

from application import app, db
from application.vnat.models import VNa

@app.route("/vnat/", methods=["GET"])
def vnat_index():
    return render_template("vnat/list.html", vnat = VNa.query.all())

@app.route("/vnat/new/")
def vnat_form():
    return render_template("vnat/new.html")


@app.route("/vnat/<vna_id>/", methods=["POST"])
def vnat_set_done(vna_id):

    t = VNa.query.get(vna_id)
    t.done = True
    db.session().commit()
    
    return redirect(url_for("vnat_index"))



@app.route("/vnat/", methods=["POST"])
def vnat_create():
    t = VNa(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
    
    return redirect(url_for("vnat_index"))
