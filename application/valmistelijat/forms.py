from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ValmistelijaForm(FlaskForm):
    name = StringField("Valmistelijan nimi", [validators.Length(min=3)])
    titteli = StringField("Titteli", [validators.Length(min=3)])
    puh = StringField("Puhelinnumero", [validators.Length(min=3)])
    email = StringField("Sähköposti", [validators.Length(min=3)])

 
    class Meta:
        csrf = False
