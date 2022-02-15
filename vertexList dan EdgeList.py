vertexList = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13]
print("Vertex List : ", vertexList)

edgeList = [ (1,2), (1,3), (2,1), (2,5), (2,7), (3,1), (3,4), (3,6), (4,3), (4,7), (4,9), (5,2), (5,8), (6,3),
             (6,9), (7,2), (7,4), (7,10), (8,5), (8,10), (9,4), (9,6), (9,10), (10,7), (10,8), (10,9)]
print("Edge List : ", edgeList)

graphs = (vertexList, edgeList)
print("Graph : ", graphs)

def breadth_Fist(graphs, start):
    vertexList, edgeList = graphs
    visitedList = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])
    print("Adjacency List : ", adjacencyList)
    while queue:
        current = queue.pop(0)
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.append(neighbor)
            visitedList.append(current)
        return visitedList

print("Breadth Fist : ", breadth_Fist(graphs, 4))