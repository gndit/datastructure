class NODE:
    def __init__(self,data):
        self.data=data
        self.head=None
class LLIST:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=NODE(new_data)
        new_node.next=self.head
        self.head=new_node


# This function counts number of nodes in Linked List
# iteratively, given 'node' as starting node.
    def getCount(self):

        temp = self.head  # Initialise temp
        count = 0  # Initialise count

    # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

if __name__=='__main__':
    llist=LLIST()
    llist.push(2)
    llist.push(7)
    llist.push(4)
    llist.push(4)
    llist.push(9)
    print('count of nodes is-->')
    print( llist.getCount())
