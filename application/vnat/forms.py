from flask_wtf import FlaskForm
from wtforms import StringField, validators, HiddenField, SubmitField
from application.vnat.models import Vna

class VnaForm(FlaskForm):
    name = StringField("Valtioneuvoston asetuksen nimi", [validators.DataRequired(message=("Nimi ei voi olla tyhjä")), validators.Length(min=2, max=300)])
    kuvaus = StringField("Kuvaus", [validators.DataRequired(message=("Kuvaus ei voi olla tyhjä")), validators.Length(min=2, max=300)])
 
    class Meta:
        csrf = False

class EditVnaForm(FlaskForm):
    name = StringField("Asetuksen nimi", [
        validators.DataRequired(message=("Anna asetuksen nimi")),
        validators.Length(min=3, max=300, message=("Asetuksen nimessä on 3-300 merkkiä"))
    ])
    kuvaus = StringField("Kuvaus", [
        validators.Length(min=3, max=300, message=("Kuvauksessa on 3-300 merkkiä")),
        validators.DataRequired(message=("Anna asetukselle kuvaus"))
    ])
    id = HiddenField("Asetuksen ID", [
        validators.DataRequired(message=("ID puuttuu"))
    ])
    submit = SubmitField("Tallenna")

    def validate_name(self, name):
        name = Vna.query.filter_by(name=name.data).first()

    def validate_kuvaus(self, kuvaus):
        kuvaus = Vna.query.filter_by(kuvaus=kuvaus.data).first()

    class Meta:
        csrf = False


