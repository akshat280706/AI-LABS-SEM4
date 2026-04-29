def is_safe(node,color):
    neighbors=set(G.neighbots(node)) | set(G.predecessors(node))
    for neighbor in neighbors:
        if neighbor in solution and solution[neighbor]==color:
            return false
    return true

def backtrack(index,node,parent_id):
    if index==len(nodes):
        return true
    node=nodes[index]
    
    for color in colors:
        if isSafe(node,color):
            solution[node]=color
            
            if backtrack(node,index+1,current_id):
                return true
            del solution[node]
    return false
