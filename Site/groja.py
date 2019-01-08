""" groja.py: main application source for groja.com

Purpose: link routes to their corresponding templates
Author: Tom W. Hartung
Date: Winter, 2017
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  Chapter 3 of the "Flask Web Development" book (M. Grinberg, 2014)
"""

from groja_config import *
from flask import abort
from flask import Flask
from flask import redirect, render_template, request, session, url_for
from flask_bootstrap import Bootstrap
from db_access import update_or_insert_name_email
from send_email import send_interest_email

app = Flask(__name__)

#
# Load the configuration settings and Bootstrap the app
#
app.config.from_object('groja_config.Config')
Bootstrap(app)

# =============================================================================
#
# Routes and view functions
# -------------------------

@app.route('/')
@app.route('/home')
def home():
    """ Show the Home page """
    return render_template('home.html')


@app.route('/about')
def about():
    """ Show the About page """
    return render_template('about.html', aboutActive='active')


@app.route('/yourportrait')     # deprecated
@app.route('/your_portrait')    # preferred route - matches template name
def yourportrait():

    """
    Show the Your Portrait page
    """

    return render_template(
            'your_portrait.html',
            your_portraitActive='active'
    )


@app.route("/legal/<legal_page>")
def legal(legal_page):

    """ Display the requested legal page, defaulting to the terms_of_service """

    if legal_page == 'privacy_policy':
        template_name = 'legal/privacy_policy.html'
    elif legal_page == 'terms_of_service':
        template_name = 'legal/terms_of_service.html'
    elif legal_page == 'affiliate_marketing_disclosure':
        template_name = 'legal/affiliate_marketing_disclosure.html'
    elif legal_page == 'questionnaire_disclaimer':
        template_name = 'legal/questionnaire_disclaimer.html'
    else:
        template_name = 'legal/terms_of_service.html'

    return render_template(template_name, legalActive='active')


@app.route("/conversion/<interest>", methods=['GET', 'POST'])
def conversion(interest):

    """ Display and process conversion pages that contain a form """

    if interest == 'avmn':
        from form import SubscribeForm
        conv_form = SubscribeForm(request.form)
    elif interest == 'free_offer':
        from form import FreeOfferForm
        conv_form = FreeOfferForm(request.form)
    elif interest == 'get_your_portrait':
        from form import GetYourPortraitForm
        conv_form = GetYourPortraitForm(request.form)
    elif interest == 'seeourminds':
        from form import SubscribeForm
        conv_form = SubscribeForm(request.form)
    elif interest == 'joomoowebsites':
        from form import NameEmailMessageForm
        conv_form = NameEmailMessageForm(request.form)
    elif interest == 'tomwhartung':
        from form import NameEmailMessageForm
        conv_form = NameEmailMessageForm(request.form)
    else:
        abort(404)

    if request.method == 'POST':
        try:
            name = conv_form.name.data
        except AttributeError:
            name = ''
        try:
            archetype = conv_form.archetype.data
        except AttributeError:
            archetype = ''
        try:
            email = conv_form.email.data
        except AttributeError:
            email = ''
        try:
            message = conv_form.message.data
        except AttributeError:
            message = ''

        print("In conversion, name: ", name)
        print("In conversion, email: ", email)
        print("In conversion, archetype:", "'" + archetype + "'")
        print("In conversion, message:", "'" + message + "'")

        if conv_form.validate():
            # session variables are used in the thanks page function
            session['name'] = name
            session['archetype'] = archetype
            session['email'] = email
            session['message'] = message
            session['interest'] = interest
            if interest == 'avmn':
                update_or_insert_name_email(name, email, newsletter=1)
                thanks_page_url = url_for('thanks')
            elif interest == 'free_offer':
                update_or_insert_name_email(
                    name, email, newsletter=1, portrait=1)
                thanks_page_url = url_for('thanks')
            elif interest == 'get_your_portrait':
                update_or_insert_name_email(name, email, portrait=1)
                thanks_page_url = url_for('thanks')
            elif interest == 'seeourminds':
                update_or_insert_name_email(name, email, newsletter=1)
                thanks_page_url = url_for('thanks')
            elif interest == 'joomoowebsites':
                update_or_insert_name_email(name, email, consulting=1)
                thanks_page_url = url_for('thanks')
            elif interest == 'tomwhartung':
                update_or_insert_name_email(name, email, consulting=1)
                thanks_page_url = url_for('thanks')
            else:
                update_or_insert_name_email(name, email)
                thanks_page_url = url_for('home')
            return redirect(thanks_page_url)
    else:
        try:
            conv_form.name.data = ''
        except AttributeError:
            pass
        try:
            conv_form.email.data = ''
        except AttributeError:
            pass

    if interest == 'avmn':
        template_name = 'conversion/avmn.html'
    elif interest == 'free_offer':
        template_name = 'conversion/free_offer.html'
    elif interest == 'get_your_portrait':
        template_name = 'conversion/get_your_portrait.html'
    elif interest == 'seeourminds':
        template_name = 'conversion/seeourminds.html'
    elif interest == 'joomoowebsites':
        template_name = 'conversion/joomoowebsites.html'
    elif interest == 'tomwhartung':
        template_name = 'conversion/tomwhartung.html'
    else:
        abort(404)

    return render_template(template_name, conv_form=conv_form)


@app.route("/thanks")
@app.route("/thanks/<test_interest>")
def thanks(test_interest = ''):

    """
    Thank the visitor for sharing their email address
    Note:
       test_interest allows testing the templates without submitting a form
    """

    name = session.get('name')
    archetype = session.get('archetype')
    email = session.get('email')
    message = session.get('message')

    if test_interest:
        interest = test_interest
        name = 'Testing'
        email = 'testing@example.com'
        message = 'No form submitted - just testing'
    else:
        interest = session.get('interest')

    interest_text = ""
    if interest == 'avmn':
        template_name = 'thanks/avmn.html'
        interest_text = 'Receiving the Artsy Visions Monthly Newsletter (avmn)'
    elif interest == 'free_offer':
        template_name = 'thanks/free_offer.html'
        interest_text = 'Getting a free spiritual portrait'
    elif interest == 'get_your_portrait':
        template_name = 'thanks/get_your_portrait.html'
        interest_text = 'Buying a spiritual portrait'
    elif interest == 'seeourminds':
        template_name = 'thanks/seeourminds.html'
        interest_text = 'Receiving the Artsy Visions Monthly Newsletter (seeourminds)'
    elif interest == 'joomoowebsites':
        template_name = 'thanks/joomoowebsites.html'
        interest_text = 'Hiring me as a consultant'
    elif interest == 'tomwhartung':
        template_name = 'thanks/tomwhartung.html'
        interest_text = 'Hiring me as a consultant'
    else:
        abort(404)

    #print("In thanks, name: ", name, "email: ", email)
    #print("In thanks, interest:", "'" + interest + "'")
    #print("In thanks, message:", "'" + message + "'")
    #print("In thanks, test_interest:", "'" + test_interest + "'")
    #print("In thanks, interest_text:", "'" + interest_text + "'")

    interest_email = 'Conversion completed on groja.com!' + "\n\n" \
        + 'interest_text: "' + interest_text + "\"\n" \
        + 'name: "' + name  + "\"\n" \
        + 'email: "' + email + "\"\n" \
        + 'archetype: "' + archetype + "\"\n" \
        + "Message:\n\"" + message + "\"\n-- \n" \
        + 'Sent by method thanks() in program groja.py on website groja.com .'
    send_interest_email(interest_email)

    return render_template(template_name, name=name)


@app.route('/google203aca4a4dd53796.html')
def google203aca4a4dd53796():
    """ Show the Google Verification page for my meetups acct """
    return render_template('google/google203aca4a4dd53796.html')


@app.route('/google428ef5aab2bc0870.html')
def google428ef5aab2bc0870():
    """ Show the Google Verification page for my gmail acct """
    return render_template('google/google428ef5aab2bc0870.html')


@app.route('/index')
def index():
    """ Show the index.html template we are using to convert to MDB """
    return render_template('index.html')


@app.route('/v')
def versions():
    """ Show the versions.html template to see what versions we are using """

    import platform
    python_version = platform.python_version()
    import flask
    flask_version = flask.__version__

    template_name = 'versions.html'
    return render_template(
        template_name,
        python_version=python_version,
        flask_version=flask_version
    )


@app.errorhandler(404)
def page_not_found(e):

    """
    Handle 404 errors by showing the 404.html template
    Found this code here:
        http://flask.pocoo.org/docs/0.12/patterns/errorpages/
    """

    return render_template('404.html'), 404


# =============================================================================
#
# Run the app!
#
if __name__ == '__main__':
    app.run()
