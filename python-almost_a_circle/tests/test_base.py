#!/usr/bin/python3
import unittest
from ..models.base import Base


class TestModules(unittest.TestCase):
    def test_base(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
    
    def test_idsequence(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

if __name__ == '__main__':
    unittest.main()
