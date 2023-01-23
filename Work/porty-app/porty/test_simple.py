# test_simple.py

import simple
import unittest

# Notice that it inherits from unittest.TestCase


class TestAdd(unittest.TestCase):
    def test_simple(self):
        # Test with simple integer arguments
        r = simple.add(2, 2)
        self.assertEqual(r, 5)

    def test_str(self):
        # Test with strings
        r = simple.add('hello', 'world')
        self.assertEqual(r, 'helloworld')

# # Assert that expr is True
# self.assertTrue(expr)

# # Assert that x == y
# self.assertEqual(x,y)

# # Assert that x != y
# self.assertNotEqual(x,y)

# # Assert that x is near y
# self.assertAlmostEqual(x,y,places)


# # Assert that callable(arg1,arg2,...) raises exc
# self.assertRaises(exc, callable, arg1, arg2, ...)
if __name__ == '__main__':
    unittest.main()
