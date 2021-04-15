from AdjacencyMatrix import AdjacencyMatrix
from AdjacencyList import AdjacencyList
from CSR import CSR
import numpy
import math


class Metrices:

    def __init__(self):
        pass

    def no_neighbors_function(self,adj):
        no_neighbors = []  # pinakas opou gia ka8e komvo exei row me osous komvous DEN syndeetai

        for i in adj.vertex_set():
            no_neighbors.append([v for v in adj.key_list if v not in adj.neighbors(i)])

        return(no_neighbors)


    def pairs_function(self,adj,no_neighbors):
        vertex_neighbors = []  # pinakas opou gia ka8e komvo, tous geitones tou
        pairs_array = []  # pinakas me zeygarakia pou den syndeontai

        for v1 in range(len(no_neighbors)):
            vertex_neighbors.append(adj.neighbors(v1))
            for v2 in no_neighbors[v1]:
                if (v1 != v2):  # den vazoume ayta pou einai idia dhl 0,0 1,1, 2,2....
                    pairs_array.append((v1, v2))

        pairs_array = {tuple(sorted(item)) for item in pairs_array}
        return pairs_array,vertex_neighbors


    def common_neighbors(self, adj, k):
        no_neighbors=self.no_neighbors_function(adj)
        pairs_array,vertex_neighbors=self.pairs_function(adj,no_neighbors)
        total = []

        pairs_array = {tuple(sorted(item)) for item in pairs_array}
        for j in pairs_array:
            score = len(set(vertex_neighbors[j[0]]) & set(vertex_neighbors[j[1]]))
            total.append((j[0], j[1], score))

        sorted_total = sorted(total, reverse=True, key=lambda tup: tup[2])
        return sorted_total[:k]

    def jaccard_coefficient(self, adj, k):
        no_neighbors=self.no_neighbors_function(adj)
        pairs_array,vertex_neighbors=self.pairs_function(adj,no_neighbors)
        total = []

        pairs_array = {tuple(sorted(item)) for item in pairs_array}
        for j in pairs_array:
            score = len(
                set(vertex_neighbors[j[0]]) & set(vertex_neighbors[j[1]])) / float(
                len(set(vertex_neighbors[j[0]]) | set(vertex_neighbors[j[1]])))
            total.append((j[0], j[1], score))

        sorted_total = sorted(total, reverse=True, key=lambda tup: tup[2])
        return sorted_total[:k]

    def adamic(self, adj, k):
        no_neighbors=self.no_neighbors_function(adj)
        pairs_array,vertex_neighbors=self.pairs_function(adj,no_neighbors)
        total = []

        for j in pairs_array:
            z = numpy.intersect1d(adj.neighbors(j[0]), adj.neighbors(j[1]))
            if len(z) > 0:
                score = 0
                for p in z:
                    score += 1 / math.log(adj.degree(p))
            else:
                score = 0

            total.append((j[0], j[1], score))

        sorted_total = sorted(total, reverse=True, key=lambda tup: tup[2])
        return sorted_total[:k]

