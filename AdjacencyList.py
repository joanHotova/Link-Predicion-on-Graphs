import numpy

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node;


class AdjacencyList:
    def __init__(self, key_list, val_list, edges):
        self.nodes = numpy.array(key_list)
        self.total_nodes = len(self.nodes)
        self.total_edges = len(edges)
        self.key_list = key_list

        self.array_of_lists = numpy.empty((self.total_nodes,), dtype=object)

        for i in range(self.total_nodes):
            self.array_of_lists[i] = LinkedList()

        for i in edges:
            u = i[0]
            v = i[1]

            self.array_of_lists[u].insert_at_end(v)
            self.array_of_lists[v].insert_at_end(u)

    def contains_vertex(self, v):
        return v >= 0 and v < len(self.array_of_lists) and self.array_of_lists[v] != None

    def contains_edge(self, u, v):
        if v >= 0 and v < len(self.array_of_lists) and self.array_of_lists[v] != None and u >= 0 and u < len(
                self.array_of_lists) and self.array_of_lists[u] != None:
            if self.array_of_lists[u].head is not None:
                n = self.array_of_lists[u].head
                while n is not None:
                    if n.data == v:
                        return True
                    n = n.next
                return False
        else:
            return False

    def num_vertices(self):
        return self.total_nodes

    def num_edges(self):
        return self.total_edges

    def vertex_set(self):
        return self.nodes

    def neighbors(self, v):
        a = []
        counter = 0
        if v >= 0 and v < len(self.array_of_lists) and self.array_of_lists[v] != None:
            node = self.array_of_lists[v].head
            while node is not None:
                a.insert(counter, node.data, )
                counter += 1
                node = node.next
            return a

    def degree(self, v):
        counter = 0
        if v >= 0 and v < len(self.array_of_lists) and self.array_of_lists[v] != None:
            node = self.array_of_lists[v].head
            while node is not None:
                counter += 1
                node = node.next
        return counter