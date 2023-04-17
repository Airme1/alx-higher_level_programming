#!/usr/bin/python3
import unittest
from models.base import Base

"""
Testing begins with base case
"""


class TestBase(unittest.TestCase):
    """Test Base Case"""
    b = Base()
    def test_base(self):
        self.assertEqual(b.id, 1)
