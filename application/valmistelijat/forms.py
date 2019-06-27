from flask_wtf import FlaskForm
from wtforms import StringField, validators, HiddenField, SubmitField
from application.valmistelijat.models import Valmistelija

class ValmistelijaForm(FlaskForm):
    name = StringField("Valmistelijan nimi", [validators.DataRequired(message=("Nimi ei voi olla tyhjä")), validators.Length(min=3, max=30)])
    titteli = StringField("Titteli", [validators.DataRequired(message=("Titteli ei voi olla tyhjä")), validators.Length(min=3, max=30)])
    puh = StringField("Puhelinnumero", [validators.DataRequired(message=("Puhelinnumero ei voi olla tyhjä")), validators.Length(min=3, max=30)])
    email = StringField("Sähköposti", [validators.DataRequired(message=("Sähköposti ei voi olla tyhjä")), validators.Length(min=3, max=30)])

 
    class Meta:
        csrf = False

class EditValmistelijaForm(FlaskForm):
    name = StringField("Valmistelijan nimi", [
        validators.DataRequired(message=("Anna valmistelijan nimi")),
        validators.Length(min=3, max=30, message=("Valmistelijan nimessä on 3-30 merkkiä"))
    ])
    titteli = StringField("Titteli", [
        validators.Length(min=3, max=30, message=("Tittelissä on 3-30 merkkiä")),
        validators.DataRequired(message=("Anna valmistelijan titteli"))
    ])

    puh = StringField("Puhelinnumero", [
        validators.Length(min=3, max=30, message=("Puhelinnumerossa on 3-30 merkkiä")),
        validators.DataRequired(message=("Anna valmistelijan puhelinnumero"))
    ])

    email = StringField("Sähköpostiosoite", [
        validators.Length(min=3, max=30, message=("Sähköpostiosoitteessa on 3-30 merkkiä")),
        validators.DataRequired(message=("Anna valmistelijan sähköpostiosoite"))
    ])



    id = HiddenField("Valmistelijan ID", [
        validators.DataRequired(message=("ID puuttuu"))
    ])
    submit = SubmitField("Tallenna")

    def validate_name(self, name):
        name = Valmistelija.query.filter_by(name=name.data).first()

    def validate_titteli(self, titteli):
        titteli = Valmistelija.query.filter_by(titteli=titteli.data).first()

    def validate_puh(self, puh):
        puh = Valmistelija.query.filter_by(puh=puh.data).first()

    def validate_email(self, email):
        email = Valmistelija.query.filter_by(email=email.data).first()


    class Meta:
        csrf = False

