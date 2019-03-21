class Node:

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.x = None
        self.y = None
        self.printed = False


    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                    self.left.x = self.x - 100
                    self.left.y = self.y + 100
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                    self.right.x = self.x + 100
                    self.right.y = self.y + 100
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def Inorder(self):
        if self.left:
           self.left.Inorder()

        print(self.data,end = ' ')

        if self.right:
            self.right.Inorder()
