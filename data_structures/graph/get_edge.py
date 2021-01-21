from graph import Graph

def helper(lst_nodes):
    """Helper function to convert list of nodes to dictionary with string type keys"""
    dict_nodes = {}
    for node in lst_nodes:
        dict_nodes[node.value] = node
    return dict_nodes

def helper2(lst_nodes):
    """Helper function to convert given list of neighbor nodes to dictionary with string type keys"""
    neighbors = {}
    for node in lst_nodes:
        neighbors[node[0].value] = node
    return neighbors

def get_edge(graph, arr):
    """Function that takes in graph which represent possble trips between cities and their costs and array of city names. Returns True or False based on whether the full trip is possible with direct flights, and how much it would cost."""


    dict_nodes = helper(graph.get_nodes())
    trip_price = 0

    for i in range (0, len(arr)-1):

        if arr[i] not in dict_nodes:
            return False, '$0'

        if arr[i] in dict_nodes:
            neighbors_dict = helper2(graph.get_neighbors(dict_nodes[arr[i]]))

            if arr[i+1] in neighbors_dict:
                trip_price += neighbors_dict[arr[i+1]][1]

            else:
                return False, '$0'


    return True, f'${trip_price}'