grafo = {
  'I' : ['D','E','A'],
  'D' : ['F'],
  'E' : ['D', 'O'],
  'A' : ['D'],
  'O' : ['M'],
  'M' : ['Q']
}

visitado = [] 
queue = []
n = 0     

def bfs(visitado, grafo, nodo,  L, flag):

 if n != L:
    for neighbour in grafo[nodo]:
        if neighbour not in visitado:
            visitado.append(neighbour)
            if flag and neighbour == grafo[nodo]:
                bfs(visitado, grafo, neighbour, L, True)
            else:
                bfs(visitado, grafo, neighbour, L, False)

  queue.append(nodo,n)

  while queue:

    print(visitado)
    s = queue.pop(0)


    for neighbour in grafo[s]:
      if neighbour not in visitado:
        visitado.append(neighbour)
        queue.append(neighbour)
    


bfs(visitado, grafo, 'I', 2)