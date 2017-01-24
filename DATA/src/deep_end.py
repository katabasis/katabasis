#!/usr/bin/env python3

import json
import psycopg2

from flask import (
                Flask,
                jsonify,
                make_response,
                request,
                )
from psycopg2.extras import RealDictCursor

deep = Flask(__name__)

connection = psycopg2.connect('dbname=master')
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor(cursor_factory=RealDictCursor)

# Routes

@deep.route('/market/open', methods=["GET"])
def get_open():
    symbol = request.args.get('symbol')
    __from = request.args.get('from', None)
    __to = request.args.get('to', None)
    if __from is None and __to is None:
        cursor.execute("""SELECT open FROM {}""".format(symbol))
        return json.dumps(cursor.fetchall(), indent=2)
    elif __from is None:
        cursor.execute("""SELECT open FROM {} WHERE time >= '{}'""".format(symbol, __from))
        return json.dumps(cursor.fetchall(), indent=2)
    elif __to is None:
        cursor.execute("""SELECT open FROM {} WHERE time < '{}'""".format(symbol, __to))
        return json.dumps(cursor.fetchall(), indent=2)
    else:
        cursor.execute("""SELECT open FROM {} WHERE time >= '{}' AND time < '{}'""".format(symbol, __to, __from))
        return json.dumps(cursor.fetchall(), indent=2)

@deep.route('/market/high', methods=["GET"])
def get_high():
    symbol = request.args.get('symbol')
    __from = request.args.get('from', None)
    __to = request.args.get('to', None)
    if __from is None and __to is None:
        cursor.execute("""SELECT high FROM {}""".format(symbol))
        return json.dumps(cursor.fetchall(), indent=2)
    elif __from is None:
        cursor.execute("""SELECT high FROM {} WHERE time >= '{}'""".format(symbol, __from))
        return json.dumps(cursor.fetchall(), indent=2)
    elif __to is None:
        cursor.execute("""SELECT high FROM {} WHERE time < '{}'""".format(symbol, __to))
        return json.dumps(cursor.fetchall(), indent=2)
    else:
        cursor.execute("""SELECT high FROM {} WHERE time >= '{}' AND time < '{}'""".format(symbol, __to, __from))
        return json.dumps(cursor.fetchall(), indent=2)

@deep.route('/market/low', methods=["GET"])
def get_low():
    symbol = request.args.get('symbol')
    __from = request.args.get('from', None)
    __to = request.args.get('to', None)
    if __from is None and __to is None:
        cursor.execute("""SELECT low FROM {}""".format(symbol))
        return json.dumps(cursor.fetchall(), indent=2)
    elif __from is None:
        cursor.execute("""SELECT low FROM {} WHERE time >= '{}'""".format(symbol, __from))
        return json.dumps(cursor.fetchall(), indent=2)
    elif __to is None:
        cursor.execute("""SELECT low FROM {} WHERE time < '{}'""".format(symbol, __to))
        return json.dumps(cursor.fetchall(), indent=2)
    else:
        cursor.execute("""SELECT low FROM {} WHERE time >= '{}' AND time < '{}'""".format(symbol, __to, __from))
        return json.dumps(cursor.fetchall(), indent=2)

@deep.route('/market/close', methods=["GET"])
def get_close():
    symbol = request.args.get('symbol')
    __from = request.args.get('from', None)
    __to = request.args.get('to', None)
    if __from is None and __to is None:
        cursor.execute("""SELECT close FROM {}""".format(symbol))
        return json.dumps(cursor.fetchall(), indent=2)
    elif __from is None:
        cursor.execute("""SELECT close FROM {} WHERE time >= '{}'""".format(symbol, __from))
        return json.dumps(cursor.fetchall(), indent=2)
    elif __to is None:
        cursor.execute("""SELECT close FROM {} WHERE time < '{}'""".format(symbol, __to))
        return json.dumps(cursor.fetchall(), indent=2)
    else:
        cursor.execute("""SELECT close FROM {} WHERE time >= '{}' AND time < '{}'""".format(symbol, __to, __from))
        return json.dumps(cursor.fetchall(), indent=2)

@deep.route('/market/volume', methods=["GET"])
def get_volume():
    symbol = request.args.get('symbol')
    __from = request.args.get('from', None)
    __to = request.args.get('to', None)
    if __from is None and __to is None:
        cursor.execute("""SELECT volume FROM {}""".format(symbol))
        return json.dumps(cursor.fetchall(), indent=2)
    elif __from is None:
        cursor.execute("""SELECT volume FROM {} WHERE time >= '{}'""".format(symbol, __from))
        return json.dumps(cursor.fetchall(), indent=2)
    elif __to is None:
        cursor.execute("""SELECT volume FROM {} WHERE time < '{}'""".format(symbol, __to))
        return json.dumps(cursor.fetchall(), indent=2)
    else:
        cursor.execute("""SELECT volume FROM {} WHERE time >= '{}' AND time < '{}'""".format(symbol, __to, __from))
        return json.dumps(cursor.fetchall(), indent=2)

# HTTP status codes

@deep.errorhandler(100)
def error_100(error):
    return make_response(jsonify({'error': "HTTP status code: 100"}), 100)

@deep.errorhandler(101)
def error_101(error):
    return make_response(jsonify({'error': "HTTP status code: 101"}), 101)

@deep.errorhandler(102)
def error_102(error):
    return make_response(jsonify({'error': "HTTP status code: 102"}), 102)

@deep.errorhandler(200)
def error_200(error):
    return make_response(jsonify({'error': "HTTP status code: 200"}), 200)

@deep.errorhandler(201)
def error_201(error):
    return make_response(jsonify({'error': "HTTP status code: 201"}), 201)

@deep.errorhandler(202)
def error_202(error):
    return make_response(jsonify({'error': "HTTP status code: 202"}), 202)

@deep.errorhandler(203)
def error_203(error):
    return make_response(jsonify({'error': "HTTP status code: 203"}), 203)

@deep.errorhandler(204)
def error_204(error):
    return make_response(jsonify({'error': "HTTP status code: 204"}), 204)

@deep.errorhandler(205)
def error_205(error):
    return make_response(jsonify({'error': "HTTP status code: 205"}), 205)

@deep.errorhandler(206)
def error_206(error):
    return make_response(jsonify({'error': "HTTP status code: 206"}), 206)

@deep.errorhandler(207)
def error_207(error):
    return make_response(jsonify({'error': "HTTP status code: 207"}), 207)

@deep.errorhandler(208)
def error_208(error):
    return make_response(jsonify({'error': "HTTP status code: 208"}), 208)

@deep.errorhandler(226)
def error_226(error):
    return make_response(jsonify({'error': "HTTP status code: 226"}), 226)

@deep.errorhandler(300)
def error_300(error):
    return make_response(jsonify({'error': "HTTP status code: 300"}), 300)

@deep.errorhandler(301)
def error_301(error):
    return make_response(jsonify({'error': "HTTP status code: 301"}), 301)

@deep.errorhandler(302)
def error_302(error):
    return make_response(jsonify({'error': "HTTP status code: 302"}), 302)

@deep.errorhandler(303)
def error_303(error):
    return make_response(jsonify({'error': "HTTP status code: 303"}), 303)

@deep.errorhandler(304)
def error_304(error):
    return make_response(jsonify({'error': "HTTP status code: 304"}), 304)

@deep.errorhandler(305)
def error_305(error):
    return make_response(jsonify({'error': "HTTP status code: 305"}), 305)

@deep.errorhandler(306)
def error_306(error):
    return make_response(jsonify({'error': "HTTP status code: 306"}), 306)

@deep.errorhandler(307)
def error_307(error):
    return make_response(jsonify({'error': "HTTP status code: 307"}), 307)

@deep.errorhandler(308)
def error_308(error):
    return make_response(jsonify({'error': "HTTP status code: 308"}), 308)

@deep.errorhandler(400)
def error_400(error):
    return make_response(jsonify({'error': "HTTP status code: 400"}), 400)

@deep.errorhandler(401)
def error_401(error):
    return make_response(jsonify({'error': "HTTP status code: 401"}), 401)

@deep.errorhandler(402)
def error_402(error):
    return make_response(jsonify({'error': "HTTP status code: 402"}), 402)

@deep.errorhandler(403)
def error_403(error):
    return make_response(jsonify({'error': "HTTP status code: 403"}), 403)

@deep.errorhandler(404)
def error_404(error):
    return make_response(jsonify({'error': "HTTP status code: 404"}), 404)

@deep.errorhandler(405)
def error_405(error):
    return make_response(jsonify({'error': "HTTP status code: 405"}), 405)

@deep.errorhandler(406)
def error_406(error):
    return make_response(jsonify({'error': "HTTP status code: 406"}), 406)

@deep.errorhandler(407)
def error_407(error):
    return make_response(jsonify({'error': "HTTP status code: 407"}), 407)

@deep.errorhandler(408)
def error_408(error):
    return make_response(jsonify({'error': "HTTP status code: 408"}), 408)

@deep.errorhandler(409)
def error_409(error):
    return make_response(jsonify({'error': "HTTP status code: 409"}), 409)

@deep.errorhandler(410)
def error_410(error):
    return make_response(jsonify({'error': "HTTP status code: 410"}), 410)

@deep.errorhandler(411)
def error_411(error):
    return make_response(jsonify({'error': "HTTP status code: 411"}), 411)

@deep.errorhandler(412)
def error_412(error):
    return make_response(jsonify({'error': "HTTP status code: 412"}), 412)

@deep.errorhandler(413)
def error_413(error):
    return make_response(jsonify({'error': "HTTP status code: 413"}), 413)

@deep.errorhandler(414)
def error_414(error):
    return make_response(jsonify({'error': "HTTP status code: 414"}), 414)

@deep.errorhandler(415)
def error_415(error):
    return make_response(jsonify({'error': "HTTP status code: 415"}), 415)

@deep.errorhandler(416)
def error_416(error):
    return make_response(jsonify({'error': "HTTP status code: 416"}), 416)

@deep.errorhandler(417)
def error_417(error):
    return make_response(jsonify({'error': "HTTP status code: 417"}), 417)

@deep.errorhandler(418)
def error_418(error):
    return make_response(jsonify({'error': "HTTP status code: 418"}), 418)

@deep.errorhandler(421)
def error_421(error):
    return make_response(jsonify({'error': "HTTP status code: 421"}), 421)

@deep.errorhandler(422)
def error_422(error):
    return make_response(jsonify({'error': "HTTP status code: 422"}), 422)

@deep.errorhandler(423)
def error_423(error):
    return make_response(jsonify({'error': "HTTP status code: 423"}), 423)

@deep.errorhandler(424)
def error_424(error):
    return make_response(jsonify({'error': "HTTP status code: 424"}), 424)

@deep.errorhandler(426)
def error_426(error):
    return make_response(jsonify({'error': "HTTP status code: 426"}), 426)

@deep.errorhandler(428)
def error_428(error):
    return make_response(jsonify({'error': "HTTP status code: 428"}), 428)

@deep.errorhandler(429)
def error_429(error):
    return make_response(jsonify({'error': "HTTP status code: 429"}), 429)

@deep.errorhandler(431)
def error_431(error):
    return make_response(jsonify({'error': "HTTP status code: 431"}), 431)

@deep.errorhandler(451)
def error_451(error):
    return make_response(jsonify({'error': "HTTP status code: 451"}), 451)

@deep.errorhandler(500)
def error_500(error):
    return make_response(jsonify({'error': "HTTP status code: 500"}), 500)

@deep.errorhandler(501)
def error_501(error):
    return make_response(jsonify({'error': "HTTP status code: 501"}), 501)

@deep.errorhandler(502)
def error_502(error):
    return make_response(jsonify({'error': "HTTP status code: 502"}), 502)

@deep.errorhandler(503)
def error_503(error):
    return make_response(jsonify({'error': "HTTP status code: 503"}), 503)

@deep.errorhandler(504)
def error_504(error):
    return make_response(jsonify({'error': "HTTP status code: 504"}), 504)

@deep.errorhandler(505)
def error_505(error):
    return make_response(jsonify({'error': "HTTP status code: 505"}), 505)

@deep.errorhandler(506)
def error_506(error):
    return make_response(jsonify({'error': "HTTP status code: 506"}), 506)

@deep.errorhandler(507)
def error_507(error):
    return make_response(jsonify({'error': "HTTP status code: 507"}), 507)

@deep.errorhandler(508)
def error_508(error):
    return make_response(jsonify({'error': "HTTP status code: 508"}), 508)

@deep.errorhandler(510)
def error_510(error):
    return make_response(jsonify({'error': "HTTP status code: 510"}), 510)

@deep.errorhandler(511)
def error_511(error):
    return make_response(jsonify({'error': "HTTP status code: 511"}), 511)

# HTTP status codes from Nginx

@deep.errorhandler(444)
def error_444(error):
    return make_response(jsonify({'error': "HTTP status code from Nginx: 444"}), 444)

@deep.errorhandler(495)
def error_495(error):
    return make_response(jsonify({'error': "HTTP status code from Nginx: 495"}), 495)

@deep.errorhandler(496)
def error_496(error):
    return make_response(jsonify({'error': "HTTP status code from Nginx: 496"}), 496)

@deep.errorhandler(497)
def error_497(error):
    return make_response(jsonify({'error': "HTTP status code from Nginx: 497"}), 497)

@deep.errorhandler(499)
def error_499(error):
    return make_response(jsonify({'error': "HTTP status code from Nginx: 499"}), 499)

if __name__ == "__main__":
    deep.run(host='0.0.0.0', port=<defined_api_port>)