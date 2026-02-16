import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

G=None
def create_graph():
    global G
    if graph_type.get()=="directed":
        G=nx.DiGraph()
    else:
        G=nx.Graph()
    
    node_list=node_entry.get().split()
    
    for node in node_list:
        G.add_node(node)

def add_edges():
    global G
    if G is None:
        messagebox.showerror("error", "create the graph first")
        return
    
    if weight_var.get()==1 and weight_entry.get()=="":
        messagebox.showerror("error", "enter the weight")
        return
    u=from_entry.get()
    v=to_entry.get()
    
    if u not in G.nodes or v not in G.nodes:
        messagebox.showerror("error", "node not added")
        return
    
    if weight_var.get()==1:
        w=int(weight_entry.get())
        if w<0:
            messagebox.showerror("error", "theres an error in this AI lab2 exp, can't have negetive weights")
            return
        G.add_edge(u,v,weight=w)
    else:
        G.add_edge(u,v)

def show_graph():
    pos=nx.spring_layout(G)
    nx.draw(G,pos,with_labels=True)
    labels=nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels, label_pos=0.3)
    plt.show()

root=tk.Tk()
root.title("AI LAB 2(241080009)")

graph_type=tk.StringVar(value="undirected")
tk.Label(root,text="graph type is:").pack()
tk.OptionMenu(root,graph_type,"undirected","directed").pack()

weight_var=tk.IntVar()
tk.Checkbutton(root,text="weighted graph", variable=weight_var).pack()

tk.Label(root, text="enter the nodes(seperatrd using spaces)").pack()

node_entry=tk.Entry(root)
node_entry.pack()

tk.Button(root,text="click here to create graph", command=create_graph).pack()

tk.Label(root,text="from node").pack()
from_entry=tk.Entry(root)
from_entry.pack()

tk.Label(root,text="to node").pack()
to_entry=tk.Entry(root)
to_entry.pack()

tk.Label(root,text="weight").pack()
weight_entry=tk.Entry(root)
weight_entry.pack()

tk.Button(root, text="add edge", command=add_edges).pack()
tk.Button(root, text="display graph", command=show_graph).pack()
root.mainloop()