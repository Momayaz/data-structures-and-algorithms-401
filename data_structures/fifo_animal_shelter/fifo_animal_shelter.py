
"""********************************************************************************"""
"""NOTE: repeated the Queue and Node classes because I have an issue with importing"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

############################################

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)

        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):
        if self.front == None:
            raise AttributeError("Queue is empty")
        dequeued = self.front.value
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        return(dequeued)

    def peek(self):
        if self.front == None:
            raise AttributeError("Queue is empty")
        return self.front.value

    def isEmpty(self):
        if self.rear:
            return False
        return True

    def __str__(self):
        queue_str = ""
        if self.front:
            current = self.front
            while(current):
                queue_str += f"{ current.value } <- "
                current = current.next
        queue_str += "NULL"
        return (queue_str)
                
"""NOTE: repeated the Queue and Node classes because I have an issue with importing"""
"""********************************************************************************"""
class AnimalShelter(Queue):
    def __init__(self):
        self.front = None
        self.rear = None

    def shelter_enqueue(self, animal): 
        if animal == 'dog' or animal == 'cat':
            self.enqueue(animal)
        else:
            return None

    def shelter_dequeue(self, pref): 
        if self.rear == None:
            return None
        if (pref == "dog" or pref == 'cat'):
            to_dequeue = self.front 

            while (to_dequeue.next != None and to_dequeue.next.value != pref): 
                to_dequeue = to_dequeue.next
                
            if to_dequeue.next == None: 
                return None
            else: 
                dequeued = to_dequeue.next
                to_dequeue.next = to_dequeue.next.next
                return dequeued.value   
        else:
            return None


############################################

if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.shelter_enqueue('dog')
    shelter.shelter_enqueue('cat')
    shelter.shelter_enqueue('dog')
    shelter.shelter_enqueue('cat')
    print(shelter.shelter_dequeue("cat"))