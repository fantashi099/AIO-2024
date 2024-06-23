
class Queue:
    def __init__(self, capacity: int) -> None:
        self.__capacity = capacity
        self.__list = []

    def is_empty(self):
        return len(self.__list) == 0
    
    def is_full(self):
        return len(self.__list) == self.__capacity
    
    def dequeue(self):
        if not self.is_empty():
            return self.__list.pop(0)
        return None
    
    def enqueue(self, value):
        self.__list.append(value)
    
    def front(self):
        if not self.is_empty():
            return self.__list[0]
        return None


if __name__ == '__main__':
    queue1 = Queue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)

    print(queue1.is_full())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.is_empty())