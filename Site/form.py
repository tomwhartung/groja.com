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


class SubscribeForm(FlaskForm):

    """ Form allowing the visitor to subscribe to the email newsletter """

    name = StringField('Name:', validators=[Optional()])
    email = StringField(
            'Email:',
            [Required("Share your email address so we can contact you."),
                Email("Please enter a valid email address.")]
    )
    submit = SubmitField('Submit Form')

    def reset(self):
        """ Reset the form """
        blankData = MultiDict([('csrf', self.reset_csrf())])
        self.process(blankData)


class FreeOfferForm(FlaskForm):

    """ Form to get the visitor's four-letter type and email address """

    four_letter_types = [
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

    missing_arch_msg = 'Select a four-letter type from the drop-down list'
    archetype = SelectField(
        'Four-letter type',
        choices=four_letter_types,
        validators = [Required(missing_arch_msg)] )
    email = StringField(
            'Email:',
            [Required("Share your email address so we can contact you."),
                Email("Please enter a valid email address.")]
    )
    submit = SubmitField('Submit Form')

    def reset(self):
        """ Reset the form """
        blankData = MultiDict([('csrf', self.reset_csrf())])
        self.process(blankData)


class NameEmailForm(FlaskForm):

    """ *** DEPRECATED *** """

    """ Define a form to get the visitor's name and email address """

    four_letter_types = [
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
    name = StringField('Name:', validators=[Optional()])
    archetype = SelectField(
        'Four-letter type',
        choices=four_letter_types,
        validators = [Required()] )
    email = StringField(
            'Email:',
            [Required("Share your email address so we can contact you."),
                Email("Please enter a valid email address.")]
    )
    message = StringField(u'Text', widget=TextArea(), validators=[Optional()])
    submit = SubmitField('Submit Form')

    def reset(self):
        """ Reset the form """
        blankData = MultiDict([('csrf', self.reset_csrf())])
        self.process(blankData)
