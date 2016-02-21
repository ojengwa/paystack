# -*- coding: utf-8 -*-
"""TestCases for the PaystackSDK."""

import unittest
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
        self.random_ref = 'adkjwnhbhkbhbuksfuf'
        self.test_email = 'bernard@disgui.se'
        self.test_amount = 5000
        self.plan = 'Basic'

    def tearDown(self):
        """
        Test tear down method.

        Returns:
            None
        """
        pass

    def test_init(self):
        client = TransactionResource(self.secret_key, self.random_ref)
        self.assertIsInstance(client, TransactionResource)
        self.assertEqual(client.resource_path, 'transaction')
