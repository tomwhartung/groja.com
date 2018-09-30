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
from wtforms import StringField, SubmitField
from wtforms.validators import Optional, Required, Email


class NameEmailForm(FlaskForm):

    """ Define a form to get the visitor's name and email address """

    name = StringField('Name:', validators=[Optional()])
    email = StringField(
            'Email:',
            [Required("Share your email address so we can contact you."),
                Email("Please enter a valid email address.")]
    )
    submit = SubmitField('Get Your Portrait')

    def reset(self):
        """ Reset the form """
        blankData = MultiDict([('csrf', self.reset_csrf())])
        self.process(blankData)
