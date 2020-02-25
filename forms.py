from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, StopValidation
from twitter import search_user


class ValidateId(object):
    """
    Validates that the user Twitters id exists. This validator will stop the
    validation chain on error.
    :param message:
        Error message to raise in case of a validation error.
    """
    field_flags = ('required', )

    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        if not search_user(field.data):
            if self.message is None:
                self.message = field.gettext('Wrong twitter user.')

            field.errors[:] = []
            raise StopValidation(self.message)


class UserIdForm(FlaskForm):
    username = StringField('User id', validators=[DataRequired(), ValidateId()])
    submit = SubmitField('Create map')
