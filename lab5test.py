def calculate_conflicts(state):
    conflict=0
    for i in range(n):
        for j in range(i+1,n):
            if state[i]==state[j] or abs(state[i]-state[j])==abs(i-j):
                conflict+=1
    return conflict

def get_neighbors(state):
    neighbors=[]
    n=len(state)
    for col in range(n):
        for row in range(n):
            if state[col]!=row:
                new_state=list(state)
                new_state[col]=row
                neighbors.append(new_state)
    return neighbors

def hill_climbing(n):
    current=[random.randint(0,n-1) for _ in range(n)]
    path=[current]
    visited=[tuple(current)]
    full_graph=nx.DiGraph()
    full_graph.add_node(str(current))
    while True:
        current_conflict=calculate_conflicts(current)
        neightbors=get_neighbors(current)
        best=None
        best_h=current_conflict
        
        for neighbor in neightbors:
            h=calculate_conflicts(neighbor)
            full_graph.add_edge(str(current),str(neighbor))
            if h<best_h:
                best_h=h
                best=neighbor

        if best is None:
            break
            # return hill_climbing(n)
        current=best
        path.append(current)
        visited.append(tuple(current))
        
        if best_h==0:
            break
    return current, path, visited, full_graph