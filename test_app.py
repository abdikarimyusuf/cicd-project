import unittest

from app import say_hello

class test_hello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello("abdi"),"hi:abdi")

if __name__ == "__main__":
    unittest.main()