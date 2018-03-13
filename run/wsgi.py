#!/usr/bin/env python3

from application import omnibus

# TODO Replace the invocation an industrial strength application server
#
# The following parameters are specified for the explicit purpose of
# expediting the development process of this application. They are not
# suitable for production and should be changed before deployment.
#
omnibus.run(host='127.0.0.1', port=5000, debug=True)
