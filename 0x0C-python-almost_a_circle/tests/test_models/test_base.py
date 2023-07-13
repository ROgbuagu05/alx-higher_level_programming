#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base"""

    def test_none(self):
        """test id"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)


if __name__ == '__main__':
    unittest.main()
