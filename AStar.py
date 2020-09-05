from operator import attrgetter
from typing import List

from node import Node


class AStar:
    Node.create_graph()

    @staticmethod
    def get_shortest_path():
        Node.create_graph()
        open_list = []
        closed_list = []

        start_node = Node.graph[0]
        start_node.f_score = 0

        open_list.append(start_node)

        while len(open_list) > 0:
            current_node = min(open_list, key=attrgetter('f_score'))
            open_list.remove(current_node)
            closed_list.append(current_node)

            if current_node.h_score == 0:
                AStar.print_path(current_node)

            children = current_node.neighbors

            for child in children:
                if child in closed_list:
                    continue

                child[0].g_score = current_node.g_score + child[1]
                child[0].f_score = child[0].g_score + child[0].h_score

                if (node_index := AStar.in_list(open_list, child[0])) != -1:
                    if child[0].g_score >= open_list[node_index].g_score:
                        continue

                child[0].parent = current_node
                open_list.append(child[0])

    @staticmethod
    def print_path(current_node):
        if current_node.parent is None:
            print(current_node.name)
            return

        AStar.print_path(current_node.parent)
        print(current_node.name)
        return

    @staticmethod
    def in_list(node_list: List[Node], current_node: Node):
        """
        Check if node exists in a node list
        :return: index of node in list if it exists, -1 if it does not
        """
        for index, node in enumerate(node_list):
            if node.name == current_node.name:
                return index

        return -1
