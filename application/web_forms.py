from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField, StringField, IntegerField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, DataRequired, Email
from application.models import User



class RegistrationForm(FlaskForm):
    ''' registration form '''

    email = TextField('email',  validators=[InputRequired(message='email required'), Length(min=4, max=100, message='Email must be up to 4 and 25 character')])

    password = PasswordField('password',  validators=[InputRequired(message='password required')])

    confirm_pwd = PasswordField('confirm password',  validators=[InputRequired(message='confirm password required'), EqualTo('password', message='Passwords must match')])

    submit_button = SubmitField('Create')



class LoginForm(FlaskForm):

    '''login form'''

    email = StringField('email',  validators=[DataRequired(), Email()])

    password = PasswordField('password',  validators=[DataRequired()])

    submit_button = SubmitField('Log in')

class AdminForm(FlaskForm):

    '''admin signup'''
    email = StringField('email',  validators=[DataRequired(), Email()])

    password = PasswordField('password',  validators=[DataRequired()])

    submit_button = SubmitField('Create')

class GroupForm(FlaskForm):

    '''group signup'''
    group_name = StringField('group name', validators=[DataRequired()])
    group_no_of_members = IntegerField('number of members', validators=[DataRequired()])
    group_target = StringField('group target', validators=[DataRequired()])
    group_aggr_amount = IntegerField('aggregate amount', validators=[DataRequired()])
    submit_button = SubmitField('Create')
