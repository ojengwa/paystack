paystack
===============================
[![Build Status](https://travis-ci.org/ojengwa/paystack.svg?branch=master)](https://travis-ci.org/ojengwa/paystack) [![Coverage Status](https://coveralls.io/repos/github/ojengwa/paystack/badge.svg?branch=master)](https://coveralls.io/github/ojengwa/paystack?branch=master) [![PyPI version](https://badge.fury.io/py/paystack.svg)](https://badge.fury.io/py/ibu) [![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/ojengwa/paystack/trend.png)](https://bitdeli.com/free "Bitdeli Badge")


Overview
--------

A Paystack API wrapper in Python

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


def main():
    secret_key = 'sk_test_ae4a423c668feac411cbc3c6719a52092176ca12'
    random_ref = 'asdsdswe224weuksfuf'
    test_email = 'bernard@disgui.se'
    test_amount = 5000
    plan = 'Basic'
    client = TransactionResource(secret_key, random_ref)
    response = client.initialize(test_amount,
                                 test_email,
                                 plan)
    print(response)
    verify = client.verify()
    print(verify)
    print(client.charge())

```
