from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, URL


# WTForm
class CafeForm(FlaskForm):
    name = StringField(
        'Cafe name',
        validators=[DataRequired()]
    )
    map_url = StringField(
        "Cafe Location on Google Maps (URL)",
        validators=[DataRequired(), URL()]
    )
    img_url = StringField(
        "Image URL",
        validators=[DataRequired(), URL()]
    )
    location = StringField(
        "City",
        validators=[DataRequired()]
    )
    has_sockets = BooleanField(
        # validators=[DataRequired()]
    )
    has_toilet = BooleanField(
        # validators=[DataRequired()]
    )
    has_wifi = BooleanField(
        # validators=[DataRequired()]
    )
    can_take_calls = BooleanField(
        # validators=[DataRequired()]
    )
    seats = IntegerField(
        validators=[DataRequired()]
    )
    coffee_price = FloatField(
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')