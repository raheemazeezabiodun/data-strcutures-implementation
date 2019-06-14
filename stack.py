class Stack:
    def __init__(self):
        self.count = 0  # holds stack
        self.stack = {}

    
    def push(self, value):
        self.stack[self.count] = value
        self.count += 1

    def pop(self):
        if self.count < 1:
            return None
        else:
            self.count -= 1
            del self.stack[self.count]

    def get_length(self):
        return self.count

    def get_stack(self):
        return self.stack

    def __str__(self):
        return "Stack implementation"