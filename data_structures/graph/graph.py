from stacks_and_queues import Queue, Node, Stack

class Graph:
    """Class to implement Graph object with the given methods"""

    def __init__(self):

        self._adjacency_list = {}


    def add_node(self, value):
        """
        Adds a new vertex to the graph
        Input: the value of that vertex
        Output: the added vertex
        """
        vertex = Vertex(value)

        self._adjacency_list[vertex] = []

        return vertex


    def size(self):
        """Returns the total number of nodes in the graph"""
        return len(self._adjacency_list)


    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Adds a new edge between two nodes in the graph with ability to add weight
        Input: two vertexes to be connected by the edge
        *Both nodes should already be in the Graph
        """

        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in Graph')

        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in Graph')

        adjacencies = self._adjacency_list[start_vertex]

        adjacencies.append((end_vertex,weight))


    def get_nodes(self):
        """Returns all of the nodes in the graph as a collection"""
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """
        Returns a collection of vertexes connected to the given vertex with the weights of their connections
        Input: Takes in a given vertex
        """

        return self._adjacency_list[vertex]

    def breadth_first(self, starting_vertex):
        """
        Method to do breadth-first traversal on a graph.
        Input: starting vertex
        Output: list of vertices in the breadth-first order
        """
        vertices = []
        breadth = Queue()

        if starting_vertex not in self._adjacency_list:
            raise ValueError

        breadth.enqueue(starting_vertex)

        while not breadth.is_empty():
            front = breadth.dequeue()
            vertices.append(front)

            for neighbor in self.get_neighbors(front):
                if not neighbor[0].visited:
                    neighbor[0].visited = True
                    breadth.enqueue(neighbor[0])

        for node in self._adjacency_list:
            node.visited = False

        return vertices

    def depth_first(self, starting_vertex):
        """
        Method to do depth-first traversal on a graph.
        Input: starting vertex
        Output: list of vertices in the depth-first order
        """

        vertices = []
        depth = Stack()

        if starting_vertex not in self._adjacency_list:
            raise ValueError
        
        depth.push(starting_vertex)

        while not depth.is_empty():
           top_vertex = depth.pop()
           vertices.append(top_vertex.value)
           top_node_neighbors = self.get_neighbors(top_vertex)

           for neighbor in top_node_neighbors[::-1]:
               if not neighbor[0].visited:
                   top_vertex.visited = True
                   neighbor[0].visited = True

                   depth.push(neighbor[0])

        for node in self._adjacency_list:
            node.visited = False

        return vertices



class Vertex:
    """Class to create Vertex with the given value"""
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.next = None