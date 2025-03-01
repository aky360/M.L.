class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from an empty stack")

    def peek(self):
        """Return the top item from the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from an empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the stack."""
        return str(self.items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)        # Output: [1, 2, 3]
print(stack.pop())  # Output: 3
print(stack.peek()) # Output: 2
print(stack.size()) # Output: 2
print(stack.is_empty()) # Output: False
