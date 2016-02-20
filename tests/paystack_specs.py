# -*- coding: utf-8 -*-
"""TestCases for the PaystackSDK."""

import unittest


class PaystackSDKTest(unittest.TestCase):
    """]TestCase class for the PaystackSDK."""

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
