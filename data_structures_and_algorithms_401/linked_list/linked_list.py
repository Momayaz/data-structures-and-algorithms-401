# class Node:
class Node:
    """ Class for the Node instances"""

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """ Class for the LInkedLists instances"""

    def __init__(self):
        """method to iniate a LinkedList"""

        self.head = None

    def insert(self, value):
        """method to insert new node to the beginnig of the list"""

        node = Node(value)
        node.next = self.head
        self.head = node
    
    def includes(self,value):
        """
        method to check if the given value in the liked list
        """
        
        if self.head==None:
            return False
        else:
            current=self.head
            while current:
                if current.value==value:
                    return True
                else :
                    current=current.next    
            return False

    def __str__(self):
        """method that returns a string that represents all list elements"""

        list_str = ''
        current = self.head
        while current:
            # print(current, "current")
            list_str +='{ '+ str(current.value ) + ' } -> '
            current = current.next

        list_str +='{ '+ 'none' + ' }'
        return list_str


    def append(self,value):
        """
        add a vlaue for the first of 
        """
        value !=None
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curent = self.head
            while curent.next:
                curent = curent.next
            curent.next = new_node


    def insertAfter(self, value, newVal):
        """
        in this method your value and any exist value then it will add your value after the choosen value
        """
        current = self.head
        print(current.next)
        while current is not None:
            if current.value == value:
                break
            current = current.next
        if current is None:
            print("Exception: the value not exisit in the linked list")
        else:
            new_node = Node(newVal)
            new_node.next = current.next
            current.next = new_node 


    def insertBefore(self, value, newVal):
        """
        in this method your value and any exist value then it will add your value before the choosen value
        """
        if self.head is None:
            print("List has no element")
            return
        if value == self.head.value:
            new_node = Node(newVal)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                break
            current = current.next
        if current.next is None:
            print("Exception: the value not exisit in the linked list")
        else:
            new_node = Node(newVal)
            new_node.next = current.next
            current.next = new_node  
    
    def length_ll(self):
        """method to get lenght of the list"""
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length  
    
    def kthFromEnd(self, k):
        try:
            length = -1
            current = self.head
            while current:
                current = current.next
                length = length + 1
            if length >= k:
                current = self.head
                for i in range(length - k):
                    current = current.next
            return current.value
        except:
            return "value not found"    



def zip_Lists(list1, list2):
    """
    zip_lists function which takes two linked lists as arguments. Zips them together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
    """

    current1 = list1.head
    current2 = list2.head

    if current1 == None and current2 == None:
        raise Exception("lists are empty")

    if not current1:
        list1.head = list2.head
        return list1.head

    if not current2:
        return list1.head

    temp = current2.next

    while current1.next and current2.next:
        current1.next, current2.next = current2, current1.next
        current1 = current2.next
        current2, temp = temp, temp.next

    if not current1.next:
        current1.next = current2
        return list1.head

    if not current2.next:
        current1.next, current2.next = current2, current1.next
        return list1.head



def create_list_insert(vals):
    """helper function to create list with given values, used in test module"""
    my_list = LinkedList()
    for i in vals:
        my_list.insert(i)
    return my_list
    
def create_list_append(vals):
    """helper function to create list with given values, used in test module"""
    my_list = LinkedList()
    for i in vals:
        my_list.append(i)
    return my_list


if __name__ == "__main__":

    l_list1 = create_list_append(['a','b','c','d','e'])
    print(l_list1.length_ll())
    # l_list2 = create_list_append(['f','g','h','i','j'])
    # ref_to_head = zip_Lists(l_list1, l_list2)
    # print(l_list1)
    # print(ref_to_head.value)
    # l_list11 = create_list_append([1,3,5,7.9])
    # l_list22 = create_list_append([2,4,6,8,10])
    # ref_to_head2 = zip_Lists(l_list11, l_list22)
    # print(l_list11)
    # print(ref_to_head2.value)
    # create_list_insert([1,2,3,4,5])
    # print(create_list_insert([1,2,3,4,5]).__str__())
    # print(create_list_insert([1,2,3,4,5]).includes(4))