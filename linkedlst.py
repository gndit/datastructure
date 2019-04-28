
#insertion of node in linked list
#insert in between insert in begning insert at the end
class NODE:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None
#function for node insertion in begning
    def push(self,new_data):
        new_node=NODE(new_data)
        new_node.next=self.head
        self.head=new_node

#insert in between
    def insertAfternode(self,prenode,new_data):
        if prenode is None:
            print("node must in linked list")
            return

        new_node=NODE(new_data)
        new_node.next=prenode.next
        prenode.next=new_node

#insert at the end
    def append(self,new_data):

        new_node=NODE(new_data)

        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next

        last.next=new_node

#function for print the data
    def PrintList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
#main function for executing this program
if __name__ == "__main__":
    llist = Linked_List()
    llist.append(7)
    llist.append(8)
    llist.push(2)
    llist.insertAfternode(llist.head.next,3)
    llist.append(9)
    llist.push(5)
    llist.insertAfternode(llist.head.next, 90)
    print("created list is\n")
    llist.PrintList()





