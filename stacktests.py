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

    def test_push_zero_int(self):
        self.stack.push(0)
        res = self.stack.peek()
        self.assertEquals(res, 0)

    def test_push_data_type_str(self):
        self.stack.push('-1121423sfjisjdfsidfuygadsad')
        res = self.stack.peek()
        self.assertEquals(res, '-1121423sfjisjdfsidfuygadsad')

    def test_push_data_type_int(self):
        self.stack.push(0.6)
        res = self.stack.peek()
        self.assertEquals(res, 0.6)

if __name__ == '__main__':
    unittest.main()