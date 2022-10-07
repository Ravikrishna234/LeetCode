
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_node):
        new_data = Node(new_node)
        new_data.next = self.head 
        self.head = new_data

    def pick(self):
        if(self.head is None):
            return "Stack Empty"
        pop_data = self.head
        self.head = self.head.next
        return pop_data.data
        
if __name__ == '__main__':
  t = LinkedList()
  t.push(3)
  t.push(2)
  t.push(1)
  print(t.pick())
  print(t.pick())

