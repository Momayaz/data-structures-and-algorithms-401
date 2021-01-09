
from data_structures_and_algorithms_401.hash_table.hash_table import HashTable, LinkedList, _Node

import pytest

@pytest.fixture
def my_hash_table():
    hash_table = HashTable()

    # add first key-value pair on the index 808
    hash_table.add("Cat", "Frodo")
    hash_table.add("Dog", "Sam")
    hash_table.add("goD", "Zeus")
    hash_table.add("ogD", "test test")
    hash_table.add("NewKey", "new value")
    hash_table.add(12, "int key")
    hash_table.add(0.57, "float key")

    return hash_table

def test_create_hash_table_20_element():

    hash_table = HashTable(20)

    assert hash_table._array == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_create_hash_table_3_elements():

    hash_table = HashTable(3)

    assert hash_table._array == [0, 0, 0]


def test_hash_method():
    hash_table = HashTable()

    assert hash_table.hash('Cat') == 808

    assert hash_table.hash('FRODO234') == 629

    assert hash_table.hash(1294) == 688

    assert hash_table.hash("House") == 860

def test_add_method():
    hash_table = HashTable()

    # add first key-value pair
    hash_table.add("Cat", "Frodo")
    # check if index that not 808 still has '0' in it
    assert hash_table._array[809] == 0

    # check if index 808 not '0' anymore
    assert hash_table._array[808] != 0

    assert hash_table._array[808].head.key == "Cat"
    assert hash_table._array[808].head.value == "Frodo"
    assert hash_table._array[808].head.next ==  None

def test_add_collision(my_hash_table):
    hash_table = my_hash_table
    hash_table.add("aCt", "Marsik")
    assert hash_table._array[808].head.key == "aCt"
    assert hash_table._array[808].head.value == "Marsik"
    assert hash_table._array[808].head.next.key == "Cat"
    assert hash_table._array[808].head.next.value == "Frodo"
    assert hash_table._array[808].head.next.next == None

def test_add_collision_same_key(my_hash_table):
    hash_table = my_hash_table
    hash_table.add("aCt", "Marsik")
    assert hash_table._array[808].head.key == "aCt"
    assert hash_table._array[808].head.value == "Marsik"
    assert hash_table._array[808].head.next.key == "Cat"
    assert hash_table._array[808].head.next.value == "Frodo"
    assert hash_table._array[808].head.next.next == None

def test_get_method_with_collisions(my_hash_table):
    hash_table = my_hash_table
    assert hash_table.get("Dog") == "Sam"
    assert hash_table.get("goD") == "Zeus"
    assert hash_table.get("ogD") == "test test"
    assert hash_table.get("NewKey") == "new value"
    assert hash_table.get(12) == "int key"
    assert hash_table.get(0.57) == "float key"
    assert hash_table.get("aCt") == None
    assert hash_table.get("Alice") == None

def test_contains_method_true(my_hash_table):
    hash_table = my_hash_table
    assert hash_table.contains("Dog") == True
    assert hash_table.contains("goD") == True
    assert hash_table.contains("ogD") == True
    assert hash_table.contains("NewKey") == True
    assert hash_table.contains(12) == True
    assert hash_table.contains(0.57) == True

def test_contains_method_false(my_hash_table):
    hash_table = my_hash_table
    assert hash_table.contains("Alice") == False
    assert hash_table.contains("Wonderland") == False