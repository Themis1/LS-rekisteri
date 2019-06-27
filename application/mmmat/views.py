from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.mmmat.models import Mmma
from application.mmmat.forms import MmmaForm
from application.mmmat.forms import EditMmmaForm

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

    asetus = Mmma(form.name.data, form.kuvaus.data)
    asetus.account_id = current_user.id

    db.session().add(asetus)
    db.session().commit()
    
    return redirect(url_for("mmmat_index"))


@app.route("/mmmat/<mmma_id>/", methods=["GET"])
@login_required
def get_mmma(mmma_id):

    mmma = Mmma.query.get(mmma_id)
    form = MmmaForm(obj=mmma)

    return render_template("mmmat/yksi.html", mmma=Mmma.query.get(mmma_id), form=form)


@app.route("/mmmat/<mmma_id>/edit", methods=["GET","POST"])
@login_required
def edit_mmma(mmma_id):


    if request.method == "GET":
        form = EditMmmaForm(obj=Mmma.query.get(mmma_id))
        return render_template("mmmat/edit_mmma.html", mmma=Mmma.query.get(mmma_id), form = form)

    form = EditMmmaForm(request.form)

    if not form.validate():
        return render_template("mmmat/edit_mmma.html", mmma=Mmma.query.get(mmma_id), form=form)

    mmma = Mmma.query.get(mmma_id)

    mmma.id = form.id.data
    mmma.name = form.name.data
    mmma.kuvaus = form.kuvaus.data
    db.session().commit()

    return redirect(url_for("mmmat_index"))


@app.route("/mmmat/<mmma_id>/delete", methods=["POST"])
@login_required
def delete_mmma(mmma_id):

    c = Mmma.query.get(mmma_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("mmmat_index"))
