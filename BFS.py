V = ["S", "A", "B", "C", "D", "E", "F", "G", "H"]
E = [("S", "A"), ("A", "S"), ("S", "B"), ("B", "S"), ("S", "C"), ("C", "S"), 
     ("A", "B"), ("B", "A"), ("A", "D"), ("D", "A"), ("B", "D"), ("D", "B"), 
     ("B", "G"), ("G", "B"), ("B", "F"), ("F", "B"), ("C", "F"), ("F", "C"), 
     ("C", "B"), ("B", "C"), ("D", "E"), ("E", "D"), ("F", "E"), ("E", "F"), 
     ("F", "H"), ("H", "F"), ("E", "G"), ("G", "E"), ("H", "G"), ("G", "H")]

graph = {}
for edge in E:
    if edge[0] not in graph:
        graph[edge[0]] = []
    graph[edge[0]].append(edge[1])

for node in graph:
    graph[node].sort()

def BFS(initialState, goalState):
    frontier = [initialState]  
    explored = [] 
    while frontier:
        state = frontier.pop(0)  
        explored.append(state)  
        if state == goalState:
            return explored 

        for neighbor in graph.get(state, []):
            if neighbor not in explored and neighbor not in frontier:
                frontier.append(neighbor)

    return False  

if __name__ == "__main__":
    res = BFS('S', 'G')  

    if res:
        s = 'Explored: '  
        for i in res:
            s += i + ' '  
            print(s)  
    else:
        print("No path found.")
