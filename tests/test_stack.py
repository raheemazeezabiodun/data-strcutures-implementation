from unittest import TestCase

from stack import Stack

class TestStack(TestCase):
    def setUp(self):
        self.stack_obj = Stack()
    
    def test_empty_stack(self):
        self.assertDictEqual(self.stack_obj.get_stack(), {})

    def test_stack_method(self):
        self.stack_obj.push('Abbey')
        self.stack_obj.push('Biodun')

        self.assertEqual(self.stack_obj.get_length(), 2)
        self.assertDictEqual(self.stack_obj.get_stack(), {0: 'Abbey', 1: 'Biodun'})
        
        self.stack_obj.pop()
        self.assertEqual(self.stack_obj.get_length(), 1)
        self.assertDictEqual(self.stack_obj.get_stack(), {0: 'Abbey'})

        self.stack_obj.pop()
        self.stack_obj.pop()
        self.assertDictEqual(self.stack_obj.get_stack(), {})
        self.assertEqual(self.stack_obj.get_length(), 0)
