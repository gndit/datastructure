#python progame to reverse a linked list
class NODE:
    def __init__(self,data):
        self.data=data
        self.next=None
class LINKED:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        temp=self.head
        while (temp is not None):
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        self.head=prev
    def push(self,new_data):
        new_node=NODE(new_data)
        new_node.next=self.head
        self.head=new_node

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
if __name__=='__main__':
    lst=LINKED()
    print("before reverse list look like this-->")
    lst.push(3)
    lst.push(9)
    lst.push(8)
    print(lst.print())
    print(" after reverse list look like this-->")

    lst.reverse()

    print(lst.print())

