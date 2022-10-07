class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, new_node):
        
        new_data = Node(new_node)
        new_data.next = self.head
        self.head = new_data
    
    def insertAtParticularPosition(self, pos, new_node):
        if(pos == 0):
            insertAtBeginning(new_node)
            return
        if(pos > 0):
            new_data = Node(new_node)
            start = self.head
            count = 0
            storePreviousNode = None
            while(count < pos):
                storePreviousNode = start
                start = start.next
                count = count + 1
        
            storePreviousNode.next = new_data
            new_data.next = start
            
    def insertAfter(self, prev_node, new_node):
        if(prev_node):
            new_data = Node(new_node)
            nextNode = prev_node.next
            prev_node.next = new_data
            new_data.next = nextNode
        else:
            return "Previous Node Not Found in the list"
    
    def deleteAtBeginning(self):
        
        if(self.head is None):
            return "linkedlist Empty"
        
        remove_node = self.head
        self.head = self.head.next
        return remove_node.data 
    
    def deleteAtParticularPosition(self, pos):
        if(pos == 0):
            deleteAtBeginning()
            return
        if(pos > 0):
            start = self.head
            count = 0
            while(count < pos):
                storePreviousNode = start
                start = start.next
                count = count + 1
            storePreviousNode.next = start.next
            return start.data
# Iterative Traversal Approach            
    def get_list(self):
        start = self.head
        while(start is not None):
                
            print(start.data,end=" ")
            start = start.next
# Recursive Approach
    def getNodes(self):
    	return self.getNodeCount(self.head)
    
    def getNodeCount(self, node):

        if(node is None):
            return 0
        else:
            return 1 + self.getNodeCount(node.next)
if __name__ == '__main__':
  t = linkedList()  
  t.insertAtBeginning(4)
  t.insertAtBeginning(2)
  t.insertAtParticularPosition(1, 7)
  t.insertAfter(t.head.next, 6)
  t.insertAtParticularPosition(2,0)  
  print(t.deleteAtBeginning())
  print(t.deleteAtParticularPosition(1))
  
  t.get_list()
  val = t.getNodes()
  print(f"Total Nodes {val}")
