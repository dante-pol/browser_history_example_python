import unittest
from Stack import *

class StackPushTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_positive_int(self):
        self.stack.push(11214)
        res = self.stack.peek()
        self.assertEquals(res,11214)

    def test_push_negarive_int(self):
        self.stack.push(-1121423)
        res = self.stack.peek()
        self.assertEquals(res, -1121423)


if __name__ == '__main__':
    unittest.main()