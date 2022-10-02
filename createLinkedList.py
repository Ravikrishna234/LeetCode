class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
  
        new_node.next = self.head
        self.head = new_node
        
    def insertAfter(self, prev_node, new_node):
        if(prev_node is not None):
            new_node = Node(new_node)
            new_node.next = prev_node.next
            prev_node.next = new_node
        else:
            return
    
    def append(self, new_data):
        new_node = Node(new_data)
        if(self.head is None):
            self.head = new_node
        else:

            last = self.head
            while(last.next):
                last = last.next
            last.next = new_node
    
    def getAllElements(self):
        
        start = self.head
        while(start):
          print(start.data,end=" ")
          start = start.next
          
if __name__ == '__main__':
    
    lst = LinkedList()
    lst.append(12)
    lst.push(3)
    lst.append(3)

    lst.insertAfter(lst.head.next, 5)
    lst.getAllElements()
        
