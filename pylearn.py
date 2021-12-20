class Stack:
    data=[]

    def __init__(self,data=None):
        self.data=data
    
    def __str__(self):
        return str(self.data)
    
    def show(self):
        return self.data
    
    def find(self,id):
        for el in self.data:
            if el==id:
                return True
        return False
    
    def push(self,element):
        self.data.append(element)
    
    def peek(self):
        return self.data[-1]

    def pop(self):
        del self.data[-1]

#NODE CLASS
class Node():
    data=None
    next=None

    def  __init__(self,data,node=None):
        self.data=data
        self.next=node
    
    def __str__(self):
        return str(self.data)

#LINKLIST CLASS
class LinkList():
    head=None
    tail=None
    node=None
    cur=None
    def  __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,node):
        if self.head==None and self.tail==None:
            self.head=self.tail=Node(node)
            self.cur=self.head
        else:
            self.tail.next=Node(node)
            self.tail=self.tail.next

    def next(self):
        self.cur=self.cur.next
        return self.cur

    def contains(self,data):
        while True:
            if self.cur.data==data:
                return True
            elif self.cur.next!=None:
                self.next()
            else:
                return False

    def find(self,data):
        while True:
            if self.cur.data==data:
                return self.cur
            elif self.cur.next!=None:
                self.next()
            else:
                print("Node with such data doesn't exist")
                return None
            
    def insertAfter(self,position,data):
        node=self.find(position)
        if  node != None:
            newnode=Node(data)
            oldenode=node.next
            node.next=newnode
            newnode.next=oldenode
        return newnode

    def removeAfter(self,position):
        node=self.find(position)
        if  node.next != None:
            tempnode=node.next.next
            del node.next
            node.next=tempnode
            return True
        return False


#singleton design pattern

class Single:
    instance=None

    
    def __init__(self):
        if Single.instance==None:
            Single.instance=self
        else:
            Single.instance
    def get_instance(cls):
        return instance
print(Single())
print(Single())