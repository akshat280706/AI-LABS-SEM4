import tkinter as tk
import networkx as nx
from tkinter import messagebox
import matplotlib.pyplot as plt

G= None
solution={}
# colors=['red','blue']
colors=['red','blue','green']
backtrack_count=0
tree=nx.DiGraph()
state_id=0

def create_graph():
    global G
    G=nx.DiGraph()
    node_list=node_entry.get().split()
    print(f"\nvariables:{node_list}")
    for node in node_list:
        G.add_node(node)
    messagebox.showinfo("success","graph created")

def add_edge():
    global G
    if G is None:
        messagebox.showinfo("error", "create graph first")
        return
    u=from_entry.get()
    v=to_entry.get()
    if u not in G.nodes or v not in G.nodes:
        messagebox.showerror("error","node not added")
        return
    if u==v:
        messagebox.showerror("error","same nodes")
        return
    G.add_edge(u,v)
    messagebox.showinfo("success",f"edge{u} -> {v} added")

def is_safe(node,color):
    neighbors=set(G.neighbors(node)) | set(G.predecessors(node))
    for neighbor in neighbors:
        if neighbor in solution and solution[neighbor]==color:
            return False
    return True

def backtrack(nodes, index, parent_id):
    global backtrack_count,state_id
    
    if index==len(nodes):
        return True
    node=nodes[index]
    print(f"\ntrying color for node {node}:{colors}")
    for color in colors:
        print(f"trying {color} for node:{node}")
        if is_safe(node,color):
            solution[node]=color
            
            state_label=str(solution.copy())
            state_id+=1
            current_id=state_id
            
            tree.add_node(current_id, label=state_label)
            tree.add_edge(parent_id, current_id)
            
            if backtrack(nodes, index+1, current_id):
                return True
            print(f"\nbacktrack from node {node} with colour{color}")
            del solution[node]
            backtrack_count+=1
        else:
            print(f"{color} is not safe for node {node}")
    return False

def solve_coloring():
    global backtrack_count,tree,state_id
    if G is None:
        messagebox.showerror("error", "create graph first")
        return
    
    solution.clear()
    backtrack_count=0
    
    tree=nx.DiGraph()
    state_id=0
    tree.add_node(state_id, label="start")
    nodes=list(G.nodes())
    if not backtrack(nodes,0,state_id):
        messagebox.showerror("result","coloring not possible")
        print(f"\ntotal backtracks:{backtrack_count}")
        show_state_space_tree()
        return
    print(f"\nfinal sol: {solution}")
    print(f"total backtrack: {backtrack_count}")
    
    backtrack_label.config(text=f"Backtracks:{backtrack_count}")
    show_colored_graph()
    show_state_space_tree()

def show_colored_graph():
    pos=nx.spring_layout(G)
    node_colors=[solution.get(node,"gray") for node in G.nodes()]
    
    plt.figure()
    nx.draw(G,pos,with_labels=True, node_color=node_colors,
            node_size=1200, font_size=12,
            font_weight='bold',edge_color='black')
    plt.title("CSP Result")
    plt.show()

def show_state_space_tree():
    pos=nx.spring_layout(tree)
    labels=nx.get_node_attributes(tree,'label')
    plt.figure(figsize=(10,7))
    nx.draw(tree,pos,with_labels=False,
            node_size=1500, node_color='lightblue')
    nx.draw_networkx_labels(tree,pos,labels,font_size=8)
    plt.title("CSP-Graph Coloring")
    plt.show()
    
root=tk.Tk()
root.title("241080009-Akshat-AI LAB7")
tk.Label(root,text="enter nodes(seperate by space)").pack()
node_entry=tk.Entry(root)
node_entry.pack()
tk.Button(root, text="create graph", command=create_graph).pack(pady=5)
tk.Label(root,text="from node").pack()
from_entry=tk.Entry(root)
from_entry.pack()

tk.Label(root,text="to node").pack()
to_entry=tk.Entry(root)
to_entry.pack()
tk.Button(root,text="add edge", command=add_edge).pack(pady=5)
tk.Button(root, text="graph coloring",command=solve_coloring).pack(pady=10)
backtrack_label=tk.Label(root, text="backtracks:0")
backtrack_label.pack()
root.mainloop()