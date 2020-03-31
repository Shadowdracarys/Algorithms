class element():
    def __init__(self, key, val):
        self.key = key
        self.val = val

class directaddresstable():
    def search(self, k):
        return self[k]
    
    def insert(self, x):
        self[x.key] = x.val
    
    def delete(self, x):
        self[x.key] = None

class hashtable(list):
    def __init__(self):
        list.__init__([])

    def h(self, k):
        pass

    def insert(self, k):
        i = 0
        while True:
            j = h(k, i)
            if self[j] == None:
                self[j] = k
                return j
            else:
                i += 1
            if i == m:
                break
        print("hash table overflow")
    
    def search(self, k):
        i = 0
        while True:
            j = h(k, i)
            if self[j] == k:
                return j
            i += 1
            if self[j] == None or i == m:
                break
        return None
    
    def delelte(self, x):
        pass
if __name__ == "__main__":
    pass