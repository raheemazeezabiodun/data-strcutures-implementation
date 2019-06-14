from unittest import TestCase

from stack import Stack

class TestStack(TestCase):
    def setUp(self):
        self.stack_obj = Stack()
    
    def test_push_method(self):
        self.stack_obj.push('book1')
        self.stack_obj.push('book2')
        
        self.assertDictEqual(self.stack_obj.get_stack(), {
            0: 'book1',
            1: 'book2'
        })

    def test_pop_method(self):
        self.stack_obj.push('Nigeria')
        self.assertEqual(self.stack_obj.pop(), 'Nigeria')
        self.assertDictEqual(self.stack_obj.get_stack(), {})
        self.assertIsNone(self.stack_obj.pop())

    def test_peek(self):
        self.stack_obj.push('USA')
        self.stack_obj.push('Russia')

        self.assertEqual(self.stack_obj.peek(), 'Russia')

    def test_is_empty_method(self):
        self.assertTrue(self.stack_obj.is_empty())

        self.stack_obj.push('Yankee')
        self.assertFalse(self.stack_obj.is_empty())

    def test_get_size_method(self):
        self.assertEqual(self.stack_obj.size(), 0)
        self.stack_obj.push('New York')
        self.assertEqual(self.stack_obj.size(), 1)
