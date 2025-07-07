class Stack:
    def __init__(self):
        self.s=[]
    def push(self,item):
        self.s.append(item)
    def pop(self):
        if not self.s:
            return None
        else:
            return self.s.pop()
    def peek(self):
        return self.s[-1]
    def isempty(self):
        if len(self.s)==0:
            print("Stack is empty")
        else:
            print("Stack Has elements")
s1=Stack()
n=int(input("Enter the number of stack elements: "))
for i in range(n):
    item=int(input(f"Enter the {i} th number to be pushed :"))
    s1.push(item)        #pushing the item
print(s1.s)              #printing the new stack
print(s1.peek())         #peeking the top most element
print(s1.pop())          #popping the last element
print(s1.s)              #stack after popping
print(s1.isempty())      #to check if empty