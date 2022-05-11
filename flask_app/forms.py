from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import (
    InputRequired,
    DataRequired,
    NumberRange,
    Length,
    Email,
    EqualTo,
    ValidationError,
)


from .models import User

class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=1, max=40)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError("Email is taken")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")


class UpdateUsernameForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    submit = SubmitField("Update Username")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.objects(username=username.data).first()
            if user is not None:
                raise ValidationError("That username is already taken")

class UpdateProfilePicForm(FlaskForm):
    picture = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Change Profile')

class NewThreadForm(FlaskForm):
    subject = TextAreaField(
        "Subject", validators=[InputRequired(), Length(min=5, max=100)]
    )
    content = TextAreaField(
        "Description", validators=[InputRequired(), Length(min=5, max=200)]
    )
    picture = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Create Thread")

class NewPostForm(FlaskForm):
    text = TextAreaField(
        "Comment", validators=[InputRequired(), Length(min=5, max=500)]
    )
    picture = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Submit post")

class ReportForm(FlaskForm):
    text = TextAreaField(
        "Reason", validators=[InputRequired(), Length(min=5, max=500)]
    )
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.objects(username=username.data).first()
            if user is None:
                raise ValidationError("That user does not exist")

    submit = SubmitField("Submit Report")