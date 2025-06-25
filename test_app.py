import unittest

from app import say_hello

class test_hello(unittest.testcase):
    def test_say_hello(self):
        self.asserEqual(say_hello(),"abdi")

if __name__ == "__main__":
    unittest.main()