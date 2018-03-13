#!/usr/bin/env python3

import os

from flask import Flask, jsonify, request

from katabasis.models import omnibus as models
from katabasis.views  import omnibus as views


omnibus = Flask(__name__)
omnibus.register_blueprint(models)
omnibus.register_blueprint(views)


def keymaker(omnibus, filename='secret_key'):
    pathname = os.path.join(omnibus.instance_path, filename)
    try:
        omnibus.config['SECRET_KEY'] = open(pathname, "rb").read()
    except IOError:
        parent_directory = os.path.dirname(pathname)
        if not os.path.isdir(parent_directory):
            os.system('mkdir -p {0}'.format(parent_directory))
        os.system('head -c 24 /dev/urandom > {0}'.format(pathname))

keymaker(omnibus)


# Error handlers for HTTP responses in the 4XX error-space


@omnibus.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': "HTTP status code: 400"}), 400)


@omnibus.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({'error': "HTTP status code: 401"}), 401)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(402)
# def payment_required(error):
#     return make_response(jsonify({'error': "HTTP status code: 402"}), 402)


@omnibus.errorhandler(403)
def forbidden(error):
    return make_response(jsonify({'error': "HTTP status code: 403"}), 403)


@omnibus.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': "HTTP status code: 404"}), 404)


@omnibus.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({'error': "HTTP status code: 405"}), 405)


@omnibus.errorhandler(406)
def not_acceptable(error):
    return make_response(jsonify({'error': "HTTP status code: 406"}), 406)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(407)
# def proxy_authentication_required(error):
#     return make_response(jsonify({'error': "HTTP status code: 407"}), 407)


@omnibus.errorhandler(408)
def request_timeout(error):
    return make_response(jsonify({'error': "HTTP status code: 408"}), 408)


@omnibus.errorhandler(409)
def conflict(error):
    return make_response(jsonify({'error': "HTTP status code: 409"}), 409)


@omnibus.errorhandler(410)
def gone(error):
    return make_response(jsonify({'error': "HTTP status code: 410"}), 410)


@omnibus.errorhandler(411)
def length_required(error):
    return make_response(jsonify({'error': "HTTP status code: 411"}), 411)


@omnibus.errorhandler(412)
def precondition_failed(error):
    return make_response(jsonify({'error': "HTTP status code: 412"}), 412)


@omnibus.errorhandler(413)
def payload_too_large(error):
    return make_response(jsonify({'error': "HTTP status code: 413"}), 413)


@omnibus.errorhandler(414)
def uri_too_long(error):
    return make_response(jsonify({'error': "HTTP status code: 414"}), 414)


@omnibus.errorhandler(415)
def unsupported_media_types(error):
    return make_response(jsonify({'error': "HTTP status code: 415"}), 415)


@omnibus.errorhandler(416)
def range_not_satisfiable(error):
    return make_response(jsonify({'error': "HTTP status code: 416"}), 416)


@omnibus.errorhandler(417)
def expectation_failed(error):
    return make_response(jsonify({'error': "HTTP status code: 417"}), 417)


@omnibus.errorhandler(418)
def im_a_teapot(error):
    return make_response(jsonify({'error': "HTTP status code: 418"}), 418)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(421)
# def misdirected_request(error):
#     return make_response(jsonify({'error': "HTTP status code: 421"}), 421)


@omnibus.errorhandler(422)
def unprocessable_entity(error):
    return make_response(jsonify({'error': "HTTP status code: 422"}), 422)


@omnibus.errorhandler(423)
def locked(error):
    return make_response(jsonify({'error': "HTTP status code: 423"}), 423)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(424)
# def failed_dependency(error):
#     return make_response(jsonify({'error': "HTTP status code: 424"}), 424)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(426)
# def upgrade_required(error):
#     return make_response(jsonify({'error': "HTTP status code: 426"}), 426)


@omnibus.errorhandler(428)
def precondition_required(error):
    return make_response(jsonify({'error': "HTTP status code: 428"}), 428)


@omnibus.errorhandler(429)
def too_many_requests(error):
    return make_response(jsonify({'error': "HTTP status code: 429"}), 429)


@omnibus.errorhandler(431)
def request_header_fields_too_large(error):
    return make_response(jsonify({'error': "HTTP status code: 431"}), 431)


@omnibus.errorhandler(451)
def unavailable_for_legal_reasons(error):
    return make_response(jsonify({'error': "HTTP status code: 451"}), 451)


#  Error handlers for HTTP responses in an expansion of the 4XX error-space


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(444)
# def no_response(error):
#     return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 444"}), 444)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(495)
# def ssl_certificate_error(error):
#     return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 495"}), 495)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(496)
# def ssl_certificate_required(error):
#     return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 496"}), 496)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(497)
# def http_request_sent_to_https_port(error):
#     return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 497"}), 497)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(499)
# def client_closed_request(error):
#     return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 499"}), 499)


# Error handlers for HTTP responses in the 5XX error-space


@omnibus.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'error': "HTTP status code: 500"}), 500)


@omnibus.errorhandler(501)
def not_implemented(error):
    return make_response(jsonify({'error': "HTTP status code: 501"}), 501)


@omnibus.errorhandler(502)
def bad_gateway(error):
    return make_response(jsonify({'error': "HTTP status code: 502"}), 502)


@omnibus.errorhandler(503)
def service_unavailable(error):
    return make_response(jsonify({'error': "HTTP status code: 503"}), 503)


@omnibus.errorhandler(504)
def gateway_timeout(error):
    return make_response(jsonify({'error': "HTTP status code: 504"}), 504)


@omnibus.errorhandler(505)
def http_version_not_supported(error):
    return make_response(jsonify({'error': "HTTP status code: 505"}), 505)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(506)
# def variant_also_negotiates(error):
#     return make_response(jsonify({'error': "HTTP status code: 506"}), 506)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(507)
# def insufficient_storage(error):
#     return make_response(jsonify({'error': "HTTP status code: 507"}), 507)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(508)
# def loop_detected(error):
#     return make_response(jsonify({'error': "HTTP status code: 508"}), 508)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(510)
# def not_extended(error):
#     return make_response(jsonify({'error': "HTTP status code: 510"}), 510)


# FIXME Fix the following error handler
#
# @omnibus.errorhandler(511)
# def network_authentication_required(error):
#     return make_response(jsonify({'error': "HTTP status code: 511"}), 511)