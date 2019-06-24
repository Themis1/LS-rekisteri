from flask_wtf import FlaskForm
from wtforms import StringField, validators

class MmmaForm(FlaskForm):
    name = StringField("Maa- ja metsätalousministeriön asetuksen nimi", [validators.Length(min=2)])
    kuvaus = StringField("Kuvaus")
 
    class Meta:
        csrf = False




