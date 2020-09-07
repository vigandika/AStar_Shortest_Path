class Node:
    graph = []

    def __init__(self, name, h_score, g_score=None):
        self.name = name
        self.h_score = h_score
        self.g_score = g_score
        self.f_score = None
        self.neighbors = []
        self.parent = None

    def add_neighbour(self, node, distance):
        self.neighbors.append([node, distance])

    @staticmethod
    def create_graph():
        start_node = Node('S', 17, 0)

        a_node = Node('A', 10)
        b_node = Node('B', 13)
        c_node = Node('C', 4)

        start_node.add_neighbour(Node('A', 10), 6)
        start_node.add_neighbour(Node('B', 13), 5)
        start_node.add_neighbour(Node('C', 4), 10)

        e_node = Node('E', 4)
        d_node = Node('D', 2)

        a_node.add_neighbour(Node('E', 4), 6)
        b_node.add_neighbour(Node('E', 4), 6)
        b_node.add_neighbour(Node('D', 2), 7)
        c_node.add_neighbour(Node('D', 2), 6)

        f_node = Node('F', 1)

        e_node.add_neighbour(Node('F', 1), 4)
        d_node.add_neighbour(Node('F', 1), 6)

        g_node = Node('G', 0)

        f_node.add_neighbour(Node('G', 0), 3)

        Node.graph.extend([start_node, a_node, b_node, c_node, d_node, e_node, f_node, g_node])
