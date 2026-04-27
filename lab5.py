import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
import networkx as nx

last_graph=None
last_path=None
def calculate_conflicts(state):
    conflict=0
    n=len(state)
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
        neighbors=get_neighbors(current)
        best=None
        best_h=current_conflict
        
        for neighbor in neighbors:
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

def draw_board(canvas,state):
    canvas.delete("all")
    n=len(state)
    size=400
    cell=size//n
    for i in range(n):
        for j in range(n):
            color="white" if (i+j)%2==0 else "gray"
            canvas.create_rectangle(j*cell, i*cell,
                                    (j+1)*cell, (i+1)*cell,
                                    fill=color)
    
    for col in range(n):
        row=state[col]
        x=col*cell+cell//2
        y=row*cell+cell//2
        canvas.create_text(x,y,text="Q", fill="red")

def show_full_graph():
    if last_graph is None:
        messagebox.showerror("error", "first run the algorithm")
        return
    pos=nx.spring_layout(last_graph, seed=42)
    nx.draw(last_graph, pos, with_labels=True,
            node_size=500, font_size=6,node_color="lightblue")
    plt.title("state space of N queens")
    plt.show()

def show_path_graph():
    if last_graph is None:
        messagebox.showerror("error", "first run the algorithm")
        return
    G_path=nx.DiGraph()
    for i in range(len(last_path)-1):
        G_path.add_edge(str(last_path[i]),str(last_path[i+1]))  
    pos=nx.spring_layout(G_path, seed=42)
    nx.draw(G_path, pos, with_labels=True,
            node_size=800, font_size=8,node_color="lightgreen")
    plt.title("Solution Path")
    plt.show()

def run_algorithm():
    global last_graph, last_path
    try:
        n=int(entry.get())
        if n not in [4,8]:
            messagebox.showerror("error", "enter 4 or 8 only")
            return
        solution, path, visited, G=hill_climbing(n)
        last_graph=G
        last_path=path
        output.delete("1.0",tk.END)
        output.insert(tk.END, "initial state: "+str(path[0])+ " h="+str(calculate_conflicts(path[0]))+"\n\n")
        output.insert(tk.END, "path: \n")
        for p in path:
            output.insert(tk.END, str(p)+" h="+str(calculate_conflicts(p))+"\n")
        output.insert(tk.END, "\nvisited nodes:\n")
        for v in visited:
            output.insert(tk.END, str(v)+"\n")
        output.insert(tk.END, "\nfinal state: "+str(solution))
        output.insert(tk.END, "\nheuristic(conflicts): "+str(calculate_conflicts(solution))+"\n")
        draw_board(canvas, solution)
        
    except:
        messagebox.showerror("error", "invalid input")

root=tk.Tk()
root.title("241080009-Akshat-LAB5")
frame=tk.Frame(root)
frame.pack(pady=10)
tk.Label(frame, text="enter N(4/8): ").grid(row=0, column=0)
entry=tk.Entry(frame)
entry.grid(row=0, column=1)
tk.Button(frame, text="run hill climbing", command=run_algorithm).grid(row=0, column=2)
tk.Button(frame, text="whole state space", command=show_full_graph).grid(row=1, column=0)
tk.Button(frame, text="solution path graph", command=show_path_graph).grid(row=1, column=1)

canvas=tk.Canvas(root, width=400, height=400)
canvas.pack()
output=tk.Text(root, height=15, width=60)
output.pack()
root.mainloop()







# import tkinter as tk
# from tkinter import messagebox
# import random
# import matplotlib.pyplot as plt
# import networkx as nx

# last_graph=None
# last_path=None
# def calculate_conflicts(state):
#     conflict=0
#     n=len(state)
#     for i in range(n):
#         for j in range(i+1,n):
#             if state[i]==state[j] or abs(state[i]-state[j])==abs(i-j):
#                 conflict+=1
#     return conflict

# def get_neighbors(state):
#     neighbors=[]
#     n=len(state)
#     for col in range(n):
#         for row in range(n):
#             if state[col]!=row:
#                 new_state=list(state)
#                 new_state[col]=row
#                 neighbors.append(new_state)
#     return neighbors

# def hill_climbing(n):
#     current=[random.randint(0,n-1) for _ in range(n)]
#     path=[current]
#     visited=[tuple(current)]
#     full_graph=nx.DiGraph()
#     full_graph.add_node(str(current))
#     while True:
#         current_conflict=calculate_conflicts(current)
#         neighbors=get_neighbors(current)
#         best=None
#         best_h=current_conflict
        
#         for neighbor in neighbors:
#             h=calculate_conflicts(neighbor)
#             full_graph.add_edge(str(current),str(neighbor))
#             if h<best_h:
#                 best_h=h
#                 best=neighbor

#         if best is None:
#             break
#             # return hill_climbing(n)
#         current=best
#         path.append(current)
#         visited.append(tuple(current))
        
#         if best_h==0:
#             break
#     return current, path, visited, full_graph

# def draw_board(canvas,state):
#     canvas.delete("all")
#     n=len(state)
#     size=400
#     cell=size//n
#     for i in range(n):
#         for j in range(n):
#             color="white" if (i+j)%2==0 else "gray"
#             canvas.create_rectangle(j*cell, i*cell,
#                                     (j+1)*cell, (i+1)*cell,
#                                     fill=color)
    
#     for col in range(n):
#         row=state[col]
#         x=col*cell+cell//2
#         y=row*cell+cell//2
#         canvas.create_text(x,y,text="Q", fill="red")

# def show_full_graph():
#     if last_graph is None:
#         messagebox.showerror("error", "first run the algorithm")
#         return
#     pos=nx.spring_layout(last_graph, seed=42)
#     nx.draw(last_graph, pos, with_labels=True,
#             node_size=500, font_size=6,node_color="lightblue")
#     plt.title("state space of N queens")
#     plt.show()

# def show_path_graph():
#     if last_graph is None:
#         messagebox.showerror("error", "first run the algorithm")
#         return
#     G_path=nx.DiGraph()
#     for i in range(len(last_path)-1):
#         G_path.add_edge(str(last_path[i]),str(last_path[i+1]))  
#     pos=nx.spring_layout(G_path, seed=42)
#     nx.draw(G_path, pos, with_labels=True,
#             node_size=800, font_size=8,node_color="lightgreen")
#     plt.title("Solution Path")
#     plt.show()

# def run_algorithm():
#     global last_graph, last_path
#     try:
#         n=int(entry.get())
#         if n not in [4,8]:
#             messagebox.showerror("error", "enter 4 or 8 only")
#             return
#         solution, path, visited, G=hill_climbing(n)
#         last_graph=G
#         last_path=path
#         output.delete("1.0",tk.END)
#         output.insert(tk.END, "initial state: "+str(path[0])+ " h="+str(calculate_conflicts(path[0]))+"\n\n")
#         output.insert(tk.END, "path: \n")
#         for p in path:
#             output.insert(tk.END, str(p)+" h="+str(calculate_conflicts(p))+"\n")
#         output.insert(tk.END, "\nvisited nodes:\n")
#         for v in visited:
#             output.insert(tk.END, str(v)+"\n")
#         output.insert(tk.END, "\nfinal state: "+str(solution))
#         output.insert(tk.END, "\nheuristic(conflicts): "+str(calculate_conflicts(solution))+"\n")
#         draw_board(canvas, solution)
        
#     except:
#         messagebox.showerror("error", "invalid input")

# root=tk.Tk()
# root.title("241080009-Akshat-LAB5")
# frame=tk.Frame(root)
# frame.pack(pady=10)
# tk.Label(frame, text="enter N(4/8): ").grid(row=0, column=0)
# entry=tk.Entry(frame)
# entry.grid(row=0, column=1)
# tk.Button(frame, text="run hill climbing", command=run_algorithm).grid(row=0, column=2)
# tk.Button(frame, text="whole state space", command=show_full_graph).grid(row=1, column=0)
# tk.Button(frame, text="solution path graph", command=show_path_graph).grid(row=1, column=1)

# canvas=tk.Canvas(root, width=400, height=400)
# canvas.pack()
# output=tk.Text(root, height=15, width=60)
# output.pack()
# root.mainloop()
