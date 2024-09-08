class Stack:
    def __init__(self) -> None:
        self.elements = []
    
    def push(self, element):
        self.elements.append(element)
    
    def empty(self):
        if self.elements:
            return False
        return True

    def first_element(self):
        return self.elements[-1]
    
    def pop(self):
        element = self.elements[-1]
        self.elements.pop(-1)
        return element


stack = Stack()
print(stack.empty())
stack.push(5)
print(stack.empty())
stack.push(6)
stack.push(2)
print(stack.first_element())
print(stack.pop())
print(stack.first_element())