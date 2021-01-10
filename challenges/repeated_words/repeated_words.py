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


def length(string):
    star_len = 1
    while True:
        try:
            string[star_len]
        except IndexError:
            break
        else:
            star_len += 1
            continue
    return star_len

###################################################################################################
""" Here is the code challenge for today, coz i faced some problems related to import the linked list"""

def repeated_word(paragraph):
    words = LinkedList()
    word = ''
    count = 0
    for i in paragraph:
        count +=1
        if count == length(paragraph): # for length it is a function i built it 
            words.append(word)
        elif i ==',' or i =='.':
            continue
        elif i == ' ' or i == ',':
            if words.includes(word):
                return word
            words.append(word)
            word=''
            continue
        else:
            word += i.lower()
        
    return 'there is no repeated word in this paragraph'




if __name__ == '__main__':
    test1 = "Once upon a time, there was a brave princess who..."
    assert repeated_word(test1) == 'a'
    print('all tests is passed !!!')