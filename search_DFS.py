graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}

def DFS(start_v, start_node):
    stack = []
    discovered = []

    stack.append(start_node)

    while stack :
        node = stack.pop()
        if node not in discovered :
            discovered.append(node)
            stack.extend(graph[node])
    print(discovered)
    return discovered

def DFS_RECURSIVE(start_v, discovered=[]):
    discovered.append(start_v)
    for w in graph[start_v]:
        if not w in discovered:
            discovered = DFS_RECURSIVE(w, discovered)
    print(discovered)
    return discovered

if __name__ == "__main__":

    DFS_RECURSIVE(5)




