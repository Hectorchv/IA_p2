metro = {
    'universidad' : ['centro_medico'],
    'centro_medico' : ['tacubaya', 'balderas', 'chabacano'],
    'tacubaya' : [],
    'balderas' : ['tacubaya', 'hidalgo', 'pino_suarez'],
    'hidalgo' : ['zocalo', 'la_raza'],
    'zocalo' : [],
    'pino_suarez' : ['zocalo', 'pantitlan'],
    'pantitlan' : ['la_raza'],
    'la _raza': ['politecnico'],
    'chabacano' : ['pino_suarez', 'pantitlan'],
    'politecnico' : []
}

visitado = [] 
queue = []     

def bfs(grafo, inicio, sol):
    visitado=[]
    queue=[inicio]
    if inicio==sol:
        print("Solución: ")
        print(inicio)

    while queue:
        s = queue.pop(0)
        nodo=s[-1]
        if nodo not in visitado:
            neighbours=grafo[nodo]
            for neighbour in neighbours:
                camino=list(s)
                camino.append(neighbour)
                queue.append(camino)
                if neighbour == sol:
                    return camino

ruta_politecnico = bfs(metro, 'universidad', 'universidad')
print("La ruta desde el metro Universidad hasta el metro Politécnico es: ", visitado)
#prueba