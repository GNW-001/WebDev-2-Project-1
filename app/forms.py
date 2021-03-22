from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import  DataRequired

class PropForm(FlaskForm):
    title = TextField('Title', validators=[DataRequired()])
    numBedroom = TextField('No. of Bedrooms', validators=[DataRequired()])
    numBathroom = TextField('No. of Bathroom', validators=[DataRequired()])
    location = TextField('Location', validators=[DataRequired()])
    price = TextField('Price', validators=[DataRequired()])
    type = SelectField('Type', choices = [('h', 'House'), ('a','Apartment')])
    propImage = FileField('Image', validators=[FileRequired(), FileAllowed(['png', 'jpg', 'Images only!'])])
    submit = SubmitField('Send')