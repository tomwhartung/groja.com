""" Define the forms used by this app

Purpose: class that defines the form used on the Contact Me page
Author: Tom W. Hartung
Date: Winter, 2017
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
References:
    See the README.md file
    https://github.com/tomwhartung/always_learning_python/tree/master/13-flask_frankenforms_exp-4  # noqa
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import Optional, Required, Email


FOUR_LETTER_TYPES = [
    ('', ''),
    ('ENFJ', 'ENFJ'), ('ENFP', 'ENFP'),
    ('ENTJ', 'ENTJ'), ('ENTP', 'ENTP'),
    ('ESFJ', 'ESFJ'), ('ESFP', 'ESFP'),
    ('ESTJ', 'ESTJ'), ('ESTP', 'ESTP'),
    ('INFJ', 'INFJ'), ('INFP', 'INFP'),
    ('INTJ', 'INTJ'), ('INTP', 'INTP'),
    ('ISFJ', 'ISFJ'), ('ISFP', 'ISFP'),
    ('ISTJ', 'ISTJ'), ('ISTP', 'ISTP'),
]

NAME_MISSING_MSG = 'Please share your name or nickname with us'
EMAIL_MISSING_MSG = 'Please share your email address, so we can contact you'
EMAIL_INVALID_MSG = 'You must enter a valid email address'
ARCHETYPE_MISSING_MSG = 'Select a four-letter type from the drop-down list'
MESSAGE_MISSING_MSG = 'Please specify the type of help you need'


class SubscribeForm(FlaskForm):

    """ Form allowing the visitor to subscribe to the email newsletter """

    name = StringField('Name:', validators=[Required(NAME_MISSING_MSG)])
    email = StringField(
        'Email:',
        [Required(EMAIL_MISSING_MSG), Email(EMAIL_INVALID_MSG)]
    )
    submit = SubmitField('Submit Form')

    def reset(self):
        """ Reset the form """
        blankData = MultiDict([('csrf', self.reset_csrf())])
        self.process(blankData)


class FreeOfferForm(FlaskForm):

    """ Form to get the visitor's four-letter type and email address """

    archetype = SelectField(
        'Four-letter type',
        choices=FOUR_LETTER_TYPES,
        validators=[Required(ARCHETYPE_MISSING_MSG)] )
    email = StringField(
        'Email:',
        [Required(EMAIL_MISSING_MSG), Email(EMAIL_INVALID_MSG)]
    )
    submit = SubmitField('Submit Form')

    def reset(self):
        """ Reset the form """
        blankData = MultiDict([('csrf', self.reset_csrf())])
        self.process(blankData)


class GetYourPortraitForm(FlaskForm):

    """ Get the visitor's name, archetype, email, and optional message """

    name = StringField('Name:', validators=[Required(NAME_MISSING_MSG)])
    archetype = SelectField(
        'Four-letter type',
        choices=FOUR_LETTER_TYPES,
        validators=[Required(ARCHETYPE_MISSING_MSG)] )
    email = StringField(
        'Email:',
        [Required(EMAIL_MISSING_MSG), Email(EMAIL_INVALID_MSG)]
    )
    message = StringField(u'Text', widget=TextArea(), validators=[Optional()])
    submit = SubmitField('Submit Form')

    def reset(self):
        """ Reset the form """
        blankData = MultiDict([('csrf', self.reset_csrf())])
        self.process(blankData)


class NameEmailMessageForm(FlaskForm):

    """ Form to get the visitor's name, email address, and required message """

    name = StringField('Name:', validators=[Required(NAME_MISSING_MSG)])
    email = StringField(
        'Email:',
        [Required(EMAIL_MISSING_MSG), Email(EMAIL_INVALID_MSG)]
    )
    message = StringField(
        u'Text',
        widget=TextArea(),
        validators=[Required(MESSAGE_MISSING_MSG)]
    )
    submit = SubmitField('Submit Form')

    def reset(self):
        """ Reset the form """
        blankData = MultiDict([('csrf', self.reset_csrf())])
        self.process(blankData)
