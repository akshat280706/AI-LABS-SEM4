# 241080009_akshat_AI Lab4
import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
import heapq

graph = {
    'Arad':{'Zerind':75, 'Sibiu':140, 'Timisoara':118},
    'Bucharest':{'Fagaras':211, 'Pitesti':101, 'Giurgiu':90, 'Urziceni':85},
    'Craiova':{'Drobeta':120, 'Rimnicu Vilcea':146, 'Pitesti':138},
    'Drobeta':{'Mehadia':75, 'Craiova':120},
    'Eforie':{'Hirsova':86},    
    'Fagaras':{'Sibiu':99, 'Bucharest':211},
    'Giurgiu':{'Bucharest':90},
    'Hirsova':{'Urziceni':98, 'Eforie':86},
    'Iasi':{'Vaslui':92, 'Neamt':87},
    'Lugoj':{'Timisoara':111, 'Mehadia':70},
    'Mehadia':{'Lugoj':70, 'Drobeta':75},
    'Neamt':{'Iasi':87},
    'Oradea':{'Zerind':71, 'Sibiu':151},
    'Pitesti':{'Rimnicu Vilcea':97, 'Craiova':138, 'Bucharest':101},
    'Rimnicu Vilcea':{'Sibiu':80, 'Craiova':146, 'Pitesti':97},
    'Sibiu':{'Arad':140, 'Oradea':151, 'Fagaras':99, 'Rimnicu Vilcea':80},
    'Timisoara':{'Arad':118, 'Lugoj':111},
    'Urziceni':{'Bucharest':85, 'Hirsova':98, 'Vaslui':142},
    'Vaslui':{'Urziceni':142, 'Iasi':92},
    'Zerind':{'Arad':75, 'Oradea':71},
}
heuristic = {
    'Arad':366, 'Bucharest':0, 'Craiova':160, 'Drobeta':242, 'Eforie':161,
    'Fagaras':178, 'Giurgiu':77, 'Hirsova':151, 'Iasi':226, 'Lugoj':244,
    'Mehadia':241, 'Neamt':234, 'Oradea':380, 'Pitesti':98, 'Rimnicu Vilcea':193, 
    'Sibiu':253, 'Timisoara':329, 'Urziceni':80, 'Vaslui':199, 'Zerind':374, 
}

def astar(start, goal):
    open_list=[]
    heapq.heappush(open_list,(heuristic[start],start))
    came_from={}
    g_cost={node:float('inf') for node in graph}
    g_cost[start]=0
    visited=[]
    closed=set()
    
    while open_list:
        f,current=heapq.heappop(open_list)
        if current in closed:
            continue
        closed.add(current)        
        visited.append(current)
        
        if current==goal:
            break
        
        for neighbor, cost in graph[current].items():
            new_cost=g_cost[current]+cost
            
            if new_cost<g_cost[neighbor]:
                g_cost[neighbor]=new_cost
                f_cost=new_cost+heuristic[neighbor]
                heapq.heappush(open_list,(f_cost,neighbor))
                came_from[neighbor]=current
    if g_cost[goal]==float('inf'):
        return [], visited, float('inf')
    
    path=[]
    node=goal
    while node!=start:
        path.append(node)
        node=came_from[node]
    path.append(start)
    path.reverse()
    return path,visited,g_cost[goal]

def draw_graph(path=None):
    G=nx.Graph()
    if path:
        for i in range(len(path)-1):
            city=path[i]
            neighbor=path[i+1]
            cost=graph[city][neighbor]
            G.add_edge(city, neighbor, weight=cost)
    else:
        for city in graph:
            for neighbor, cost in graph[city].items():
                G.add_edge(city,neighbor,weight=cost)
    
    pos={
        'Arad':(0,3),'Zerind':(0,4),'Oradea':(1, 4),'Sibiu':(2, 3),'Timisoara':(0, 2),
        'Lugoj':(1, 1),'Mehadia':(2, 0),'Drobeta':(3, 0),'Craiova':(4, 1),'Rimnicu Vilcea':(3, 2),
        'Fagaras':(4, 3),'Pitesti':(5, 2),'Bucharest':(6, 3),'Giurgiu':(6, 2),'Urziceni':(7, 3),
        'Hirsova':(8, 3),'Eforie':(9, 3),'Vaslui':(7, 4),'Iasi':(8, 5),'Neamt':(9, 6)
    }
    plt.figure(figsize=(10,7))
    edge_labels=nx.get_edge_attributes(G,'weight')
    
    nx.draw(G,pos,
            with_labels=True,
            node_color='orange',
            node_size=2000,
            font_size=10,
            font_weight='bold')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    plt.title("A*")
    plt.axis('off')
    plt.show()

def run_astar():
    start=start_entry.get().strip()
    # goal=goal_entry.get().strip()
    goal= "Bucharest"
    
    if start=="" or goal=="":
        messagebox.showerror("input error","input both source and destination")
        return
    start=start.title()
    goal=goal.title()
    
    if start not in graph:
        messagebox.showerror("error", "'"+start+"' is not a valid city")
        return
    if goal not in graph:
        messagebox.showerror("error", "'"+goal+"' is not a valid city")
        return
    # if start==goal:
    #     messagebox.showerror("error", "source and destination canot be the same")
    #     return
    path,visited,cost=astar(start,goal)
    result_text.delete(1.0, tk.END)

    result_text.insert(tk.END, "visited nodes are:\n")
    result_text.insert(tk.END, "->".join(visited))
    result_text.insert(tk.END, "\n\noptimal path is:\n")
    result_text.insert(tk.END, "->".join(path))
    result_text.insert(tk.END,"\n\npath cost is: "+str(cost))
    
    draw_graph(path)
    
def show_grah():
    draw_graph()
    
root=tk.Tk()
root.title("A* Algorithm(241080009_Akshat)")
root.geometry("500x500")
tk.Label(root, text="enter source city").pack()
start_entry=tk.Entry(root)
start_entry.pack()
tk.Label(root, text="Destination: Bucharest").pack(pady=5)
# goal_entry=tk.Entry(root)
# goal_entry.pack()

tk.Button(root, text="Run A*", command=run_astar).pack(pady=10)
tk.Button(root, text="show whole map", command=show_grah).pack(pady=10)

result_text=tk.Text(root,height=15)
result_text.pack()
root.mainloop()




# # 241080009_akshat_AI Lab4
# import tkinter as tk
# from tkinter import messagebox
# import networkx as nx
# import matplotlib.pyplot as plt
# import heapq

# graph = {
#     'Arad':{'Zerind':75, 'Sibiu':140, 'Timisoara':118},
#     'Bucharest':{'Fagaras':211, 'Pitesti':101, 'Giurgiu':90, 'Urziceni':85},
#     'Craiova':{'Drobeta':120, 'Rimnicu Vilcea':146, 'Pitesti':138},
#     'Drobeta':{'Mehadia':75, 'Craiova':120},
#     'Eforie':{'Hirsova':86},    
#     'Fagaras':{'Sibiu':99, 'Bucharest':211},
#     'Giurgiu':{'Bucharest':90},
#     'Hirsova':{'Urziceni':98, 'Eforie':86},
#     'Iasi':{'Vaslui':92, 'Neamt':87},
#     'Lugoj':{'Timisoara':111, 'Mehadia':70},
#     'Mehadia':{'Lugoj':70, 'Drobeta':75},
#     'Neamt':{'Iasi':87},
#     'Oradea':{'Zerind':71, 'Sibiu':151},
#     'Pitesti':{'Rimnicu Vilcea':97, 'Craiova':138, 'Bucharest':101},
#     'Rimnicu Vilcea':{'Sibiu':80, 'Craiova':146, 'Pitesti':97},
#     'Sibiu':{'Arad':140, 'Oradea':151, 'Fagaras':99, 'Rimnicu Vilcea':80},
#     'Timisoara':{'Arad':118, 'Lugoj':111},
#     'Urziceni':{'Bucharest':85, 'Hirsova':98, 'Vaslui':142},
#     'Vaslui':{'Urziceni':142, 'Iasi':92},
#     'Zerind':{'Arad':75, 'Oradea':71},
# }
# heuristic = {
#     'Arad':366, 'Bucharest':0, 'Craiova':160, 'Drobeta':242, 'Eforie':161,
#     'Fagaras':178, 'Giurgiu':77, 'Hirsova':151, 'Iasi':226, 'Lugoj':244,
#     'Mehadia':241, 'Neamt':234, 'Oradea':380, 'Pitesti':98, 'Rimnicu Vilcea':193, 
#     'Sibiu':253, 'Timisoara':329, 'Urziceni':80, 'Vaslui':199, 'Zerind':374, 
# }

# def astar(start, goal):
#     open_list=[]
#     heapq.heappush(open_list,(heuristic[start],start))
#     came_from={}
#     g_cost={node:float('inf') for node in graph}
#     g_cost[start]=0
#     visited=[]
#     closed=set()
    
#     while open_list:
#         f,current=heapq.heappop(open_list)
#         if current in closed:
#             continue
#         closed.add(current)        
#         visited.append(current)
        
#         if current==goal:
#             break
        
#         for neighbor, cost in graph[current].items():
#             new_cost=g_cost[current]+cost
            
#             if new_cost<g_cost[neighbor]:
#                 g_cost[neighbor]=new_cost
#                 f_cost=new_cost+heuristic[neighbor]
#                 heapq.heappush(open_list,(f_cost,neighbor))
#                 came_from[neighbor]=current
#     if g_cost[goal]==float('inf'):
#         return [], visited, float('inf')
    
#     path=[]
#     node=goal
#     while node!=start:
#         path.append(node)
#         node=came_from[node]
#     path.append(start)
#     path.reverse()
#     return path,visited,g_cost[goal]

# def draw_graph(path=None):
#     G=nx.Graph()
#     if path:
#         for i in range(len(path)-1):
#             city=path[i]
#             neighbor=path[i+1]
#             cost=graph[city][neighbor]
#             G.add_edge(city, neighbor, weight=cost)
#     else:
#         for city in graph:
#             for neighbor, cost in graph[city].items():
#                 G.add_edge(city,neighbor,weight=cost)
    
#     pos={
#         'Arad':(0,3),'Zerind':(0,4),'Oradea':(1, 4),'Sibiu':(2, 3),'Timisoara':(0, 2),
#         'Lugoj':(1, 1),'Mehadia':(2, 0),'Drobeta':(3, 0),'Craiova':(4, 1),'Rimnicu Vilcea':(3, 2),
#         'Fagaras':(4, 3),'Pitesti':(5, 2),'Bucharest':(6, 3),'Giurgiu':(6, 2),'Urziceni':(7, 3),
#         'Hirsova':(8, 3),'Eforie':(9, 3),'Vaslui':(7, 4),'Iasi':(8, 5),'Neamt':(9, 6)
#     }
#     plt.figure(figsize=(10,7))
#     edge_labels=nx.get_edge_attributes(G,'weight')
    
#     nx.draw(G,pos,
#             with_labels=True,
#             node_color='orange',
#             node_size=2000,
#             font_size=10,
#             font_weight='bold')
#     nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
#     plt.title("A*")
#     plt.axis('off')
#     plt.show()

# def run_astar():
#     start=start_entry.get().strip()
#     # goal=goal_entry.get().strip()
#     goal= "Bucharest"
    
#     if start=="" or goal=="":
#         messagebox.showerror("input error","input both source and destination")
#         return
#     start=start.title()
#     goal=goal.title()
    
#     if start not in graph:
#         messagebox.showerror("error", "'"+start+"' is not a valid city")
#         return
#     if goal not in graph:
#         messagebox.showerror("error", "'"+goal+"' is not a valid city")
#         return
#     # if start==goal:
#     #     messagebox.showerror("error", "source and destination canot be the same")
#     #     return
#     path,visited,cost=astar(start,goal)
#     result_text.delete(1.0, tk.END)

#     result_text.insert(tk.END, "visited nodes are:\n")
#     result_text.insert(tk.END, "->".join(visited))
#     result_text.insert(tk.END, "\n\noptimal path is:\n")
#     result_text.insert(tk.END, "->".join(path))
#     result_text.insert(tk.END,"\n\npath cost is: "+str(cost))
    
#     draw_graph(path)
    
# def show_grah():
#     draw_graph()
    
# root=tk.Tk()
# root.title("A* Algorithm(241080009_Akshat)")
# root.geometry("500x500")
# tk.Label(root, text="enter source city").pack()
# start_entry=tk.Entry(root)
# start_entry.pack()
# tk.Label(root, text="Destination: Bucharest").pack(pady=5)
# # goal_entry=tk.Entry(root)
# # goal_entry.pack()

# tk.Button(root, text="Run A*", command=run_astar).pack(pady=10)
# tk.Button(root, text="show whole map", command=show_grah).pack(pady=10)

# result_text=tk.Text(root,height=15)
# result_text.pack()
# root.mainloop()
