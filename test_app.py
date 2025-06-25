import unittest

from app import say_hello

class test_hello(unittest.TestCase):
    def test_say_hello(self):
        self.asserEqual(say_hello("abdi"),"abdi")

if __name__ == "__main__":
    unittest.main()