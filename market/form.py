from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, user_name_to_check):
        user = User.query.filter_by(username=user_name_to_check.data).first()
        if user:
            raise ValidationError('Este usuario ya existe. Por favor prueba otro nombre')
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Este email ya existe. Por favor prueba otro email')

    username = StringField(label='user name:', validators=[Length(max=30), DataRequired()])
    email_address = StringField(label='email:',validators=[Email(), DataRequired()])
    password1 = PasswordField(label='password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='confirm password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='!crear cuenta!')

# Para el mail:
# = StringField("Email",  [InputRequired("Please enter your email address."), Email("This field requires a valid email address")])