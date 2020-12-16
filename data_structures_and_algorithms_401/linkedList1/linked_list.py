

class LinkedList:

    def __init__(self):
        self.head=None


    def insert(self,data):
        """
         Takes any value as an argument and adds a new node with that value to the head of the list.
         Arguments:
            a value to be added to the list
        """
        try:
            node = Node(data)
            if self.head ==None:
                self.head=node
            else:
                node.next= self.head
                self.head=node
        except Exception as error:
            print(f'this is error in this method {error}')




    def includes(self,data):
        """
         method which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node's value somewhere within the list.
         Arguments:
            a value to search for
        """
        try:
            current = self.head
            while current !=None:
                if current.value ==data:
                    return True
                else:
                    current=current.next
            return False
        except Exception as error:
            print(f'this is error in this method {error}')


    def append(self,value):
        """
           Takes any value as an argument and adds a new node with that value to the end of the list.
           Arguments:
               a value to be added to the list
        """
        try:
            node =Node(value)
            if self.head ==None:
                self.head=node
            else:
                current = self.head
                while current.next !=None:
                    current=current.next
                current.next=node
        except Exception as error:
            print(f'this is error in this method {error}')


    def insert_before(self,value, newVal):


        try:
            node =Node(newVal)
            if not self.head:
                self.head = node
            else:
                # To add before the first node
                if self.head.value == value:
                        swap = self.head
                        self.head = node
                        node.next = swap
                        return
                else:

                    current = self.head
                    while current.next != None:
                        if current.next.value == value:
                            swap = current.next
                            current.next = node
                            node.next = swap
                            return
                        else:
                            current = current.next

                    return "this node doesn't exist!"
        except Exception as error:
            print(f'this is error in this method {error}')



    def insert_after(self,value, newVal):
        try:
            node=Node(newVal)
            if self.head ==None:
                self.head=node
            else:
                current = self.head
                while current:
                    if current.value == value:
                        node.next = current.next
                        current.next = node

                        break

                    else:
                        current = current.next

                return "this node doesn't exist!"
        except Exception as error:
            print(f'this is error in this method {error}')



    def kth_from_end(self, k):


        try:


            counter = -1
            current = self.head
            while current:
                current = current.next
                counter = counter + 1
            if counter >= k:
                current = self.head
                for i in range(counter - k):
                    current = current.next
                return current.value
            else:
                return 'The Value Not Found'

        except:
            return "The Value Not Found"













    def __str__(self):
        """
         method which takes in no arguments and returns a string representing all the values in the Linked List,
          output =
           "{ a } -> { b } -> { c } -> NULL"
        """
        try:
            string =''
            current = self.head
            while current!=None:
                string+=f'{{ {current.value} }} -> '
                current=current.next
                if current == None:
                    string+= 'NULL'
            return string
        except Exception as error:
            print(f'this is error in this method {error}')

