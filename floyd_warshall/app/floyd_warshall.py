import math
from collections import deque

def get_shortest_distances(graph):
    """
    Return the shortest distance between between every pair of vertices
    of a weighted directed graph (Floyd - Warshall algorithm).
    argument:
    graph -- n * n list forming the adjacency matrix of the graph.
             The weight of an edge is represented by positive values.
             Negative values are invalid. The weight of an edge of a
             vertex to itself must be 0. If there is no edge between
             two vertices, the weight must be set to math.inf. E.g.:

             [[0, 1, 2],
              [3, 0, math.inf],
              [2, 2, 0]]
    result:
    distances -- Matrix containing the distances.
    """
    _validate_graph(graph)
    distances = _calculate_distances(graph)
    return distances

def _validate_graph(graph):
    n = len(graph)
    for i in range(0, n):
        for j in range(0, n):
            _validate_weight(i, j, graph)

def _validate_weight(i, j, graph):
    weight = _get_weight(i, j, graph)
    try:
        if i != j and weight < 0:
            raise InvalidGraphError('The given graph contains a negative weight.')
        if i == j and weight != 0:
            raise InvalidGraphError('The given graph contains an edge from a vertex to itself that is not 0.')
    except TypeError as e:
        raise InvalidGraphError('The given graph contains a non numeric weight.') from e

def _get_weight(i, j, graph):
    try:
        return graph[i][j]
    except IndexError as e:
        raise InvalidGraphError('The given graph is not in quadratic form.') from e

def _calculate_distances(graph):
    n = len(graph)
    distances = [[graph[i][j] for j in range(0, n)] for i in range(0, n)]
    for k in range(0, n):
        for j in range(0, n):
            for i in range(0, n):
                distances[k][j] = min(distances[k][j], distances[k][i] + graph[i][j])
    return distances

class InvalidGraphError(Exception):
    pass
