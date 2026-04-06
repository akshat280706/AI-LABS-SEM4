# # # import tkinter as tk
# # # from tkinter import messagebox
# # # import matplotlib.pyplot as plt
# # # import networkx as nx

# # import tkinter as tk
# # import networkx as nx
# # import matplotlib.pyplot as plt

# # # Graph definition
# # graph = {
# #     'A': ['B', 'D'],
# #     'B': ['A', 'C'],
# #     'C': ['B', 'D'],
# #     'D': ['A', 'C']
# # }

# # colors = ['red', 'green', 'blue']
# # solution = {}

# # # Check if safe to assign color
# # def is_safe(node, color):
# #     for neighbor in graph[node]:
# #         if neighbor in solution and solution[neighbor] == color:
# #             return False
# #     return True

# # # Backtracking algorithm
# # def backtrack(nodes, index):
# #     if index == len(nodes):
# #         return True

# #     node = nodes[index]

# #     for color in colors:
# #         if is_safe(node, color):
# #             solution[node] = color
# #             update_visual()

# #             root.update()
# #             root.after(500)

# #             if backtrack(nodes, index + 1):
# #                 return True

# #             del solution[node]

# #     return False

# # # Visualization function
# # def update_visual():
# #     plt.clf()
# #     G = nx.Graph()

# #     for node in graph:
# #         G.add_node(node)
# #         for neighbor in graph[node]:
# #             G.add_edge(node, neighbor)

# #     node_colors = []
# #     for node in G.nodes():
# #         node_colors.append(solution.get(node, 'gray'))

# #     pos = nx.spring_layout(G)
# #     nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1000)

# #     plt.draw()

# # # Tkinter setup
# # root = tk.Tk()
# # root.title("Graph Coloring CSP")

# # fig = plt.figure()

# # canvas = tk.Canvas(root, width=600, height=600)
# # canvas.pack()

# # def solve():
# #     nodes = list(graph.keys())
# #     backtrack(nodes, 0)
# #     update_visual()
# #     plt.show()

# # btn = tk.Button(root, text="Solve Graph Coloring", command=solve)
# # btn.pack()

# # root.mainloop()

# import tkinter as tk
# import networkx as nx
# import matplotlib.pyplot as plt

# # ---------------- GRAPH STORAGE ----------------
# graph = {}
# solution = {}
# colors = ['red', 'green', 'blue']

# # ---------------- UI SETUP ----------------
# root = tk.Tk()
# root.title("Graph Coloring CSP")

# # Inputs
# tk.Label(root, text="Enter nodes (space separated)").pack()
# nodes_entry = tk.Entry(root, width=40)
# nodes_entry.pack()

# tk.Label(root, text="From Node").pack()
# from_entry = tk.Entry(root)
# from_entry.pack()

# tk.Label(root, text="To Node").pack()
# to_entry = tk.Entry(root)
# to_entry.pack()

# # ---------------- GRAPH FUNCTIONS ----------------
# def create_graph():
#     global graph
#     graph.clear()
#     nodes = nodes_entry.get().split()

#     for node in nodes:
#         graph[node] = []

#     print("Graph created:", graph)

# def add_edge():
#     u = from_entry.get()
#     v = to_entry.get()

#     if u in graph and v in graph:
#         graph[u].append(v)
#         graph[v].append(u)
#         print(f"Edge added: {u}-{v}")
#     else:
#         print("Invalid nodes!")

# # ---------------- VISUALIZATION ----------------
# def draw_graph(highlight_node=None, bad=False):
#     plt.clf()
#     G = nx.Graph()

#     for node in graph:
#         G.add_node(node)
#         for neighbor in graph[node]:
#             G.add_edge(node, neighbor)

#     node_colors = []

#     for node in G.nodes():
#         if node == highlight_node:
#             if bad:
#                 node_colors.append("red")   # constraint violation
#             else:
#                 node_colors.append("yellow")  # current node
#         else:
#             node_colors.append(solution.get(node, "gray"))

#     pos = nx.spring_layout(G)
#     nx.draw(G, pos, with_labels=True,
#             node_color=node_colors, node_size=1000)

#     plt.pause(0.5)

# # ---------------- CSP LOGIC ----------------
# def is_safe(node, color):
#     for neighbor in graph[node]:
#         if neighbor in solution and solution[neighbor] == color:
#             return False
#     return True

# def backtrack(nodes, index):
#     if index == len(nodes):
#         return True

#     node = nodes[index]

#     for color in colors:
#         solution[node] = color

#         # Show attempt
#         if is_safe(node, color):
#             draw_graph(node, bad=False)
#         else:
#             draw_graph(node, bad=True)
#             root.update()
#             root.after(500)
#             del solution[node]
#             continue

#         root.update()
#         root.after(500)

#         if backtrack(nodes, index + 1):
#             return True

#         # BACKTRACK STEP
#         print(f"Backtracking on {node}")
#         del solution[node]
#         draw_graph(node, bad=True)
#         root.update()
#         root.after(500)

#     return False

# # ---------------- SOLVE ----------------
# def solve_graph():
#     solution.clear()
#     nodes = list(graph.keys())

#     plt.ion()
#     backtrack(nodes, 0)

#     print("Final Solution:", solution)
#     plt.ioff()
#     plt.show()

# # ---------------- BUTTONS ----------------
# tk.Button(root, text="Create Graph", command=create_graph).pack(pady=5)
# tk.Button(root, text="Add Edge", command=add_edge).pack(pady=5)
# tk.Button(root, text="Solve (Color Graph)", command=solve_graph).pack(pady=10)

# root.mainloop()

import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

# ---------------- GLOBALS ----------------
G = None
solution = {}
colors = ['red', 'blue', 'green', 'yellow']
backtrack_count = 0

# ---------------- GRAPH CREATION ----------------
def create_graph():
    global G
    G = nx.DiGraph()

    node_list = node_entry.get().split()
    
    for node in node_list:
        G.add_node(node)

    messagebox.showinfo("Success", "Graph created successfully")


def add_edges():
    global G
    if G is None:
        messagebox.showerror("Error", "Create graph first")
        return
    
    u = from_entry.get()
    v = to_entry.get()

    if u not in G.nodes or v not in G.nodes:
        messagebox.showerror("Error", "Node not found")
        return

    G.add_edge(u, v)
    messagebox.showinfo("Success", f"Edge {u} → {v} added")


# ---------------- CSP LOGIC ----------------
def is_safe(node, color):
    for neighbor in G.neighbors(node):
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True


def backtrack(nodes, index):
    global backtrack_count

    if index == len(nodes):
        return True

    node = nodes[index]

    for color in colors:
        if is_safe(node, color):
            solution[node] = color

            if backtrack(nodes, index + 1):
                return True

            # BACKTRACK
            del solution[node]
            backtrack_count += 1

    return False


# ---------------- SOLVE ----------------
def solve_coloring():
    global backtrack_count

    if G is None:
        messagebox.showerror("Error", "Create graph first")
        return

    solution.clear()
    backtrack_count = 0

    nodes = list(G.nodes())

    if not backtrack(nodes, 0):
        messagebox.showerror("Result", "Graph coloring not possible")
        return

    backtrack_label.config(text=f"Backtracks: {backtrack_count}")
    show_colored_graph()


# ---------------- DISPLAY ----------------
def show_colored_graph():
    pos = nx.spring_layout(G)

    node_colors = []
    for node in G.nodes():
        node_colors.append(solution.get(node, "gray"))

    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1000)

    plt.title("Graph Coloring Result")
    plt.show()


# ---------------- UI ----------------
root = tk.Tk()
root.title("Graph Coloring CSP")

tk.Label(root, text="Enter nodes (space separated)").pack()
node_entry = tk.Entry(root)
node_entry.pack()

tk.Button(root, text="Create Graph", command=create_graph).pack(pady=5)

tk.Label(root, text="From node").pack()
from_entry = tk.Entry(root)
from_entry.pack()

tk.Label(root, text="To node").pack()
to_entry = tk.Entry(root)
to_entry.pack()

tk.Button(root, text="Add Edge", command=add_edges).pack(pady=5)

tk.Button(root, text="Solve Graph Coloring", command=solve_coloring).pack(pady=10)

backtrack_label = tk.Label(root, text="Backtracks: 0")
backtrack_label.pack()

# ---------------- RUN ----------------
root.mainloop()