paystack
===============================

version number: 0.0.1
author: Bernard Ojengwa

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

Contributing
------------

TBD

Example
-------

TBD