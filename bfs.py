from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)
  
  def addEdge(self,v1,v2):
    self.graph[v1].append(v2)
  
  def BFS(self, start):
    visitedSet = set()
    bfs = [] 
    queue = []
    queue.append(start)
    bfs.append(start)
    visitedSet.add(start)
  
    while(queue):
      current = queue.pop(0)

      for neighbor in self.graph.get(current):
        if (neighbor not in visitedSet):
          bfs.append(neighbor)
          visitedSet.add(neighbor)
          queue.append(neighbor)

    print(bfs)

  
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Breadth First Traversal")
g.BFS(0) 
