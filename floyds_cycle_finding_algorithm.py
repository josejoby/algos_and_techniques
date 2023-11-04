"""
### ****Floyd’s Cycle-Finding Algorithm ****

- to find if a linked list has loop
- two pointers - fast and slow
    - both fast and slow pointers will start from the same node.
    - Fast pointer will jump 2 nodes and slow pointer will move to next node
    - if there is a cycle, fast pointer will eventually meet the slow pointer.
    - Check this until fast pointer has next element or fast pointer meets slow pointer.
"""


class Node:
    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data

class LinkedList:

    def __init__(self) -> None:
        self.head_node = None
    
    def get_head(self):
        return self.head_node
    
    def insert_node(self, node) -> None:
        if self.head_node is None:
            self.head_node = node
        else:
            curr_node = self.head_node
            while curr_node.next_node:
                curr_node = curr_node.next_node
            curr_node.next_node = node
        return

# Floyd's Cycle Finding Algorithm
def detect_loop(lst):
    # Keep two iterators
    onestep = lst.get_head()
    twostep = lst.get_head()
    while onestep and twostep and twostep.next_node:
        onestep = onestep.next_node  # Moves one node at a time
        twostep = twostep.next_node.next_node  # Skips a node
        if onestep == twostep:  # Loop exists
            return True
    return False

if __name__ == "__main__":
    data = [21, 14, 7]
    lst = LinkedList()
    for x in data:
        lst.insert_node(Node(x))

    # check for loop/cycle
    print(detect_loop(lst)) #false

    # creating a loop/cycle
    node = lst.get_head()
    while node.next_node is not None: # finding the last node
        node = node.next_node
    node.next_node = lst.get_head().next_node

    # check for loop/cycle
    print(detect_loop(lst)) #true