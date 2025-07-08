class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
    def display(self):
        curr=self.head
        while curr:
            print(curr.data,end="-->")
            curr=curr.next
        print("None")
n=int(input("Enter the number of elements: "))
Llist=Linkedlist()
for i in range(n):
    a=int(input("Enter the element: "))
    Llist.insert_at_end(a)
Llist.display()