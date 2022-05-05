from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class LinkForm(FlaskForm):
    link_example = StringField('link_example',
                               validators=[DataRequired()])