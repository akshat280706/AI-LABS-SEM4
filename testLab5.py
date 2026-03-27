# import tkinter as tk
# from tkinter import messagebox
# import random
# import matplotlib.pyplot as plt
# import networkx as nx

# # -------------------------------
# # Heuristic Function
# # -------------------------------
# def calculate_conflicts(state):
#     conflicts = 0
#     n = len(state)

#     for i in range(n):
#         for j in range(i + 1, n):
#             if state[i] == state[j]:
#                 conflicts += 1
#             elif abs(state[i] - state[j]) == abs(i - j):
#                 conflicts += 1

#     return conflicts


# # -------------------------------
# # Generate Neighbors
# # -------------------------------
# def get_neighbors(state):
#     neighbors = []
#     n = len(state)

#     for col in range(n):
#         for row in range(n):
#             if state[col] != row:
#                 new_state = list(state)
#                 new_state[col] = row
#                 neighbors.append(new_state)

#     return neighbors


# # -------------------------------
# # Hill Climbing
# # -------------------------------
# def hill_climbing(n):
#     current = [random.randint(0, n - 1) for _ in range(n)]
#     path = [current]
#     visited = [tuple(current)]

#     G = nx.DiGraph()
#     G.add_node(str(current))

#     while True:
#         current_conflicts = calculate_conflicts(current)
#         neighbors = get_neighbors(current)

#         best = None
#         best_h = current_conflicts

#         for neighbor in neighbors:
#             h = calculate_conflicts(neighbor)
#             G.add_edge(str(current), str(neighbor))

#             if h < best_h:
#                 best_h = h
#                 best = neighbor

#         if best is None:
#             break

#         current = best
#         path.append(current)
#         visited.append(tuple(current))

#         if best_h == 0:
#             break

#     return current, path, visited, G


# # -------------------------------
# # Draw Board on Canvas
# # -------------------------------
# def draw_board(canvas, state):
#     canvas.delete("all")
#     n = len(state)
#     size = 400
#     cell = size // n

#     for i in range(n):
#         for j in range(n):
#             color = "white" if (i + j) % 2 == 0 else "gray"
#             canvas.create_rectangle(j*cell, i*cell,
#                                     (j+1)*cell, (i+1)*cell,
#                                     fill=color)

#     # draw queens
#     for col in range(n):
#         row = state[col]
#         x = col * cell + cell // 2
#         y = row * cell + cell // 2
#         canvas.create_text(x, y, text="Q", font=("Arial", 20), fill="red")


# # -------------------------------
# # Draw Graph
# # -------------------------------
# def show_graph(G):
#     pos = nx.spring_layout(G, seed=42)
#     nx.draw(G, pos, with_labels=True, node_size=500, font_size=6)
#     plt.title("State Space Graph")
#     plt.show()


# # -------------------------------
# # Run Button
# # -------------------------------
# def run_algorithm():
#     try:
#         n = int(entry.get())
#         if n not in [4, 8]:
#             messagebox.showerror("Error", "Enter 4 or 8 only")
#             return

#         solution, path, visited, G = hill_climbing(n)

#         # Show path
#         output.delete("1.0", tk.END)
#         output.insert(tk.END, "Path:\n")
#         for p in path:
#             output.insert(tk.END, f"{p}  h={calculate_conflicts(p)}\n")

#         output.insert(tk.END, "\nVisited Nodes:\n")
#         for v in visited:
#             output.insert(tk.END, f"{v}\n")

#         output.insert(tk.END, f"\nFinal Solution: {solution}")
#         output.insert(tk.END, f"\nConflicts: {calculate_conflicts(solution)}\n")

#         draw_board(canvas, solution)

#         # Show graph in separate window
#         show_graph(G)

#     except:
#         messagebox.showerror("Error", "Invalid input")


# # -------------------------------
# # GUI Setup
# # -------------------------------
# root = tk.Tk()
# root.title("N-Queen Hill Climbing")

# frame = tk.Frame(root)
# frame.pack()

# tk.Label(frame, text="Enter N (4 or 8):").grid(row=0, column=0)
# entry = tk.Entry(frame)
# entry.grid(row=0, column=1)

# btn = tk.Button(frame, text="Run", command=run_algorithm)
# btn.grid(row=0, column=2)

# # Canvas for board
# canvas = tk.Canvas(root, width=400, height=400)
# canvas.pack()

# # Output box
# output = tk.Text(root, height=15, width=60)
# output.pack()

# root.mainloop()


import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
import networkx as nx

# Store last results globally
last_graph = None
last_path = None


# -------------------------------
# Heuristic Function
# -------------------------------
def calculate_conflicts(state):
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# -------------------------------
# Generate Neighbors
# -------------------------------
def get_neighbors(state):
    neighbors = []
    n = len(state)

    for col in range(n):
        for row in range(n):
            if state[col] != row:
                new_state = list(state)
                new_state[col] = row
                neighbors.append(new_state)

    return neighbors


# -------------------------------
# Hill Climbing
# -------------------------------
def hill_climbing(n):
    current = [random.randint(0, n - 1) for _ in range(n)]
    path = [current]
    visited = [tuple(current)]

    full_graph = nx.DiGraph()
    full_graph.add_node(str(current))

    while True:
        current_conflicts = calculate_conflicts(current)
        neighbors = get_neighbors(current)

        best = None
        best_h = current_conflicts

        for neighbor in neighbors:
            h = calculate_conflicts(neighbor)

            # FULL STATE SPACE
            full_graph.add_edge(str(current), str(neighbor))

            if h < best_h:
                best_h = h
                best = neighbor

        if best is None:
            break

        current = best
        path.append(current)
        visited.append(tuple(current))

        if best_h == 0:
            break

    return current, path, visited, full_graph


# -------------------------------
# Draw Chess Board
# -------------------------------
def draw_board(canvas, state):
    canvas.delete("all")
    n = len(state)
    size = 400
    cell = size // n

    for i in range(n):
        for j in range(n):
            color = "white" if (i + j) % 2 == 0 else "gray"
            canvas.create_rectangle(j*cell, i*cell,
                                    (j+1)*cell, (i+1)*cell,
                                    fill=color)

    for col in range(n):
        row = state[col]
        x = col * cell + cell // 2
        y = row * cell + cell // 2
        canvas.create_text(x, y, text="♛", font=("Arial", 20), fill="red")


# -------------------------------
# Show Full State Space Graph
# -------------------------------
def show_full_graph():
    if last_graph is None:
        messagebox.showinfo("Info", "Run the algorithm first!")
        return

    pos = nx.spring_layout(last_graph, seed=42)

    nx.draw(last_graph, pos,
            with_labels=True,
            node_size=500,
            font_size=6,
            node_color="lightblue")

    plt.title("Complete State Space")
    plt.show()


# -------------------------------
# Show Solution Path Graph
# -------------------------------
def show_path_graph():
    if last_path is None:
        messagebox.showinfo("Info", "Run the algorithm first!")
        return

    G_path = nx.DiGraph()

    for i in range(len(last_path) - 1):
        G_path.add_edge(str(last_path[i]), str(last_path[i+1]))

    pos = nx.spring_layout(G_path, seed=42)

    nx.draw(G_path, pos,
            with_labels=True,
            node_size=800,
            font_size=8,
            node_color="lightgreen",
            edge_color="red")

    plt.title("Solution Path Only")
    plt.show()


# -------------------------------
# Run Algorithm
# -------------------------------
def run_algorithm():
    global last_graph, last_path

    try:
        n = int(entry.get())

        if n not in [4, 8]:
            messagebox.showerror("Error", "Enter 4 or 8 only")
            return

        solution, path, visited, G = hill_climbing(n)

        last_graph = G
        last_path = path

        output.delete("1.0", tk.END)
        
        output.insert(tk.END, f"Initial State: {path[0]}  h={calculate_conflicts(path[0])}\n\n")
        # PATH
        output.insert(tk.END, "Path:\n")
        for p in path:
            output.insert(tk.END, f"{p}  h={calculate_conflicts(p)}\n")

        # VISITED NODES
        output.insert(tk.END, "\nVisited Nodes:\n")
        for v in visited:
            output.insert(tk.END, f"{v}\n")

        # FINAL
        output.insert(tk.END, f"\nFinal State: {solution}")
        output.insert(tk.END, f"\nConflicts: {calculate_conflicts(solution)}\n")

        draw_board(canvas, solution)

    except:
        messagebox.showerror("Error", "Invalid input")


# -------------------------------
# GUI
# -------------------------------
root = tk.Tk()
root.title("N-Queen Hill Climbing")

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Enter N (4 or 8):").grid(row=0, column=0)
entry = tk.Entry(frame)
entry.grid(row=0, column=1)

tk.Button(frame, text="Run", command=run_algorithm).grid(row=0, column=2)

# NEW BUTTONS
tk.Button(frame, text="Show State Space", command=show_full_graph).grid(row=1, column=0)
tk.Button(frame, text="Show Solution Path", command=show_path_graph).grid(row=1, column=1)

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

output = tk.Text(root, height=15, width=60)
output.pack()

root.mainloop()
