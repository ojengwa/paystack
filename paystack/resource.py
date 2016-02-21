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
from client import RequestsClient
import error
import util
import version


class BaseAPIResource(object):

    def __init__(self, api_secret=None, resource_path=None, verify_ssl=False):
        self.protocol = 'https'
        self.api_host = self.protocol + '//api.paystack.co/'

        if not api_secret:
            raise error.ValidationError('You must provide your API SECRET_KEY \
                                        during object initialisation')

        if not resource_path:
            raise error.ValidationError('You must provide the API endpoint for\
                                         for the  resourcyou want to access.')
        self.api_secret = util.utf8(api_secret)
        self.resource_path = resource_path
        self.client = RequestsClient(verify_ssl_certs=verify_ssl)
        self.headers = {}
        self.headers.update({
            "Authorization": "Bearer {0}".format(self.api_secret),
            "Content-Type": "application/json",
            "user-agent": "PaystackSDK - {0}".format(version.VERSION)
        })

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


class CustomerResource(BaseAPIResource):
    pass


class TransactionResource(BaseAPIResource):

    def __init__(self, api_secret, reference,
                 resource_path='transaction', *args, **kwargs):
        super(TransactionResource, self)\
            .__init__(api_secret, resource_path, *args, **kwargs)
        self.reference = reference

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
        response = self.client.request(method, url, self.headers,
                                       post_data=payload)
        print(response)
        return response

    def verify(self, ref=None):
        endpoint = '/verify/'
        method = 'GET'


class PlanResource(BaseAPIResource):
    pass
