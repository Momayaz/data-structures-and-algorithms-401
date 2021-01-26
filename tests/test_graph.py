import pytest

from data_structures.graph.graph import Graph, Vertex, Queue

def test_add_node():

    graph = Graph()

    assert graph.add_node('cat').value == 'cat'

def test_size_empty():

    graph = Graph()

    assert graph.size() == 0


def test_size():

    graph = Graph()

    graph.add_node('apple')

    assert graph.size() == 1

    graph.add_node('banana')

    assert graph.size() == 2


def test_edge_start_node_not_in_graph():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_edge_end_node_not_in_graph():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)



def test_add_edge_groovy():

    graph = Graph()

    end = graph.add_node('end')

    start = graph.add_node('start')

    graph.add_edge(start, end)


def test_add_edge_more_nodes():
    graph = Graph()

    a_vertex = graph.add_node('a')

    b_vertex = graph.add_node('b')
    c_vertex = graph.add_node('c')
    d_vertex = graph.add_node('d')

    graph.add_edge(a_vertex, b_vertex, 1)
    graph.add_edge(a_vertex, c_vertex, 2)
    graph.add_edge(a_vertex, d_vertex, 3)

    neighbors = graph.get_neighbors(a_vertex)


    assert neighbors[0][0].value == 'b'
    assert neighbors[0][1] == 1
    assert isinstance(neighbors[0][0], Vertex)
    assert neighbors[1][0].value == 'c'
    assert neighbors[1][1] == 2
    assert isinstance(neighbors[1][0], Vertex)
    assert neighbors[2][0].value == 'd'
    assert neighbors[2][1] == 3
    assert isinstance(neighbors[2][0], Vertex)


def test_add_edge():

    graph = Graph()

    end = graph.add_node('banana')

    start = graph.add_node('apple')

    graph.add_edge(start, end)

    assert graph._adjacency_list[start][0] == (end, 0)
    assert graph.get_neighbors(start) == [(end, 0)]
    graph.add_edge(end, start)
    assert graph.get_neighbors(end) == [(start, 0)]


def test_add_edge_with_weight():

    graph = Graph()

    end = graph.add_node('banana')

    start = graph.add_node('apple')

    graph.add_edge(start, end, 44)

    assert graph.get_neighbors(start) == [(end, 44)]

    graph.add_edge(end, start, 23)

    assert graph.get_neighbors(end) == [(start, 23)]

def test_add_edge_with_weight_letters():

    graph = Graph()

    end = graph.add_node('dog')

    start = graph.add_node('cat')

    graph.add_edge(start, end, "a")

    assert graph.get_neighbors(start) == [(end, "a")]

    graph.add_edge(end, start, "b")

    assert graph.get_neighbors(end) == [(start, "b")]


def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')
    dog = graph.add_node('dog')

    not_in_graph = Vertex('test')

    assert len(graph.get_nodes()) == 3

def test_get_nodes_no_nodes():
    graph = Graph()
    assert len(graph.get_nodes())== 0


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    assert neighbors[0][0].value == 'banana'

    assert isinstance(neighbors[0][0], Vertex)

    assert neighbors[0][1] == 44

def test_get_neighbors_no_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    neighbors = graph.get_neighbors(banana)

    assert len(neighbors) == 0
    assert neighbors == []


def test_breadth_first_empty_graph():
    
    graph = Graph()

    banana = Vertex("banana")
    with pytest.raises(ValueError):
        vertices_lst = graph.breadth_first(banana)


def test_breadth_first_one_element():

    graph = Graph()

    banana = graph.add_node('banana')
    vertices_lst = graph.breadth_first(banana)
    assert vertices_lst == [banana]


def test_breadth_first_regular():

    graph = Graph()

    banana = graph.add_node('banana')
    vertices_lst = graph.breadth_first(banana)

    apple = graph.add_node('apple')
    graph.add_edge(banana, apple)

    vertices_lst = graph.breadth_first(banana)

    assert vertices_lst == [banana, apple]

def test_breadth_first_regular2():
    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    strawberry = graph.add_node('strawberry')
    graph.add_edge(banana, apple)

    graph.add_edge(strawberry, banana)

    vertices_lst = graph.breadth_first(strawberry)
    assert vertices_lst == [strawberry, banana, apple]

def test_breadth_first_different_start_node():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    strawberry = graph.add_node('strawberry')

    graph.add_edge(banana, apple)

    graph.add_edge(strawberry, banana)

    vertices_lst = graph.breadth_first(banana)

    assert vertices_lst == [banana, apple]

def test_breadth_firts_islands_nodes():
    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    strawberry = graph.add_node('strawberry')

    graph.add_edge(banana, apple)

    vertices_lst = graph.breadth_first(banana)

    assert vertices_lst == [banana, apple]

    vertices_lst = graph.breadth_first(apple)

    assert vertices_lst == [apple]


def test_breadth_first_check_visited():
    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    strawberry = graph.add_node('strawberry')

    graph.add_edge(banana, apple)
    graph.add_edge(apple, strawberry)

    vertices_lst = graph.breadth_first(banana)
    assert vertices_lst == [banana, apple, strawberry]

    tomato = graph.add_node('tomato')
    graph.add_edge(apple, tomato)

    vertices_lst = graph.breadth_first(banana)
    assert vertices_lst == [banana, apple, strawberry, tomato]
def test_depth_first():
    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    strawberry = graph.add_node('strawberry')
    tomato = graph.add_node('tomato')

    graph.add_edge(banana, apple)
    graph.add_edge(apple, strawberry)
    graph.add_edge(banana, tomato)
    vertices_lst = graph.depth_first(banana)

    assert vertices_lst == [banana.value, apple.value, strawberry.value, tomato.value]

def test_depth_first_another_case():
    graph = Graph()

    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')

    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(c, e)
    graph.add_edge(e, f)

    vertices_lst = graph.depth_first(a)

    assert vertices_lst == [a.value, b.value, c.value, e.value, f.value, d.value]

def test_depth_first_xhallenge_example():

    graph = Graph()

    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node('h')

    graph.add_edge(a, b)
    graph.add_edge(b, c)
    graph.add_edge(b, d)
    graph.add_edge(c, g)
    graph.add_edge(a, d)
    graph.add_edge(d, e)
    graph.add_edge(d, h)
    graph.add_edge(d, f)

    graph.add_edge(f, h)

    vertices_lst = graph.depth_first(a)

    assert vertices_lst == [a.value, b.value, c.value, g.value, d.value, e.value, h.value, f.value]


def test_deapth_first_empty_graph():

    graph = Graph()

    banana = Vertex("banana")
    with pytest.raises(ValueError):
        vertices_lst = graph.depth_first(banana)

def test_depth_first_given_vertex_not_in_graph():

    graph = Graph()

    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = Vertex('d')

    graph.add_edge(a, b)
    graph.add_edge(b, c)

    with pytest.raises(ValueError):
        vertices_lst = graph.depth_first(d)