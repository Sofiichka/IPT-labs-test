SIZE = 5
class Queue:
    def __init__(self): #constructor for Queue class
        self.arr = [None]*SIZE
        self.front = self.rear = -1

    def isFull(self): #bool method if queue full
        if self.front == 0 and self.rear == SIZE-1:
            return True
        elif self.front == self.rear+1:
            return True
        else:
            return False

    def isEmpty(self):                     # bool method if queue empty
        if self.front == -1:
            return True
        else:
            return False

    def push(self, element): #push method for insertion elements in queue
        if self.isFull():
            print("IT'S OVERLOADED")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear+1)%SIZE # move rear number to the front
                                           # in case if it's the end of queue, move to the start 
            self.arr[self.rear] = element
            print('Element inserted')

    def pull(self):     #delete or pull method for removing elements from queue
        element = 0
        if self.isEmpty():
            print("IT'S EMPTY")
            return -1
        else:
            element = self.arr[self.front] # pull first element
            if self.front == self.rear:    # if the begin and the end of queue is te same element
                self.front = self.rear = -1 # remove them both and make the queue empty
            else:
                self.front = (self.front+1)% SIZE # move front element in the front
        return element

    def display(self): #display queue current state
        if self.isEmpty():
            print("IT'S EMPTY")
        else:
            print(self.front)
            for i in range(self.front, self.rear):
                print(self.arr[i])
            print(self.arr[i+1])
            print(self.rear)