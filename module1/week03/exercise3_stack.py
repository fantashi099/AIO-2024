
class Stack:
    def __init__(self, capacity: int) -> None:
        self.__capacity = capacity
        self.__list = []

    def is_empty(self):
        return len(self.__list) == 0
    
    def is_full(self):
        return len(self.__list) == self.__capacity
    
    def pop(self):
        if not self.is_empty():
            return self.__list.pop()
        return None
    
    def push(self, value):
        self.__list.append(value)
    
    def top(self):
        if not self.is_empty():
            return self.__list[-1]
        return None
    

if __name__ == '__main__':
    stack1 = Stack(capacity=5)
    stack1.push(1)
    stack1.push(2)

    print(stack1.is_full())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.is_empty())
