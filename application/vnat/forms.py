from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class VnaForm(FlaskForm):
    name = StringField("Valtioneuvoston asetuksen nimi", [validators.Length(min=2)])
    done = BooleanField("Annettu")
 
    class Meta:
        csrf = False
