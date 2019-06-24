from flask_wtf import FlaskForm
from wtforms import StringField, validators

class VnaForm(FlaskForm):
    name = StringField("Valtioneuvoston asetuksen nimi", [validators.Length(min=2)])
    kuvaus = StringField("Kuvaus")
 
    class Meta:
        csrf = False
