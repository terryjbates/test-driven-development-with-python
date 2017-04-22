# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import Form
from wtforms import PasswordField, StringField, SubmitField, validators
from wtforms.validators import DataRequired

from myflaskapp.user.models import User


class LoginForm(Form):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = User.query.filter_by(username=self.username.data).first()
        if not self.user:
            self.username.errors.append('Unknown username')
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        if not self.user.active:
            self.username.errors.append('User not activated')
            return False
        return True


class ToDoListForm(Form):
    """To-Do List form."""

    name = StringField('Enter a to-do item',
                     [validators.required(), validators.length(max=50)],
                     id='id_new_item')
    submit = SubmitField('Add item')

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(ToDoListForm, self).__init__(*args, **kwargs)
        self.user = None
