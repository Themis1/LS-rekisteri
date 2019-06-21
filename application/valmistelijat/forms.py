from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class ValmistelijaForm(FlaskForm):
    name = StringField("Valmistelijan nimi", [validators.Length(min=2)])
    done = BooleanField("Virassa")
 
    class Meta:
        csrf = False
