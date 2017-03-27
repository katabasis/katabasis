#!/usr/bin/env python3
# import requests

# # should probably be defining the get, _get, post, _post in a parent class
# # that inherits from object but that isn't time to test for that, right now

class Markit():

    def __init__(self):
    self.endpoint = "http://dev.markitondemand.com/MODApis/Api/v2/"

    def get(self, path, *args, **kwargs):
        return self._get(
            path,
            *args,
            **kwargs
            )

    def _get(self, path, *args, **kwargs):
        headers = kwargs["headers"] if type(kwargs.get("headers")) is dict else {}
        params = kwargs["params"] if type(kwargs.get("params")) is dict else {}
        return requests.get(
            self.endpoint+path,
            params=params,
            headers=headers
            )

    def lookup_endpoint(self, name):
        path = "{}/{}/{}".format("Lookup","json","?input=" + name)
        return self._get(
            path
            )

    def quote_endpoint(self, symbol):
        path = "{}/{}/{}".format("Quote","json","?symbol=" + symbol)
        return self._get(
            path
            )

# class Google():
# class Yahoo():
