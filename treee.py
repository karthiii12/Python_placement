class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    #def insert(self,data):

root=Node(10)
root.left=Node(20)
root.right=Node(90)
root.left.left=Node(30)
root.left.right=Node(80)
root.left.left.left=Node(40)
root.left.left.right=Node(50)
root.left.right.left=Node(60)
root.left.right.right=Node(70)
root.right.right=Node(100)
root.right.right.left=Node(110)
root.right.right.right=Node(120)
root.right.right.right.left=Node(140)
root.right.right.right.right=Node(150)

def PreOrder(root):
    if not root:
        return 0
    else:
        print(root.data,end=' ')
        PreOrder(root.left)
        PreOrder(root.right)
def InOrder(root):
    if not root:
        return 0
    else:
        InOrder(root.left)
        print(root.data,end=' ')
        InOrder(root.right)
def PostOrder(root):
    if not root:
        return 0
    else:
        PostOrder(root.left)
        PostOrder(root.right) 
        print(root.data,end=' ')
def Cnode(root):
    if not root:
        return 0
    else:
        return 1+Cnode(root.left)+Cnode(root.right) 
def SNode(root):
    if not root:
        return 0
    else:
        return root.data + SNode(root.left) + SNode(root.right)
def HNode(root):
    if not root:
        return 0
    else:
        lefthh=HNode(root.left)
        Righth=HNode(root.right)
        return 1+max(lefthh,Righth)
def Depth(root,n,lv=0):
        if not root:
            return -1
        else:
            if root.data==n:
                return lv
            leftdep=Depth(root.left,n,lv+1)
            if leftdep!=-1:
                return leftdep
            return Depth(root.right,n,lv+1)
            

        
print("PreOrder:")
PreOrder(root)
print("\n")
print("InOrder:")
InOrder(root)
print("\n")
print("PostOrder:")
PostOrder(root)
print("\n")
print("Count of Nodes:")
print(Cnode(root))
#print("\n")
print("Sum of Nodes:")
print(SNode(root))
print("Height:")
print(HNode(root))
print("Depth:")
print(Depth(root,120))