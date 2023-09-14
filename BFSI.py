grafo = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visitado = [] 
queue = []     

def bfs(visitado, grafo, nodo):
  visitado.append(nodo)
  queue.append(nodo)

  while queue:
    s = queue.pop(0)
    print (s, end = " ")

    for neighbour in grafo[s]:
      if neighbour not in visitado:
        visitado.append(neighbour)
        queue.append(neighbour)


bfs(visitado, grafo, 'A')