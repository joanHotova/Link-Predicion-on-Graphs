class AdjacencyMatrix:

  def __init__(self, key_list):
      self.key_list=key_list
      lengthoflist= len(key_list)
      self.AdjMatrix=[]
      for i in range(lengthoflist): 
        self.AdjMatrix.append([0 for i in range(lengthoflist)])
      self.lengthoflist = lengthoflist

  def fill_AdjMatrix(self,v1,v2):
        self.AdjMatrix[v1][v2] = 1
        self.AdjMatrix[v2][v1] = 1

  def return_AdjMatrix(self):
      return self.AdjMatrix

  def print_AdjMatrix (self):
      for row in self.AdjMatrix[:][:]:
          for val in row[:]:
              print(val, end=" ")
          print()

  def contains_vertex(self, v):
      if v in self.key_list:
          return True
      else:
          return False

  def contains_edge(self,u,v):
        if self.contains_vertex(u) and self.contains_vertex(v):
            if self.AdjMatrix[u][v]==1:
                return True
            else:
                return False
        else:
                return None


  def num_vertices(self):
      return len(self.key_list)

  def num_edges(self):
      sum = 0
      i = 1
      for row in self.AdjMatrix[:][:]:
          for val in row[i:]:
              sum = sum+val
          i += 1
      return sum

  def vertex_set(self):
    return (self.key_list)

  def neighbors(self, v):
      if self.contains_vertex(v):
          indices = [i for i, x in enumerate(list(self.AdjMatrix[v])) if x == 1]
          return indices
      else:
          return None


  def degree(self,v):
      if self.contains_vertex(v):
          s=0
          for row in self.AdjMatrix[:][v:v+1]:
              for val in row[:]:
                  s=s+val
              return s
      else:
          return None


