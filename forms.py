from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Length

class GetAddressForm(FlaskForm):
    address = StringField('Flo Address',validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Get New Address')
    submit_pvt = SubmitField('Get Pvt Key')
