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
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        from paystack.version import VERSION
        self.assertIsInstance(VERSION, str)


class TransactionResourceTest(unittest.TestCase):
    """TestCase class for the PaystackSDK.

    Attributes:
        client (TYPE): Description
        plan (str): Description
        random_ref (TYPE): Description
        response (TYPE): Description
        secret_key (str): Description
        test_amount (int): Description
        test_email (str): Description
    """

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
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self.assertIsInstance(self.client, TransactionResource)

    def test_has_resource_path(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self.assertEqual(self.client.resource_path, 'transaction')

    def test_has_reference(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self.assertEqual(self.client.reference, self.random_ref)

    @unittest.skip
    def test_has_response(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self.response = self.client.initialize(self.test_amount,
                                               self.test_email,
                                               self.plan)
        self.assertIsNotNone(self.response)


class UtilTest(unittest.TestCase):
    """TestCase class for the util module.

    Attributes:
        value (TYPE): Description
    """

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
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self.assertIsInstance(self.value, str)

    def test_equal(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self.value = util.utf8(138186)
        self.assertEqual(self.value, 138186)


class HTTPClientTest(unittest.TestCase):
    """TestCase class for the HTTPClient class.

    Attributes:
        client (TYPE): Description
        headers (dict): Description
        method (str): Description
        url (str): Description
    """

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
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self.assertIsInstance(self.client, HTTPClient)

    def test_verify_ssl(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self.assertEqual(self.client._verify_ssl_certs, True)


class RequestsClientTest(unittest.TestCase):
    """TestCase class for the HTTPClient class.

    Attributes:
        client (TYPE): Description
        headers (dict): Description
        method (str): Description
        url (str): Description
    """

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
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self.assertIsInstance(self.client, RequestsClient)

    def test_verify_ssl(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self.assertEqual(self.client._verify_ssl_certs, True)

    @unittest.skip
    def test_kwargs_is_verify(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        verify = self.kwargs['verify']
        self.assertTrue(verify)

    @unittest.skip
    def test_kwargs_is_not_verify(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self._verify_ssl_certs = False
        self.client.request(self.method, self.url, self.headers)
        verify = self.kwargs['verify']
        self.assertFalse(verify)

    @unittest.skip
    def test_status_code(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self.client.request(self.method, self.url, self.headers)
        self.assertIsInstance(self._status_code, int)

    @unittest.skip
    def test_response(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        response = self.client.request(self.method, self.url, self.headers)
        self.assertIsInstance(response, tuple)

    @unittest.skip
    def test_not_implemented(self):
        """
        Summary.

        Returns:
            name (TYPE): Description
        """
        self.assertRaises(self.client.request(self.method,
                                              self.url,
                                              self.headers
                                              ), NotImplementedError)
