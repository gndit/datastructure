#search a item in linked list
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

    def search(self,key):
        temp=self.head
        while(temp!=None):
            if temp.data==key:
                return True
            temp=temp.next
        return False
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
if __name__=='__main__':
    llist=LLIST()
    llist.push(2)
    llist.push(7)
    llist.push(4)
    llist.push(6)
    llist.push(9)
    if llist.search(23):
        print("yes")
    else:
        print("no")
    print("list is look like this:")
    llist.print()

