import unittest
import math
from app.floyd_warshall import get_shortest_distances
from app.invalid_graph_error import InvalidGraphError

class TestFloydWarshall(unittest.TestCase):
    def test_empty_graph(self):
        self.assertEqual([], get_shortest_distances([]))

    def test_graph_with_one_node(self):
        self.assertEqual([[0]], get_shortest_distances([[0]]))

    def test_graph_with_two_nodes_and_one_edge(self):
        graph = [[0, 1],
                 [math.inf, 0]]

        expected_distances = [[0, 1],
                              [math.inf, 0]]

        self.assertEqual(expected_distances, get_shortest_distances(graph))

    def test_graph_with_two_nodes_and_one_edge_mirrored(self):
        graph = [[0, math.inf],
                 [7, 0]]

        expected_distances = [[0, math.inf],
                              [7, 0]]

        self.assertEqual(expected_distances, get_shortest_distances(graph))

    def test_graph_with_two_nodes_and_a_circle(self):
        graph = [[0, 1],
                 [2, 0]]

        expected_distances = [[0, 1],
                              [2, 0]]

        self.assertEqual(expected_distances, get_shortest_distances(graph))

    def test_graph_with_two_nodes_and_no_edges(self):
        graph = [[0, math.inf],
                 [math.inf, 0]]

        expected_distances = [[0, math.inf],
                              [math.inf, 0]]

        self.assertEqual(expected_distances, get_shortest_distances(graph))

    def test_direct_path_is_shortest(self):
        graph = [[0, 1, 1],
                 [math.inf, 0, 1],
                 [math.inf, math.inf, 0]]

        expected_distances = [[0, 1, 1],
                              [math.inf, 0, 1],
                              [math.inf, math.inf, 0]]

        self.assertEqual(expected_distances, get_shortest_distances(graph))

    def test_indirect_path_is_shortest(self):
        graph = [[0, 1, 3],
                 [math.inf, 0, 1],
                 [math.inf, math.inf, 0]]

        expected_distances = [[0, 1, 2],
                              [math.inf, 0, 1],
                              [math.inf, math.inf, 0]]

        self.assertEqual(expected_distances, get_shortest_distances(graph))

    def test_patch_back_to_root(self):
        graph = [[0, 1, 3],
                 [1, 0, 1],
                 [4, 2, 0]]

        expected_distances = [[0, 1, 2],
                              [1, 0, 1],
                              [3, 2, 0]]

        self.assertEqual(expected_distances, get_shortest_distances(graph))

    def test_path_with_two_stops_is_shortest(self):
        graph = [[0, 1, 3, 3],
                 [math.inf, 0, 1, 2],
                 [math.inf, math.inf, 0, 1],
                 [math.inf, math.inf, math.inf, 0]]

        expected_distances = [[0, 1, 2, 3],
                              [math.inf, 0, 1, 2],
                              [math.inf, math.inf, 0, 1],
                              [math.inf, math.inf, math.inf, 0]]

        self.assertEqual(expected_distances, get_shortest_distances(graph))

    def test_path_with_shortcut(self):
        graph = [[0, 1, math.inf, math.inf],
                 [1, 0, 1, math.inf],
                 [math.inf, 2, 0, 1],
                 [math.inf, 1, 5, 0]]

        expected_distances = [[0, 1, 2, 3],
                              [1, 0, 1, 2],
                              [3, 2, 0, 1],
                              [2, 1, 2, 0]]

        self.assertEqual(expected_distances, get_shortest_distances(graph))

    def test_not_in_quadratic_form(self):
        with(self.assertRaisesRegexp(InvalidGraphError, 'The given graph is not in quadratic form.')):
            get_shortest_distances([[0, 2],[1]])

    def test_not_a_number(self):
        with(self.assertRaisesRegexp(InvalidGraphError, 'The given graph contains a non numeric weight.')):
            get_shortest_distances([[0, 'dummy'], [1, 0]])

    def test_negative_number(self):
        with(self.assertRaisesRegexp(InvalidGraphError, 'The given graph contains a negative weight.')):
            get_shortest_distances([[0, -1], [1, 0]])

    def test_vertex_to_self_is_not_zero(self):
        with self.assertRaisesRegexp(InvalidGraphError, 'The given graph contains an edge from a vertex to itself that is not 0.'):
            get_shortest_distances([[1]])
