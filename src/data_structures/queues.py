class Queues:
    def __init__(self) -> None:
        self.elements = []
    
    def push(self, element):
        self.elements.insert(0, element)

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
    

queues = Queues()
print(queues.empty())
queues.push(5)
print(queues.empty())
queues.push(6)
queues.push(2)
print(queues.first_element())
print(queues.pop())
print(queues.first_element())