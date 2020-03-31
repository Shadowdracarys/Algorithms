class queue(list):
    def __init__(self):
        list.__init__([])
        self.head = 0
        self.tail = 0
        self.length = 0

    def enqueue(self, x):
        self.append(x)
        if self.tail == self.length:
            self.tail = 1
        else:
            self.tail += 1

    def dequeue(self):
        x = self[self.head]
        if self.head == self.length:
            self.head = 1
        else:
            self.head += 1
        return x
    
    def isEmpty(self):
        return self.length==0



class stack(list):
    def __init__(self):
        list.__init__([])
        self.top = 0

    def stack_empty(self):
        if self.top == 0:
            return True
        else:
            return False
    
    def push(self, x):
        self.top += 1
        self.append(x)
    
    def pop(self, S):
        if self.stack_empty():
            raise print('underflow')
        else:
            self.top -= 1
            return self[self.top+1]



class linked_list():
    class node():
        def __init__(self, x):
            self.key = x
            self.prev = None
            self.next = None
    
    def __init__(self):
        self.head = None
    
    def list_search(self, k):
        x = self.head
        while x != None and x.key != k :
            x = x.next
        return x
    
    def list_insert(self, x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None
    
    def list_delete(self, x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev