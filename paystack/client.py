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
import os
import textwrap
import requests

from paystack import error

try:
    import json
except Exception as e:  # pragma: no cover
    import simplejson as json


class HTTPClient(object):
    """Base API Request Client."""

    def __init__(self, verify_ssl_certs=True):
        """
        Summary.

        Args:
            verify_ssl_certs (bool, optional): SSL is not yet supported.
        """
        self._verify_ssl_certs = verify_ssl_certs

    def request(self, method, url, headers, post_data=None):
        """
        Summary.

        Args:
            method (TYPE): Description
            url (TYPE): Description
            headers (TYPE): Description
            post_data (TYPE, optional): Description

        Raises:
            NotImplementedError: Description

        Returns:
            TYPE: Description
        """
        raise NotImplementedError(
            'HTTPClient subclasses must implement `request`'
        )  # pragma: no cover


class RequestsClient(HTTPClient):  # pragma: no cover
    """
    Summary.

    Attributes:
        name (str): Description
    """

    def request(self, method, url, headers, post_data=None):
        """
        Summary.

        Args:
            method (TYPE): Description
            url (TYPE): Description
            headers (TYPE): Description
            post_data (TYPE, optional): Description

        Raises:
            TypeError: Description

        Returns:
            TYPE: Description
        """
        self.kwargs = {}

        if self._verify_ssl_certs:
            key = os.path.join(
                os.path.dirname(__file__), 'data/paystack.key')
            cert = os.path.join(
                os.path.dirname(__file__), 'data/paystack.crt')
            self.kwargs['cert'] = (cert, key)
        else:
            self.kwargs['verify'] = False

        try:
            try:
                result = requests.request(method,
                                          url,
                                          headers=headers,
                                          data=json.dumps(post_data),
                                          timeout=80,
                                          **self.kwargs)
            except TypeError as e:  # pragma: no cover
                raise TypeError(
                    'Warning: It looks like your installed version of the '
                    '"requests" library is not compatible with Paystack\'s '
                    'usage thereof. (HINT: The most likely cause is that '
                    'your "requests" library is out of date. You can fix '
                    'that by running "pip install -U requests".) The '
                    'underlying error was: %s' % (e,))

            # This causes the content to actually be read, which could cause
            # e.g. a socket timeout. TODO: The other fetch methods probably
            # are susceptible to the same and should be updated.
            self._content = (lambda cont: json
                             .loads(cont) if cont else None)(result.content)
            self._status_code = result.status_code

        except Exception as e:
            # Would catch just requests.exceptions.RequestException, but can
            # also raise ValueError, RuntimeError, etc.
            self._handle_request_error(e)
        return self._content, self._status_code, result.headers

    def _handle_request_error(self, e):
        """
        Summary.

        Args:
            e (TYPE): Description

        Raises:
            error.APIConnectionError: Description

        Returns:
            TYPE: Description
        """
        if isinstance(e, requests.exceptions.RequestException):
            msg = ("Unexpected error communicating with Paystack.  "
                   "If this problem persists, let me know at "
                   "bernardojengwa@gmail.com.")
            err = "%s: %s" % (type(e).__name__, str(e))
        else:  # pragma: no cover
            msg = ("Unexpected error communicating with Paystack. "
                   "It looks like there's probably a configuration "
                   "issue locally.  If this problem persists, let me "
                   "know at bernardojengwa@gmail.com.")
            err = "A %s was raised" % (type(e).__name__,)
            if str(e):
                err += " with error message %s" % (str(e),)
            else:
                err += " with no error message"
        msg = textwrap.fill(msg) + "\n\n(Network error: %s)" % (err,)
        raise error.APIConnectionError(msg)
