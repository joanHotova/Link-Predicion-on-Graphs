class CSR:
    def __init__(self, key_list):
      self.key_list = key_list
      lengthoflist= len(key_list)
      self.matrix = []
      for i in range(lengthoflist):
          self.matrix.append([0 for i in range(lengthoflist)])
      self.lengthoflist = lengthoflist

    def fill_matrix(self, v1, v2):
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1

    def csr_arrays(self):
        self.row = []
        self.column = []
        self.value = []
        for r in range(self.lengthoflist):
            for c in range(self.lengthoflist):
                if self.matrix[r][c] == 1:
                    #self.row.append(r)
                    self.column.append(c)
                    self.value.append(1)
        self.row.insert(0,0)
        s=0
        for i in (self.matrix):
            s = s+sum(i)
            self.row.append(s)
        #print(self.column[self.row[2]])

        return self.row, self.column, self.value

    def contains_vertex(self, v):
        if v in set(self.column):
            return True
        else:
            return False

    def contains_edge(self, u, v):
        if self.contains_vertex(u) and self.contains_vertex(v):
            diastima=self.column[self.row[u]:self.row[u+1]]
            print (diastima)
            if v in diastima:
                return True
            else:
                return False
        else:
            return None

    def num_vertices(self):
        return len((self.row))-1

    def num_edges(self):
        return len(self.column)//2

    def vertex_set(self):
        return set(self.column)

    def neighbors(self, v):
        if self.contains_vertex(v):
            neighbors_of_v = self.column[self.row[v]:self.row[v + 1]]
            return (neighbors_of_v)
        else:
            return None

    def degree(self, v):
        if self.contains_vertex(v):
            d=self.row[v+1]-self.row[v]
            return d
        else:
            return None