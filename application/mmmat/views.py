from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.mmmat.models import Mmma
from application.mmmat.forms import MmmaForm

@app.route("/mmmat/", methods=["GET"])
def mmmat_index():
    return render_template("mmmat/list.html", mmmat = Mmma.query.all())

@app.route("/mmmat/new/")
@login_required
def mmmat_form():
    return render_template("mmmat/new.html", form = MmmaForm())



@app.route("/mmmat/", methods=["POST"])
@login_required
def mmmat_create():
    form = MmmaForm(request.form)

    if not form.validate():
        return render_template("mmmat/new.html", form = form)

    t = Mmma(form.name.data)
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
    
    return redirect(url_for("mmmat_index"))

@app.route("/mmmat/<mmma_id>", methods=["POST"])
@login_required
def mmmat_set_done(mmma_id):

    t = Mmma.query.get(mmma_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("mmmat_index"))


@app.route("/mmmat/", methods=["GET"])
def mmmat_yksi(mmma_id):
    id = Mmma.query.get(mmma_id)
    return render_template("mmmat/yksi.html", mmmat_id = id)


@app.route("/mmmat/", methods=["POST"])
def mmmat_save():
    uusi = Mmma(request.form.get("name"))

    db.session().add(uusi)
    db.session().commit()
