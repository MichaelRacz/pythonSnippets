from app.invalid_graph_error import InvalidGraphError

def validate_graph(graph):
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
