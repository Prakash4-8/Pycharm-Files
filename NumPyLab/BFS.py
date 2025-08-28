# Bread th first search
graph = {
    '3': ['1', '3', '4', '5'],
    '2': ['5', '7', '8', '3'],
    '6': ['6', '8', '4', '3'],
    '1':['3'],
    '4':[],
    '5':[]

}
visited = []
queue = []
def bfs (graph, visited, root):

    visited.append(root)
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print(node, end=' -> ')
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)



bfs(graph, visited, '3')
print('\b'*3)