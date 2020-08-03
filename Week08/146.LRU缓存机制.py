class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:
    def __init__(self, capacity: int):
        self.dic={}
        self.head=Node(None,None)
        self.tail=Node(None,None)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity

    def get(self, key: int) -> int:
        if not key in self.dic:
            return -1
        node=self.dic[key]
        self.delete(node)
        self.insert(node)
        return node.val        

    def insert(self,node):
        node.next,node.prev=self.head.next,self.head
        temp=self.head.next
        self.head.next=node
        temp.prev=node

    def delete(self,node):
        node.prev.next,node.next.prev=node.next,node.prev

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node=self.dic[key]
            node.val=value
            self.delete(node)
            self.insert(node)
            return        
        if len(self.dic)==self.capacity:
            node=self.tail.prev
            self.delete(node)
            del self.dic[node.key]
        node=Node(key,value)
        self.dic[key]=node
        self.insert(node)
