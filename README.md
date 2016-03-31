paystack
===============================

[![Build Status](https://travis-ci.org/ojengwa/paystack.svg?branch=master)](https://travis-ci.org/ojengwa/paystack) [![Coverage Status](https://coveralls.io/repos/github/ojengwa/paystack/badge.svg?branch=master)](https://coveralls.io/github/ojengwa/paystack?branch=master) [![PyPi Version](https://badge.fury.io/py/paystack.svg)](https://badge.fury.io/py/paystack) [![PyPI](https://img.shields.io/pypi/dm/paystack.svg)](https://pypi.python.org/pypi/paystack)


Overview
--------

Paystack API bindings in Python.

Installation / Usage
--------------------

To install use pip:

    $ pip install --upgrade paystack

or

    $ easy_install --upgrade paystack

See http://www.pip-installer.org/en/latest/index.html for instructions
on installing pip. If you are on a system with easy_install but not
pip, you can use easy_install instead. If you're not using virtualenv,
you may have to prefix those commands with `sudo`. You can learn more
about virtualenv at http://www.virtualenv.org/

To install from source, clone this repo and run:

    $ git clone https://github.com/ojengwa/paystack.git
    $ python setup.py install


Documentation
-------------

Please see https://developers.paystack.co/docs for the most up-to-date documentation for the Paystack API.


API Anatomy
-------------

The API resource are exposed via a single interface `paystack.resource`.

Classes exposed via the interface includes:
`'BaseAPIResource', 'CustomerResource', 'PlanResource', 'RequestsClient', 'TransactionResource', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'error', 'util', 'version'`

Documentation and signature for each of the methods defined in the API follows:

**TransactionResource**:

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


    def charge(self, auth_code=None, amount=None,
               email=None, reference=None):  # pragma no cover
        """
        Bill a transaction to a customer's account.

        Args:
            auth_code (string, optional): Paystack verification authorization_code
            amount (int, optional): Amount to pay in Kobo.
            email (string, optional): Client's email address.
            reference (string, optional): Unique transaction reference.

        Raises:
            error.APIError: Something generally bad happened... :()
            error.ValidationError: Bad input.

        Returns:
            response (dict): Response data from Paystack
        """


    def authorize(self, auth_url=None):  # pragma: no cover
        """
        Open a browser window for client to enter card details.

        Args:
            auth_url (string, optional): Paystack verification authorization_url

        Raises:
            e: Browser Error :(
            error.ValidationError: Bad input.

        Returns:
            None
        """


Testing
-------------

The package is compatible with Python 2.6+, Python 3.1+ and PyPy.  We need to test against all of these environments to ensure compatibility.  Travis CI will automatically run our tests on push.  For local testing, we use [nose](http://nose2.readthedocs.org/en/latest/) to handle testing across environments.

To run the included test:

1. Clone the repo:

    ```$ git clone https://github.com/ojengwa/paystack.git```

2. Cd into project directory:

    ```$ cd paystack```

3. Install dependencies:

    ```$ pip install -r requirements.txt```

4. Run the includded test using fabric:

    ```$ fab test```

TODO
------------

1. Add Event hooks
2. Create Consumer Resource
3. Create Plan Resource

Example
-------

```

from paystack.resource import TransactionResource

import random
import string

def main():
    rand = ''.join(
        [random.choice(
            string.ascii_letters + string.digits) for n in range(16)])
    secret_key = 'YOUR_SECRET_KEY'
    random_ref = rand
    test_email = 'TEST_EMAIL'
    test_amount = 'TEST_AMOUNT'
    plan = 'Basic'
    client = TransactionResource(secret_key, random_ref)
    response = c****lient.initialize(test_amount,
                                 test_email,
                                 plan)
    print(response)
    client.authorize() # Will open a browser window for client to enter card details
    verify = client.verify() # Verify client credentials
    print(verify)
    print(client.charge()) # Charge an already exsiting client

```
