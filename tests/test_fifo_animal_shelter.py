from data_structures_and_algorithms_401.fifo_animal_shelter.fifo_animal_shelter import Node, Queue, AnimalShelter

"""
Test Cases:
    1. Creating a shelter instance.
    2. Enqueue one Animal into the shelter.
    3. Enqueue multiple Animals into the shelter.
    4. Return None when enqueueing not dog or cat into the shelter.
    5. Dequeue a preferred animal from the shelter.
    6. Refuse dequeuing from an empty shelter.
"""

def test_new_shelter():
    shelter = AnimalShelter()
    assert shelter.front == None
    assert shelter.rear == None

def test_shelter_enqueue_one():
    shelter = AnimalShelter()
    shelter.shelter_enqueue('cat')
    assert shelter.front.value == 'cat'

def test_shelter_enqueue_multiple():
    shelter = AnimalShelter()
    shelter.shelter_enqueue('cat')
    shelter.shelter_enqueue('dog')
    assert shelter.front.value == 'cat'
    assert shelter.front.next.value == 'dog'

def test_shelter_enqueue_not_cat_not_dog():
    shelter = AnimalShelter()
    assert shelter.shelter_enqueue(Node('notWhoYouAreLookingFor')) == None

def test_shelter_dequeue():
    shelter = AnimalShelter()
    shelter.shelter_enqueue("cat")
    shelter.shelter_enqueue("cat")
    shelter.shelter_enqueue("dog")
    shelter.shelter_enqueue("cat")
    dequeued = shelter.shelter_dequeue('dog')
    assert dequeued == 'dog'
 
def test_shelter_dequeue_empty():
    shelter = AnimalShelter()
    dequeued = shelter.shelter_dequeue('dog')
    assert dequeued == None
