# -*- coding: utf-8 -*-
"""TestCases for the PaystackSDK."""

import unittest

from paystack import util
from paystack.resource import (TransactionResource,
                               )


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
    """]TestCase class for the PaystackSDK."""

    def setUp(self):
        """
        Test set up method.

        Returns:
            None
        """
        self.secret_key = 'sk_test_ae4a423c668feac411cbc3c6719a52092176ca12'
        self.random_ref = 'adkjwnhbhkbhb34242uksfuf'
        self.test_email = 'bernard@disgui.se'
        self.test_amount = 5000
        self.plan = 'Basic'
        self.client = TransactionResource(self.secret_key, self.random_ref)

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

    @unittest.skip
    def test_has_response(self):
        self.response = self.client.initialize(self.test_amount,
                                               self.test_email,
                                               self.plan)
        print(dir(self.response))
        self.assertIsNotNone(self.response)


class UtilTest(unittest.TestCase):
    """]TestCase class for the PaystackSDK."""

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

    def test_is_string(self):
        self.assertIsInstance(self.value, str)

    def test_equal(self):
        self.assertEqual(self.value, '138186')
