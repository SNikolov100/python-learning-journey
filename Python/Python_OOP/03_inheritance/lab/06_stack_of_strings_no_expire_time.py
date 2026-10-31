class Stack:
    def __init__(self):
        self.data:list = []

    def push(self, element:str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if len(self.data) == 0 else False

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


first_stack = Stack()
first_stack.push("11")
first_stack.push("111")
first_stack.push("adf")
print(first_stack)