from data_structures.graph.graph import Graph
from data_structures.graph.get_edge import get_edge, helper, helper2
import pytest

@pytest.fixture
def my_graph():
    graph = Graph()

    pandora = graph.add_node("Pandora")
    metroville = graph.add_node("Metroville")
    arendelle = graph.add_node("Arendelle")
    monstropolis = graph.add_node("Monstropolis")
    narnia = graph.add_node("Narnia")
    naboo = graph.add_node("Naboo")

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(metroville, monstropolis, 105)
    graph.add_edge(arendelle, monstropolis, 42)
    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(naboo, naboo, 250)
    graph.add_edge(monstropolis, naboo, 73)

    return graph

def test_helper():
    graph = Graph()

    pandora = graph.add_node("Pandora")
    metroville = graph.add_node("Metroville")
    arendelle = graph.add_node("Arendelle")
    monstropolis = graph.add_node("Monstropolis")
    narnia = graph.add_node("Narnia")
    naboo = graph.add_node("Naboo")

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(metroville, monstropolis, 105)
    graph.add_edge(arendelle, monstropolis, 42)
    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(naboo, naboo, 250)
    graph.add_edge(monstropolis, naboo, 73)

    vertices_dict = helper(graph.get_nodes())

    assert vertices_dict == {
                            "Pandora": pandora,
                            "Metroville": metroville,
                            "Arendelle": arendelle,
                            "Monstropolis": monstropolis,
                            "Narnia": narnia,
                            "Naboo": naboo
                            }

def test_helper_empty():
    graph = Graph()
    vertices_dict = helper(graph.get_nodes())
    assert vertices_dict == {}

def test_helper2():
    graph = Graph()

    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    d = graph.add_node("d")
    graph.add_edge(a, b, 150)
    graph.add_edge(a, c, 100)
    graph.add_edge(a, d, 50)

    neighbors_dict = helper2(graph.get_neighbors(a))

    assert neighbors_dict == {
                            "b":(b, 150),
                            "c":(c, 100),
                            "d":(d, 50),
                            }

def test_helper2_no_neighbors():

    graph = Graph()

    a = graph.add_node("a")

    neighbors_dict = helper2(graph.get_neighbors(a))

    assert neighbors_dict == {}



def test_two_direct_cities(my_graph):
    graph = my_graph

    assert get_edge(graph, ['Pandora', 'Metroville']) == (True, '$82')

def test_three_direct_cities(my_graph):
    graph = my_graph

    assert get_edge(graph, ['Arendelle', 'Monstropolis', 'Naboo']) == (True, '$115')

def test_two_non_direct_cities(my_graph):
    graph = my_graph

    assert get_edge(graph, ['Naboo', 'Pandora']) == (False, '$0')


def test_three_non_direct_cities(my_graph):
    graph = my_graph

    assert get_edge(graph, ['Narnia', 'Arendelle', 'Naboo']) == (False, '$0')


def test_city_not_in_graph(my_graph):
    graph = my_graph

    assert get_edge(graph, ['Metroville', 'Pandora', 'Kazan']) == (False, '$0')