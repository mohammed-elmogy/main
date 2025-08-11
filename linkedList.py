#linkedLisk unarrganged
#two copy linked list 
#new linked list to arrange
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self,head):
        self.head=head
        self.startPoint=Node(head)
        self.endPoint=self.startPoint
        self.data=str(head)
    def add(self,value):
        newNode=Node(value)
        self.endPoint.next=newNode
        self.endPoint=newNode
        self.data+="=>"+str(value)
        return self
    def addAtStart(self,value):
        newNode=Node(value)
        newNode.next=self.startPoint
        self.startPoint=newNode
        self.data=str(value)+"=>"+self.data
        return self
    
    def addAtEnd(self,value):
        newNode=Node(value)
        self.endPoint.next=newNode
        self.endPoint=newNode
        self.data+="=>"+str(value)
        return self
    
    def Display(self):
        return self.data
            
    def __str__(self):
        return self.data
    def changeToArray(self):
        return self.data.split("=>")   
    
        
e=LinkedList(1).addAtEnd(6).addAtStart(0).add(2).add(3).add(4).add(5) # 0 1 6 2 3 4 5

print(e)

e=e.startPoint
while e is not None:
    print(e.value)
    e = e.next