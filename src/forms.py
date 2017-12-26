from wtforms.fields import PasswordField, StringField
from wtforms.validators import Email, Length
from wtforms.form import Form


class LoginForm(Form):

    username = StringField(validators=[Length(min=4)])
    password = PasswordField(validators=[Length(min=4)])
