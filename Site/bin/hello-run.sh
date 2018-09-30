#!/bin/bash
#
# Sanity check to test that we can render the base template
#
export FLASK_DEBUG=1
export FLASK_APP=hello.py

cd .. && python3 -m flask run
