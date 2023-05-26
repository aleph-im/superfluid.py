import unittest

from main.superfluid import is_permissions_clean


class TestPermissionChecker(unittest.TestCase):

    def test_valid_permissions(self):
        self.assertEqual(is_permissions_clean(
            1), True)
        self.assertEqual(is_permissions_clean(
            2), True)
        self.assertEqual(is_permissions_clean(
            3), True)
        self.assertEqual(is_permissions_clean(
            4), True)
        self.assertEqual(is_permissions_clean(
            5), True)
        self.assertEqual(is_permissions_clean(
            6), True)
        self.assertEqual(is_permissions_clean(
            7), True)

    def test_invalid_permissions(self):
        self.assertEqual(is_permissions_clean(
            8), False)
        self.assertEqual(is_permissions_clean(
            9), False)
        self.assertEqual(is_permissions_clean(
            10), False)
        self.assertEqual(is_permissions_clean(
            11), False)
        self.assertEqual(is_permissions_clean(
            12), False)
        self.assertEqual(is_permissions_clean(
            13), False)
        self.assertEqual(is_permissions_clean(
            14), False)
