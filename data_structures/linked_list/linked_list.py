
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else: 
            node.next = self.head
            self.head = node
        
    def includes(self, data):
        current = self.head
        while (current != None):
            if current.value == data:
                return True
            else:
                current = current.next
        return False
            
    def __str__(self):
        if self.head == None:
            return ("NULL")
        else:
            list = ""
            current = self.head
            while (current != None):
                list += '{ %s } -> ' %current.value
                current = current.next
            list += 'NULL'
            return (f"{list}")

    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else: 
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = node

    def insertBefore(self, value, newVal):
        if (self.includes(value) == False):
            print('Value does not exist.')
        else:
            node = Node(newVal)
            if (self.head.value == value):
                return(self.insert(newVal))
            current = self.head
            while(current.next.value != value):
                current = current.next
            node.next = current.next
            current.next = node

    def insertAfter(self, value, newVal):
        if (self.includes(value) == False):
            print('Value does not exist.')
        else:
            node = Node(newVal)
            current = self.head
            while(current.value != value):
                current = current.next
            node.next = current.next
            current.next = node

    def deleteValue(self, value):
        if (self.includes(value) == False):
            print('Value does not exist.')
        else:
            current = self.head
            while(current.next.value != value):
                current = current.next
            current.next = current.next.next

    def getLength(self): 
        current = self.head 
        count = 0 
        while (current): 
            count += 1
            current = current.next
        return count 

    def get_kth_value(self, k):
        list_length = self.getLength()
        if type(k) != int or k < 0:
            raise TypeError("The parameter must be a positive integer")
        elif list_length == 0:
            raise Exception("Linked List is empty.")
        elif k > list_length-1:
            raise IndexError("Index out of range")
        else:
            value_index = (list_length-1) - k
            counter = 0
            current = self.head
            while(current):
                if counter == value_index:
                    return(current.value)
                counter += 1
                current = current.next

    def zipLists(self, other):
        if(other.head != None):
            current_self = self.head
            current_other = other.head
            while (current_self):
                    self.insertAfter(current_self.value, current_other.value)
                    current_self = current_self.next.next
                    current_other = current_other.next
                    if current_other == None:
                        break
            while(current_other):
                self.append(current_other.value)
                current_other = current_other.next

    def reverseList(self):
        new_head = None
        current = self.head
        while(current != None):
            next = current.next
            current.next = new_head
            new_head = current
            current = next
        self.head = new_head

            


####################################################
if __name__ == "__main__":
    myList = LinkedList()
    myList.append(0)
    myList.insert(5)
    myList.insert(3)
    myList.insert(1)
    print(myList)
    myList.reverseList()
    print(myList)






  


    
