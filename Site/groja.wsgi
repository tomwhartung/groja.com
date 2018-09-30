""" Use WSGI to run groja.py

Purpose: insert the current directory into the system path and run the app
Author: Tom W. Hartung
Date: Winter, 2017
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
References:
  http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/
  http://www.jakowicz.com/flask-apache-wsgi/
  http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/#creating-a-wsgi-file
    "from yourapplication import app as application"
Usage:
  Reference this file in the apache config file.
  For details, see the references listed above.
"""

import sys
sys.path.insert(0, '/var/www/groja.com/htdocs/groja.com/Site')

#
# Note:
#   "noqa" lets PEP8 checkers know that we are doing something non-compliant
#   We need to use it here because the app won't run unless we set the path!
#
from groja import app as application   # noqa (see comment above)

