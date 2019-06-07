from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class MmmaForm(FlaskForm):
    name = StringField("Maa- ja metsätalousministeriön asetuksen nimi", [validators.Length(min=2)])
    done = BooleanField("Annettu")
 
    class Meta:
        csrf = False




