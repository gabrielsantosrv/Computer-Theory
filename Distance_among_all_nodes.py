queue = list()

def enqueue(x):
    queue.append(x)

def dequeue():
    return queue.pop(0)

def BFS (graph, matrix, j):
    visited = [False]*len(graph)
    enqueue((j,0))
    
    while len(queue) > 0:
	(i,h) = dequeue()
	visited[i] = True
	matrix[i][j] = h

	for a in range(len(graph)):
	  if graph[i][a] == 1 and not visited[a]:
	    enqueue((a,h+1))


def distance_matrix(graph):
	matrix = [0]*len(graph)
	for i in range(len(graph)):
	   matrix[i] = [0] * len(graph[0])

	for j in range(len(graph)):
	   BFS(graph, matrix, j)
	
	return matrix

graph = [[1,0,1,0],
	 [0,1,1,1],
	 [1,1,1,1],
	 [0,1,1,1]]

matrix = distance_matrix(graph)
print(matrix)
	
