  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F','J'],
  'D' : [],
  'E' : ['H'],
  'F' : [],
  'H':[],
  'J':[]
}

visitado = [] 
queue = []     
prev=[]

def bfs(visitado, grafo, nodo,iter):
  visitado.append(nodo)
  queue.append(nodo)
  prev=queue.copy()
  while queue:
    s = queue.pop(0)

    if s not in prev:
      prev=queue.copy()
      iter-=1
      if iter==0:
        break

    for neighbour in grafo[s]:
      if neighbour not in visitado:
        visitado.append(neighbour)
        queue.append(neighbour)
    

  print(visitado)
    


bfs(visitado, grafo, 'A',3)
