
# implement a class stack
class stack:
    def __init__(self):
        self.items = []
    '''
    all the methods below takes O(1) constant time
    '''
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            return "Stack is empty"
        else:
            return self.items.pop()

    def peek(self):
        if self.items == []:
            return "stack is empty"
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def isempty(self):
        if self.items == []:
            return True
        else:
            return False


mystack = stack()
