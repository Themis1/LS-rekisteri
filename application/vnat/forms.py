from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class VNaForm(FlaskForm):
    name = StringField("Valtioneuvoston asetuksen nimi", [validators.Length(min=2)])
    done = BooleanField("Annettu")
 
    class Meta:
        csrf = False
