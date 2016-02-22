# -*- coding: utf-8 -*-
"""
Paystack API wrapper.

@author Bernard Ojengwa.

Copyright (c) 2015, Bernard Ojengwa
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OƒR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
from paystack.client import RequestsClient
from paystack import error
from paystack import util
from paystack import version


class BaseAPIResource(object):

    def __init__(self, api_secret=None, resource_path=None, verify_ssl=True):
        self.protocol = 'https'
        self.api_host = self.protocol + '://api.paystack.co/'

        if not api_secret:
            raise error.ValidationError('You must provide your API SECRET_KEY \
                                        during object initialisation')

        if not resource_path:
            raise error.ValidationError('You must provide the API endpoint for\
                                         for the resource you want to access.')
        self.api_secret = util.utf8(api_secret)
        self.resource_path = resource_path
        self.client = RequestsClient(verify_ssl_certs=verify_ssl)
        self.request_headers = {
            "Authorization": "Bearer {0}".format(self.api_secret),
            "Content-Type": "application/json",
            "user-agent": "PaystackSDK - {0}".format(version.VERSION)
        }

        self._result = {}
        self._status_code = None
        self._response_headers = {}

    def all(self):
        pass

    def one(self, id):
        pass

    def post(self, data):
        pass

    def delete(self, id):
        pass

    def update(self, id, data):
        pass

    @property
    def status(self):
        return self._status_code

    @property
    def response(self):
        return self._result

    @property
    def headers(self):
        self._response_headers


class CustomerResource(BaseAPIResource):
    pass


class TransactionResource(BaseAPIResource):

    def __init__(self, api_secret, reference,
                 resource_path='transaction', *args, **kwargs):
        super(TransactionResource, self)\
            .__init__(api_secret, resource_path, *args, **kwargs)
        self.reference = reference
        self.authorization_url = None
        self.access_code = None

    def initialize(self, amount, email, plan=None):
        endpoint = '/initialize'
        method = 'POST'
        payload = {
            "reference": self.reference,
            "amount": amount,
            "email": email,
            "plan": plan
        }
        url = self.api_host + self.resource_path + endpoint
        response, status, headers = self.client.request(method, url,
                                                        self.request_headers,
                                                        post_data=payload)
        self._response_headers = headers
        self._status_code = status
        self._result = response
        if not response.get('status', False):
            raise error.APIError(response.get('message'))

        self.authorization_url = response.get('authorization_url', None)
        self.access_code = response.get('access_code', None)

        return response

    def verify(self):
        endpoint = '/verify/'
        method = 'GET'
        url = self.api_host + self.resource_path + endpoint + self.reference
        response, status, headers = self.client.request(method, url,
                                                        self.request_headers
                                                        )
        self._response_headers = headers
        self._status_code = status
        self._result = response
        if not response.get('status', False):
            raise error.APIError(response.get('message'))

        self.authorization_url = response.get('authorization_url', None)
        self.access_code = response.get('access_code', None)

        return response

    def verify(self, ref=None):
        endpoint = '/verify/'
        method = 'GET'
        if not ref and not self.reference:
            raise error.ValidationError("You must define a reference key for\
                                         this transaction.")
        self.reference = (lambda ref: ref if ref else self.reference)(ref)
        url = self.api_host + self.resource_path + endpoint + self.reference
        response, status, headers = self.client.request(method, url,
                                                        self.request_headers
                                                        )
        self._response_headers = headers
        self._status_code = status
        self._result = response
        if not response.get('status', False):
            raise error.APIError(response.get('message'))

        self.authorization_url = response.get('authorization_url', None)
        self.access_code = response.get('access_code', None)

        return response


class PlanResource(BaseAPIResource):
    pass
