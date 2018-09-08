from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Length

class GetAddressForm(FlaskForm):
    submit = SubmitField('Get New Address')
    address = StringField('Flo Address',validators=[DataRequired(), Length(min=2, max=200)])
    submit_pvt = SubmitField('Get Pvt Key')

class GetPvtForm(FlaskForm):
    submit = SubmitField('Get New Address')
    address = StringField('Insert Flo Address',validators=[DataRequired(), Length(min=2, max=200)])
    submit_pvt = SubmitField('Get Private Key')

class SignForm(FlaskForm):
    address = StringField('Enter the Flo Address',validators=[DataRequired(), Length(min=2, max=200)])
    message = StringField('Enter your message  ',validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Sign Message')

class VerifyForm(FlaskForm):
    address = StringField('Enter the Flo Address',validators=[DataRequired(), Length(min=2, max=200)])
    signature = StringField('Enter your signature  ',validators=[DataRequired(), Length(min=2, max=200)])
    message = StringField('Enter your message  ',validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Verify Message')
