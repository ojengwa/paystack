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
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import webbrowser

from paystack.client import RequestsClient
from paystack import error
from paystack import util
from paystack import version


class BaseAPIResource(object):  # pragma no cover
    """
    Abstract resource class.

    Attributes:
        api_host (TYPE): Description
        api_secret (TYPE): Description
        client (TYPE): Description
        protocol (str): Description
        request_headers (TYPE): Description
        resource_path (TYPE): Description
    """

    def __init__(self, api_secret=None, resource_path=None, verify_ssl=True):
        """
        Summary.

        Args:
            api_secret (TYPE, optional): Description
            resource_path (TYPE, optional): Description
            verify_ssl (bool, optional): Description

        Raises:
            error.ValidationError: Description
        """
        self.protocol = util.utf8('https')
        self.api_host = util.utf8(self.protocol + '://api.paystack.co/')

        if not api_secret:  # pragma: no cover
            raise error.ValidationError("You must provide your API SECRET_KEY "
                                        "during object initialisation")

        if not resource_path:  # pragma: no cover
            raise error.ValidationError("You must provide the API endpoint "
                                        "for the resource you want to access.")

        self.api_secret = util.utf8(api_secret)
        self.resource_path = self._class_name(resource_path)
        self.client = RequestsClient(verify_ssl_certs=verify_ssl)
        self.request_headers = {
            "Authorization": "Bearer {0}".format(self.api_secret),
            "Content-Type": "application/json",
            "user-agent": "PaystackSDK - {0}".format(version.VERSION)
        }
        self._result = {}
        self._status_code = None
        self._response_headers = {}

    def all(self):  # pragma: no cover
        """
        Summary.

        Raises:
            NotImplementedError: Description

        Returns:
            name (TYPE): Description
        """
        raise NotImplementedError(
            'BaseAPIResource subclass must implement this method.')

    def one(self, id):  # pragma: no cover
        """
        Summary.

        Args:
            id (TYPE): Description

        Raises:
            NotImplementedError: Description

        Returns:
            name (TYPE): Description
        """
        raise NotImplementedError(
            'BaseAPIResource subclass must implement this method.')

    def post(self, data):  # pragma: no cover
        """
        Summary.

        Args:
            data (TYPE): Description

        Raises:
            NotImplementedError: Description

        Returns:
            name (TYPE): Description
        """
        raise NotImplementedError(
            'BaseAPIResource subclass must implement this method.')

    def delete(self, id):  # pragma: no cover
        """
        Summary.

        Args:
            id (TYPE): Description

        Raises:
            NotImplementedError: Description

        Returns:
            name (TYPE): Description
        """
        raise NotImplementedError(
            'BaseAPIResource subclass must implement this method.')

    def update(self, id, data):  # pragma: no cover
        """
        Summary.

        Args:
            id (TYPE): Description
            data (TYPE): Description

        Raises:
            NotImplementedError: Description

        Returns:
            name (TYPE): Description
        """
        raise NotImplementedError(
            'BaseAPIResource subclass must implement this method.')

    @property
    def status(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        return self._status_code

    @property
    def response(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        return self._result

    @property
    def headers(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self._response_headers

    @classmethod
    def _class_name(cls, resource_path):
        """
        Summary.

        Args:
            resource_path (TYPE): Description

        Raises:
            error.APIError: Description

        Returns:
            name (TYPE): Description
        """
        if cls == BaseAPIResource:
            raise error.APIError(
                'You cannot instantiate the API Base class directory.'
                'This is an abstract class.  You should perform '
                'actions on its subclasses (e.g. Charge, Customer).')
        return util.utf8(resource_path)


class CustomerResource(BaseAPIResource):  # pragma: no cover
    """Summary."""

    def __init__(self, *args, **kwargs):
        """
        Summary.

        Args:
            *args: Description
            **kwargs: Description

        Raises:
            NotImplementedError: Description
        """
        raise NotImplementedError(
            'CustomerResource: hasn\'t being implemented yet')


class TransactionResource(BaseAPIResource):
    """
    Base transaction resource Class.

    Encapsulate everything about a transaction instant.

    Attributes:
        access_code (string): Paystack access_code for initiating payment
        amount (int): Amount to pay in Kobo
        authorization_code (string): Paystack verification authorization_code
        authorization_url (string): Paystack verification authorization_url
        email (string): Client's email address
        reference (string): Unique transaction reference
    """

    def __init__(self, api_secret, reference=None,
                 resource_path='transaction', *args, **kwargs):
        """
        Create a TransactionResource instance.

        Args:
            api_secret (string): Developer's API SECRET_KEY.
            reference (string, optional): Unique transaction reference.
            resource_path (str, optional): API resource_path. Do not change.
            *args: Extra positional arguments.
            **kwargs: Extra keyworded arguments.
        """
        super(TransactionResource, self)\
            .__init__(api_secret, resource_path, *args, **kwargs)
        self.reference = util.utf8(reference)  # pragma no cover
        self.authorization_url = None  # pragma no cover
        self.access_code = None  # pragma no cover
        self.email = None  # pragma no cover
        self.amount = None  # pragma no cover
        self.authorization_code = None  # pragma no cover

    def initialize(self, amount, email,
                   plan=None, ref=None):  # pragma no cover
        """
        Transaction resource initialisation method.

        Args:
            amount (int): Amount to pay in Kobo.
            email (string): Client's email address.
            plan (string, optional): You customer billing plan.
            ref (string, optional): Unique transaction reference.

        Raises:
            error.APIError: Something generally bad happened... :()
            error.ValidationError: Bad input.

        Returns:
            response (dict): Response data from Paystack
        """
        endpoint = '/initialize'
        method = 'POST'

        self.reference = (lambda ref: ref if ref else self.reference)(ref)
        self.email = email
        self.amount = amount
        payload = {
            "amount": amount,
            "email": email,
            "plan": plan
        }
        if self.reference:
            payload.update(reference=self.reference)

        url = self.api_host + self.resource_path + endpoint
        response, status, headers = self.client.request(method, url,
                                                        self.request_headers,
                                                        post_data=payload)
        self._response_headers = headers
        self._status_code = status
        self._result = response
        if not response.get('status', False):
            raise error.APIError(response.get('message'))

        self.authorization_url = self._result['data'].get('authorization_url')
        self.access_code = self._result['data'].get('access_code')

        return response

    def verify(self, ref=None):  # pragma no cover
        """
        Verify transaction instance.

        Args:
            ref (string, optional): Unique transaction reference

        Raises:
            error.APIError: Something generally bad happened... :()
            error.ValidationError: Bad input.

        Returns:
            response (dict): Dictionary containing payment verification details
        """
        method = 'GET'

        if not ref and not self.reference:
            raise error.ValidationError('A unique object reference was not '
                                        'provided during instantiation. You'
                                        ' must provide a reference for this'
                                        ' transaction.')

        self.reference = (lambda ref: ref if ref else self.reference)(ref)

        endpoint = '/verify/' + self.reference
        url = self.api_host + self.resource_path + endpoint

        response, status, headers = self.client.request(method, url,
                                                        self.request_headers
                                                        )
        self._response_headers = headers
        self._status_code = status
        self._result = response['data']
        if not response.get('status', False):
            raise error.APIError(response.get('message'))

        self.authorization_code = self\
            ._result['authorization']['authorization_code']

        return response

    def charge(self, auth_code=None, amount=None,
               email=None, reference=None):  # pragma no cover
        """
        Bill a transaction to a customer's account.

        Args:
            auth_code (string, optional): Paystack verified authorization_code
            amount (int, optional): Amount to pay in Kobo.
            email (string, optional): Client's email address.
            reference (string, optional): Unique transaction reference.

        Raises:
            error.APIError: Something generally bad happened... :()
            error.ValidationError: Bad input.

        Returns:
            response (dict): Response data from Paystack
        """
        endpoint = '/charge_authorization'
        method = 'POST'

        if not auth_code and not self.authorization_code:
            raise error.ValidationError('This transaction object does not'
                                        ' have an authorization code.You must'
                                        ' provide an authorization code for'
                                        ' this transaction.')
        if not amount and not self.amount:
            raise error.ValidationError('There is no amount specified for this'
                                        ' transaction. You must provide the '
                                        ' transaction amount in Kobo.')
        if not email and not self.email:
            raise error.ValidationError('The customer\'s email address wss not'
                                        ' specified.')

        authorization_code = (
            lambda auth_code: auth_code if auth_code else self
            .authorization_code)(auth_code)

        email = (
            lambda email: email if email else self.email)(email)

        amount = (
            lambda amount: amount if amount else self.amount)(amount)

        payload = {
            "reference": reference,
            "amount": amount,
            "email": email,
            "authorization_code": authorization_code
        }

        url = self.api_host + self.resource_path + endpoint
        response, status, headers = self.client.request(method, url,
                                                        self.request_headers,
                                                        post_data=payload
                                                        )
        self._response_headers = headers
        self._status_code = status
        self._result = response
        if not response.get('status', False):
            raise error.APIError(response.get('message'))

        return response

    def authorize(self, auth_url=None):  # pragma: no cover
        """
        Open a browser window for client to enter card details.

        Args:
            auth_url (string, optional): Paystack verified authorization_url

        Raises:
            e: Browser Error :(
            error.ValidationError: Bad input.

        Returns:
            None
        """
        if not auth_url and not self.authorization_url:
            raise error.ValidationError('This transaction object does not'
                                        ' have an authorization url.You must'
                                        ' provide an authorization url or'
                                        'for call the `initialize` method'
                                        ' this transaction first.')

        authorization_url = (
            lambda auth_url: auth_url if auth_url else self
            .authorization_url)(auth_url)

        try:
            webbrowser.open_new_tab(authorization_url)
        except webbrowser.Error as e:
            raise e


class PlanResource(BaseAPIResource):  # pragma: no cover
    """Summary."""

    def __init__(self, *args, **kwargs):
        """
        Summary.

        Args:
            *args: Description
            **kwargs: Description

        Raises:
            NotImplementedError: Description
        """
        raise NotImplementedError(
            'PlanResource: hasn\'t being implemented yet')
