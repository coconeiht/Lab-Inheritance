class Stack:
    def __init__(self):
        self.data = []

    def push(self, item: str):
        if not isinstance(item, str):
            raise ValueError("Only strings are allowed in the stack")
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self):
        return str(self.data)