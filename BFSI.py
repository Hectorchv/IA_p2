grafo={
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F','J'],
  'D' : [],
  'E' : ['H'],
  'F' : [],
  'H':[],
  'J':[]
}

def bfsl(grafo, nodo,iter):
  visitado = [] 
  queue = []     
  prev=[]
  
  visitado.append(nodo)
  queue.append(nodo)
  prev = []


  while queue:
    s = queue.pop(0)

    if s not in prev:
      prev=queue.copy()
      iter-=1
      if iter==0:
        return visitado

    for neighbour in grafo[s]:
      if neighbour not in visitado:
        visitado.append(neighbour)
        queue.append(neighbour)
    
def bfsi(grafo, nodo,iter):
  for i in range(iter+1):
    print("Para i =", i)
    print(bfsl(grafo,nodo,i))

recorrido = bfsi(grafo, 'A', 4)