visited = set()


def dfs(visited, graph, root):
    if root not in visited:
        print(root, end=' -> ')
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour)


if __name__ == '__main__':
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }
    print("Following is Depth First Traversal: ")
    dfs(visited, graph, '5')
    print('\b' * 3)
