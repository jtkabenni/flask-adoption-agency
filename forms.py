from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, StringField, SelectField
from wtforms.validators import InputRequired, Optional, Email, NumberRange, URL


class AddPetForm(FlaskForm):
  name = StringField("Pet Name", validators =[InputRequired(message = "Pet name can't be blank")])
  species = SelectField("Species", choices=[('cat', 'cat'),  ('dog', 'dog'),  ('porcupine', 'porcupine')])
  image_url = StringField("Image URL", validators=[Optional(),URL(message= "Enter a valid url.")])
  age = FloatField("Age", validators=[Optional(), NumberRange(min=0, max=30, message = "Enter an age between 0 and 30")])
  notes = StringField("Notes")
  available = BooleanField("Available")
