Paystack
========

Installation / Usage
--------------------

To install use pip:

::

    $ pip install --upgrade paystack

or

::

    $ easy_install --upgrade paystack


Info
----

| See http://www.pip-installer.org/en/latest/index.html for instructions
| on installing pip. If you are on a system with easy\_install but not
| pip, you can use easy\_install instead. If you’re not using
  virtualenv,
| you may have to prefix those commands with ``sudo``. You can learn
  more
| about virtualenv at http://www.virtualenv.org/


To install from source, clone this repo and run:

::

    $ git clone https://github.com/ojengwa/paystack.git

    $ python setup.py install


Documentation
-------------

Please see https://developers.paystack.co/docs for the most up-to-date
documentation for the Paystack API.


API Anatomy
-----------------

Please see https://ojengwa.github.io/paystack/ for the most up-to-date
documentation of the API Anatomy.


Testing
-------

The package is compatible with Python 2.6+, Python 3.1+ and PyPy. We
need to test against all of these environments to ensure compatibility.
Travis CI will automatically run our tests on push. For local testing,
we use `nose`_ to handle testing across environments.

To run the included test:

#. Clone the repo:

::

   $ git clone https://github.com/ojengwa/paystack.git

#. Enter project directory:

::

   $ cd paystack

#. Install dependencies using fabric:

::

   $ fab install

#. Run the includded test using fabric:

::

   $ fab test


TODO
----

#. Add Event hooks
#. Create Consumer Resource
#. Create Plan Resource


Example
-------

::

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
        response = client.initialize(test_amount,
                                     test_email,
                                     plan)
        print(response)
        client.authorize() # Will open a browser window for client to enter card details
        verify = client.verify() # Verify client credentials
        print(verify)
        print(client.charge()) # Charge an already exsiting client



.. _nose: http://nose2.readthedocs.org/en/latest/

