"""
A basic implementation of the Stack data structure.

Usage:
    stack = Stack()
    stack.push(data) # data can be anything e.g String, Int, list
    stack.peek()
    stack.size()
    stack.pop()
    stack.size()
"""


class Stack:
    def __init__(self):
        """Constructor."""
        self.count = 0
        self.stack = {}

    def push(self, value):
        """
        Push a value to the top of the stack

        :params: value
        """
        self.stack[self.count] = value
        self.count += 1

    def pop(self):
        """
        Pop the last item was added to the stack

        :return : the last value of the stack
        """
        if self.count < 1:
            return None
        else:
            self.count -= 1
            popped_item = self.stack[self.count]
            del self.stack[self.count]
            return popped_item

    def peek(self):
        """Return the last item added."""
        return self.stack[self.count - 1]

    def is_empty(self):
        """Return a boolean if stack is empty."""
        return not self.stack

    def size(self):
        """Return the size of the stack."""
        return self.count

    def get_stack(self):
        """Return the size of the stack."""
        return self.stack

    def __str__(self):
        return "Stack implementation"