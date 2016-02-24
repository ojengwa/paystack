# -*- coding: utf-8 -*-
"""TestCases for the PaystackSDK."""

import unittest
import random
import string

from paystack import util
from paystack.resource import (TransactionResource,
                               )
from paystack.client import (HTTPClient,
                             RequestsClient)


class PaystackSDKTest(unittest.TestCase):
    """TestCase class for the PaystackSDK."""

    def setUp(self):
        """
        Test set up method.

        Returns:
            None
        """
        pass

    def tearDown(self):
        """
        Test tear down method.

        Returns:
            None
        """
        pass

    def test_version(self):
        from paystack.version import VERSION
        self.assertIsInstance(VERSION, str)


class TransactionResourceTest(unittest.TestCase):
    """TestCase class for the PaystackSDK."""

    def setUp(self):
        """
        Test set up method.

        Returns:
            None
        """
        rand = ''.join(
            [random
             .choice(string.ascii_letters + string.digits) for n in range(16)])
        self.secret_key = 'sk_test_16c58271c29a007970de0353d8a47868df727cd0'
        self.random_ref = util.utf8(rand)
        self.test_email = 'bernard@disgui.se'
        self.test_amount = 5000
        self.plan = 'Basic'
        self.client = TransactionResource(self.secret_key, self.random_ref)
        self.client.initialize(util.utf8(self.test_amount),
                               util.utf8(self.test_email),
                               util.utf8(self.plan))

    def tearDown(self):
        """
        Test tear down method.

        Returns:
            None
        """
        pass

    def test_instance_of(self):
        self.assertIsInstance(self.client, TransactionResource)

    def test_has_resource_path(self):
        self.assertEqual(self.client.resource_path, 'transaction')

    def test_has_reference(self):
        self.assertEqual(self.client.reference, self.random_ref)

    @unittest.skip
    def test_has_response(self):
        self.response = self.client.initialize(self.test_amount,
                                               self.test_email,
                                               self.plan)
        self.assertIsNotNone(self.response)


class UtilTest(unittest.TestCase):
    """TestCase class for the util module."""

    def setUp(self):
        """
        Test set up method.

        Returns:
            None
        """
        self.value = util.utf8('138186')

    def tearDown(self):
        """
        Test tear down method.

        Returns:
            None
        """
        pass

    def test_utf8(self):
        self.assertIsInstance(self.value, str)

    def test_equal(self):
        self.value = util.utf8(138186)
        self.assertEqual(self.value, 138186)


class HTTPClientTest(unittest.TestCase):
    """TestCase class for the HTTPClient class."""

    def setUp(self):
        """
        Test set up method.

        Returns:
            None
        """
        self.client = HTTPClient()
        self.method = 'GET'
        self.url = 'http://github.com/ojengwa'
        self.headers = {}

    def tearDown(self):
        """
        Test tear down method.

        Returns:
            None
        """
        pass

    def test_isinstance(self):
        self.assertIsInstance(self.client, HTTPClient)

    def test_verify_ssl(self):
        self.assertEqual(self.client._verify_ssl_certs, True)


class RequestsClientTest(unittest.TestCase):
    """TestCase class for the HTTPClient class."""

    def setUp(self):
        """
        Test set up method.

        Returns:
            None
        """
        self.client = RequestsClient()
        self.method = 'GET'
        self.url = 'http://github.com/ojengwa'
        self.headers = {}

    def tearDown(self):
        """
        Test tear down method.

        Returns:
            None
        """
        pass

    def test_isinstance(self):
        self.assertIsInstance(self.client, RequestsClient)

    def test_verify_ssl(self):
        self.assertEqual(self.client._verify_ssl_certs, True)

    @unittest.skip
    def test_kwargs_is_verify(self):
        verify = self.kwargs['verify']
        self.assertTrue(verify)

    @unittest.skip
    def test_kwargs_is_not_verify(self):
        self._verify_ssl_certs = False
        self.client.request(self.method, self.url, self.headers)
        verify = self.kwargs['verify']
        self.assertFalse(verify)

    @unittest.skip
    def test_status_code(self):
        self.client.request(self.method, self.url, self.headers)
        self.assertIsInstance(self._status_code, int)

    @unittest.skip
    def test_response(self):
        response = self.client.request(self.method, self.url, self.headers)
        self.assertIsInstance(response, tuple)

    @unittest.skip
    def test_not_implemented(self):
        self.assertRaises(self.client.request(self.method,
                                              self.url,
                                              self.headers
                                              ), NotImplementedError)
