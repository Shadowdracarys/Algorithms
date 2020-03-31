class redblacktree():
    class node():
        def __init__(self, x):
            self.key = x
            self.left = None
            self.right = None
            self.p = None
            self.color = None
    
    def __init__(self):
        self.root = None
        self.nil = None
    
    def inorder_tree_walk(self, x):
        if x != None:
            self.inorder_tree_walk(x.left)
            print(x.key)
            self.inorder_tree_walk(x.right)
    
    def search(self, x, k):
        if x == None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)
    
    def iterative_search(self, x, k):
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
    
    def minimun(self, x):
        while x.left != None:
            x = x.left
        return x
    
    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x
    
    def successor(self, x):
        if x.right != None:
            return self.minimun(x.right)
        y = x.p
        while y != None and x = y.right:
            x = y
            y = y.p
        return y
    
    def insert(self, z):
        def insert_fixup(self, z):
            while z.p.color == "RED":
                if z.p == z.p.p.left:
                    y = z.p.p.right
                    if y.color == "RED":
                        z.p.color = "BLACK"
                        y.color = "BLACK"
                        z.p.p.color = "RED"
                        z = z.p.p
                    else:
                        if z == z.p.right:
                            z= z.p
                            self.left_rotate(z)
                        z.p.color = "BLACK"
                        z.p.p.color = "RED"
                        self.right_rotate(z.p.p)
                else:
                    pass
            self.root.color = "BLACK"

        y = self.nil
        x = self.root
        while x != T.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
            z.p = y
            if y == T.nil:
                self.root = z
            elif z.key < y.key:
                y.left = z
            else:
                y.right = z
            z.left = self.nil
            z.right = self.nil
            z.color = "RED"
            insert_fixup(z)

    def delete(self, z):
        def transplant(self, u, v):
            if u.p == self.nil:
                self.root = v
            elif u = u.p.left:
                u.p.left = v
            else:
                u.p.right = v
            v.p = u.p
        
        def delete_fixup(self, x):
            while x != self.root and x.color == "BLACK":
                if x == x.p.left:
                    w = x.p.right
                    if w.color == "RED":
                        w.color = "BLACK"
                        x.p.color = "RED"
                        self.left_rotate(x.p)
                        w = x.p.right
                    if w.left.color == "BLACK" and w.right.color == "BLACK":
                        w.color = "RED"
                        x = x.p
                    else:
                        if w.right.color == "BLACK":
                            w.left.color = "BLACK"
                            w.color = "RED"
                            self.right_rotate(w)
                            w = x.p.right
                        w.color = x.p.color
                        x.p.color = "BLACK"
                        w.right.color = "BLACK"
                        self.left_rotate(x.p)
                        x = self.root
                else:
                    pass
            x.color = "BLACK"
        
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            trafnsplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            transplant(z, z.left)
        else:
            y = self.minimun(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == "BLACK":
            delete_fixup(x)
    
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
    
    def right_rotate(self, x):
        pass

if __name__ == "__main__":
    pass