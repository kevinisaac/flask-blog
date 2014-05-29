from flask_wtf          import Form, RecaptchaField
from wtforms            import TextField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid      = TextField     ('OpenID',      validators  = [DataRequired()])
    #password   = PasswordField ('Password',    validators  = [DataRequired()])
    rememberme = BooleanField  ('Remember me', default     = True);

