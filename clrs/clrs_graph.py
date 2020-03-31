from clrs_data_structure import queue

class graph:
    class vertex:
        def __init__(self):
            self.color = None
            self.d = None
            self.pi = None

    def __init__(self, v):
        self.V = v
        self.E = 0
        self.Adj = dict()
        for u in self.V:
            self.Adj[u] = list()
        
    def breadth_first_search(self, s):
        for u in G.V:
            u.color = "WHITE"
            u.d = 65536
            u.pi = "NIL"
        s.color = "GRAY"
        s.d = 0
        s.pi = "NIL"
        Q = queue()
        Q.enqueue(s)
        while not Q.isEmpty():
            u = Q.dequeue()
            for v in self.Adj[u]:
                if v.color == "WHITE":
                    v.color = "GRAY"
                    v.d = u.d + 1
                    v.pi = u
                    Q.enqueue(s)
            u.color = "BLACK"

    def depth_first_search(self):
        for u in self.V:
            u.color = "WHITE"
            u.pi = "NIL"
        time = 0
        for u in self.V:
            if u.color == "WHITE":
                DFS_visit(u)
    
        def DFS_visit(u):
            time += 1
            u.d = time
            u.color = "GRAY"
            for v in self.Adj[u]:
                if v.color == "WHITE":
                    v.pi = u
                    DFS_visit(v)
            u.color = "BLACK"
            time += 1
            u.f = time

    def print_path(self, s, v):
        if v==s:
            print(s)
        elif v.pi == "NIL":
            print("no path from %s to %s exists"%(s, v))
        else:
            self.print_path(s, v.pi)
            print(v)