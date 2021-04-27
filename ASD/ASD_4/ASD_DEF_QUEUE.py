class Queue:
    def __init__(self): #constructor for Queue class
        self.arr = []*10
        self.front = 0

    def isEmpty(self): #bool method if queue empty
        if self.arr ==  []:
            return True
        else:
            return False

    def push(self, element): #push method for insertion elements in queue
        self.arr.insert(0,element)
        print('Element inserted')

    def pull(self): #delete or pull method for removing elements from queue
        if self.isEmpty():
            return -1
        else:
            self.arr.pop()
    def display(self):
        if self.isEmpty():
            print("IT'S EMPTY")
        else:
            for i in range(0,len(self.arr)):
                print(self.arr[i]) 
            print(self.rear)
            
main = Queue()
print(main.pull())
for i in range(10,15):
    main.push(i)
main.display()
main.pull()
main.display()