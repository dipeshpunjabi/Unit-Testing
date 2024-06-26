# test_arraylist.py

import unittest
from arraylist import ArrayList

class TestArrayList(unittest.TestCase):
    def setUp(self):
        self.list = ArrayList()
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)

    def test_get_valid_index(self):
        self.assertEqual(self.list.get(0), 1)
        self.assertEqual(self.list.get(1), 2)
        self.assertEqual(self.list.get(2), 3)

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError):
            self.list.get(-1)
        with self.assertRaises(IndexError):
            self.list.get(3)
    
    def test_size(self):
        self.assertEqual(self.list.size(), 3)

    def test_empty_list(self):
        empty_list = ArrayList()
        with self.assertRaises(IndexError):
            empty_list.get(0)

if __name__ == "__main__":
    unittest.main()
