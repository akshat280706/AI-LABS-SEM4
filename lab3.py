import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from tkinter import messagebox

def next_state(state, cap1, cap2):
    x,y=state
    return [
        (cap1,y),
        (x,cap2),
        (0,y),
        (x,0),
        (x-min(x,cap2-y), y+min(x,cap2-y)),
        (x+min(y,cap1-x), y-min(y,cap1-x))
    ]

def validate_inputs(require_target=False):
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("error", "enter the capacity of each jug")
        return None
    
    if require_target and e3.get()=="":
        messagebox.showerror("error", "enter the target value needed")
        return None
    
    try:
        cap1=int(e1.get())
        cap2=int(e2.get())
        
        if require_target:
            target=int(e3.get())
        else:
            target=None
    except:
        messagebox.showerror("error", "enter valid integers")
        return None
    
    if cap1<=0 or cap2<=0:
        messagebox.showerror("error", "enter value greater than 0")
        return None
    if require_target:
        if target<0:
            messagebox.showerror("error", "enter target greater than 0")
            return None
        if target>max(cap1, cap2):
            messagebox.showerror("error", "target should be within range")
            return None
    return cap1, cap2, target

def search_tree(cap1, cap2, target, method):
    start=(0,0)
    if method=="BFS":
        structure=deque([start]) 
        remove=structure.popleft
    else:
        structure=[start]
        remove=structure.pop
    
    visited=set([start])
    parent={}
    
    G=nx.DiGraph()
    G.add_node(start)
    goal=None
    
    while structure:
        state=remove()
        if target in state:
            goal=state
            break
        
        for ns in next_state(state, cap1, cap2):
            if ns not in visited:
                visited.add(ns)
                parent[ns]=state
                G.add_edge(state,ns)
                structure.append(ns)
    
    tree=nx.DiGraph()
    path=[]
    
    if goal:
        current=goal
        while current!=start:
            path.append(current)
            tree.add_node(current)
            prev=parent[current]
            tree.add_edge(prev,current)
            current=prev
        
        tree.add_node(start)
        path.append(start)
        path.reverse()
    return path, visited, tree

def state_space(cap1, cap2):
    start=(0,0)
    queue=[(0,0)]
    visited=set([start])
    
    G=nx.DiGraph()
    
    while queue:
        state=queue.pop(0)
        for ns in next_state(state, cap1, cap2):
            G.add_edge(state,ns)
            
            if ns not in visited:
                visited.add(ns)
                queue.append(ns)
    return G

def draw_graph(G, title):
    plt.figure(figsize=(6,5))
    pos=nx.spring_layout(G, seed=42)

    nx.draw(G, pos,with_labels=True,
            node_color="red", node_size=1500,
            font_size=9,
            arrows=True)

    plt.title(title)
    plt.show()

def show_space():
    result = validate_inputs(require_target=False)
    if result is None:
        return

    cap1, cap2, _ = result
    G = state_space(cap1, cap2)

    draw_graph(G, "state space: ")
    output.delete(1.0, tk.END)
    output.insert(tk.END, "state space graph is shown\n")


def run(method):
    result = validate_inputs(require_target=True)
    if result is None:
        return

    cap1, cap2, target = result
    path, visited, G = search_tree(cap1, cap2, target, method)

    draw_graph(G, method + "graph")

    output.delete(1.0, tk.END)
    output.insert(tk.END, "The visited nodes are:\n")
    output.insert(tk.END, str(list(visited)) + "\n\n")

    if path:
        output.insert(tk.END, "The solution path is:\n")
        output.insert(tk.END, str(path) + "\n\n")
        output.insert(tk.END, "The path cost is: " + str(len(path)-1))
    else:
        output.insert(tk.END, "sorry, no such solution exists, try with some other inputs")
        messagebox.showerror("error", "no such solution exists")
root = tk.Tk()
root.title("241080009(IT): Water Jug")

tk.Label(root,text="Jug1").pack()
e1=tk.Entry(root)
e1.pack()

tk.Label(root,text="Jug2").pack()
e2=tk.Entry(root)
e2.pack()

tk.Label(root,text="Target").pack()
e3=tk.Entry(root)
e3.pack()

tk.Button(root,text="State Space",command=show_space).pack()
tk.Button(root,text="BFS",command=lambda: run("BFS")).pack()
tk.Button(root,text="DFS",command=lambda: run("DFS")).pack()

output = tk.Text(root,height=12)
output.pack()
root.mainloop()
