""" Module to send an email notification of interest

Purpose: send an email when someone fills out the Contact Me form
Author: Tom W. Hartung
Date: Winter, 2017
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
    https://docs.python.org/3/library/email-examples.html
"""

import smtplib
from email.mime.text import MIMEText

#
#  Set environment variables using values from /etc/apache2/envvars
#
import os
GROJA_MAIL_FROM = os.environ.get('GROJA_MAIL_FROM')
GROJA_MAIL_TO = os.environ.get('GROJA_MAIL_TO')


def send_interest_email(message_text):

    """ Send email, getting TO and FROM values from environment variables """

    # print('send_test_email(): message_text =', message_text)
    # print('GROJA_MAIL_FROM:', GROJA_MAIL_FROM)
    # print('GROJA_MAIL_TO:', GROJA_MAIL_TO)
    msg = MIMEText(message_text)
    msg['Subject'] = 'Indication of Interest on Groja.com'
    msg['From'] = GROJA_MAIL_FROM
    msg['To'] = GROJA_MAIL_TO
    server = smtplib.SMTP('localhost')
    server.send_message(msg)
    server.quit()
    # print('Message sent!')
    return True
