from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import InputRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField(label='user name:', validators=[Length(max=30)])
    email_address = StringField(label='email:',validators=Email())
    
    password1 = PasswordField(label='password:', validators=Length(min=6))
    password2 = PasswordField(label='confirm password:', validators=EqualTo('password1'))
    submit = SubmitField(label='!crear cuenta!')

# Para el mail:
# = StringField("Email",  [InputRequired("Please enter your email address."), Email("This field requires a valid email address")])