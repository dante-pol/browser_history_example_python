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

    def test_push_data_type_float(self):
        self.stack.push(0.6)
        res = self.stack.peek()
        self.assertEquals(res, 0.6)

class StackIsEmptyTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
    def test_is_empty_true(self):
        res = self.stack.is_empty()
        self.assertEquals(res,True)
    def test_is_empty_false(self):
        self.stack.push(121124)
        res = self.stack.is_empty()
        self.assertEquals(res, False)
    def test_is_empty_false(self):
        self.stack.push('fuasfsjafasfsafsaf')
        res = self.stack.is_empty()
        self.assertEquals(res, False)


if __name__ == '__main__':
    unittest.main()