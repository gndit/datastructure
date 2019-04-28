class NODE:
    def __init__(self,data):
        self.data=data
        self.head=None

class LINKED:
    def __init__(self):
        self.head=None

    def push(self,newdata):
        newnode=NODE(newdata)
        newnode.next=self.head
        self.head=newnode

    def delte(self,key):
        temp=self.head
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

            # Search for the key to be deleted, keep track of the
            # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

            # if key was not present in linked list
        if (temp == None):
            return

            # Unlink the node from linked list
        prev.next = temp.next

        temp = None


    def printlist(self):
            temp=self.head
            while(temp):
                print(temp.data)
                temp=temp.next
if __name__=="__main__":
    llist=LINKED()
    llist.push(2)
    llist.push(8)
    llist.push(5)
    llist.push(9)
    llist.delte(5)
    llist.printlist()





