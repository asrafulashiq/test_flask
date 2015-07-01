from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField("openid",validators=[DataRequired()])
    #submit = SubmitField("submit")
    pass

    
