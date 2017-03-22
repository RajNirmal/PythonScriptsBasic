class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    a = []
    # def display(self,head):
    #     current = head
    #     print("\n\n")
    #     while current:
    #         print(current.data,end=' ')
    #         current = current.next
    def removeDuplicates(self,head):
        #Write your code here
        
        flag = False
        current = head
        #a.append(head.data)
        while current.next is not None:
            #print(str(current.data) +" is the data in this loop")
            for i in self.a:
                # print(*self.a)
                # print(str(current.next.data)+" is the next data and the loop data is "+str(i))
                if(current.next.data is i):
                    # print("The data that is repeated is "+str(i))
                    flag = True
                    break
            if(flag):
                #The data is in the list so remove it 
                self.remove(current);
                print("The data that is being removed is "+str(current.next.data))
                temp = current.next
                nextNode = temp.next
                current.next = temp
                flag = False
            else:
                print("Data not touched")
                flag = False
            current = current.next
            print("Iteration Over\n")
        return head
    def remove ( head):
        temp = head.next
mylist = Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)  
    mylist.a.append(data)  
head=mylist.removeDuplicates(head)
mylist.display(head); 