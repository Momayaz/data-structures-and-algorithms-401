from linked_list import LinkedList

def zipLists(myList, other):
    if(other.head != None):
        current_self = myList.head
        current_other = other.head
        while (current_self):
            myList.insertAfter(current_self.value, current_other.value)
            current_self = current_self.next.next
            current_other = current_other.next
            if current_other == None:
                break
        while(current_other):
            myList.append(current_other.value)
            current_other = current_other.next

if __name__ == "__main__":
    myList = LinkedList()
    otherList = LinkedList()

    myList.append(0)
    myList.insert(5)
    myList.insert(3)
    myList.insert(1)
    print(myList)
    otherList.append(2)
    otherList.insert(4)
    otherList.insert(6)
    otherList.insert(8)
    print(otherList)
    zipLists(myList, otherList)
    print("Zip Output: ", myList)