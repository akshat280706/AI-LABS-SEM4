#241080009-Akshat Chauhan
import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def check_winner(board):
    wins=[(0,1,2),(3,4,5),(6,7,8),
          (0,3,6),(1,4,7),(2,5,8),
          (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a]==board[b]==board[c] and board[a]!=" ":
            return board[a]
    if " " not in board:
            return "draw"
    return None

visited_nodes=0
pruned_nodes=0

def minimax(board, is_max, alpha,beta):
    global visited_nodes, pruned_nodes
    visited_nodes+=1
    winner=check_winner(board)
    if winner =="O":
        return 1
    if winner =="X":
        return -1
    if winner =="draw":
        return 0
    
    if is_max:
        best=-float("inf")
        for i in range(9):
            if board[i]==" ":
                board[i]="O"
                val=minimax(board,False,alpha,beta)
                board[i]=" "
                best=max(best,val)
                alpha=max(alpha,best)
                
                if beta<=alpha:
                    pruned_nodes+=1
                    break
        return best
    else:
        best=float("inf")
        for i in range(9):
            if board[i]==" ":
                board[i]="X"
                val=minimax(board,True,alpha,beta)
                board[i]=" "
                best=min(best,val)
                beta=min(beta,best)
                if beta<=alpha:
                    pruned_nodes+=1
                    break
        return best

def build_tree(board):
    G=nx.DiGraph()
    root="".join(board)
    G.add_node(root, label=root+"\na=-inf b=+inf")
    best_score=-float("inf")
    best_node=None
    alpha=-float("inf")
    beta=float("inf")
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            score=minimax(board,False,alpha,beta)
            child="".join(board)
            label=child+ "\na=" +str(alpha)+ "b=" +str(beta)+ "\nscore="+str(score)
            G.add_node(child, label=label)
            G.add_edge(root,child)
            
            if score>best_score:
                best_score=score
                best_node=child
                alpha=max(alpha,best_score)
            board[i]=" "
    return G,root,best_node

def tree_layout(G,root):
    pos={}
    def dfs(node,depth,x):
        children=list(G.successors(node))
        if not children:
            pos[node]=(x,-depth)
            return x+1
        start=x
        for child in children:
            x=dfs(child,depth+1,x)
            
        mid=(start+x-1)/2
        pos[node]=(mid,-depth)
        return x
    dfs(root,0,0)
    return pos    

def draw_graph(G,root,best_node):
    for widget in graph_frame.winfo_children():
        widget.destroy()
    fig, ax=plt.subplots(figsize=(7,5))
    pos=tree_layout(G,root)
    labels=nx.get_node_attributes(G,'label')
    node_colors=[]
    for node in G.nodes():
        if node==root:
            node_colors.append("skyblue")
        elif node==best_node:
            node_colors.append("lightgreen")
        else:
            node_colors.append("lightcoral")
    edge_colors=[]
    for u,v in G.edges():
        if v==best_node:
            edge_colors.append("green")
        else:
            edge_colors.append("blue")
    
    nx.draw(G,pos, labels=labels, with_labels=True,
            node_color=node_colors,edge_color=edge_colors,
            node_size=2500, font_size=8, ax=ax)
    ax.set_title("alpha-beta pruning")
    canvas=FigureCanvasTkAgg(fig,master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def check_game_over():
    result=check_winner(board)
    if result:
        if result=="draw":
            messagebox.showinfo("over","it is a draw")
        else:
            messagebox.showinfo("over",result+"won")
        for btn in buttons:
            btn.config(state="disabled")

def computer_move():
    global visited_nodes, pruned_nodes
    visited_nodes=0
    pruned_nodes=0
    G,root,best_node=build_tree(board)
    print("nodes visited: ", visited_nodes)
    print("pruned nodes: ", pruned_nodes)
    print(" ")
    
    for i in range(9):
        if board[i]==" ":
            temp=board[:]
            temp[i]="O"
            if"".join(temp)==best_node:
                board[i]="O"
                buttons[i]["text"]="O"
                break
    draw_graph(G,root,best_node)
    check_game_over()

def play_move(i):
    if board[i]==" ":
        board[i]="X"
        buttons[i]["text"]="X"
        check_game_over()
        if not check_winner(board):
            computer_move()

root=tk.Tk()
root.title("241080009_akshat_Alpha-Beta")
board=[" "]*9
buttons=[]
board_frame=tk.Frame(root)
board_frame.pack(side="left",padx=10)
for i in range(9):
    btn=tk.Button(board_frame,text=" ",width=5,
                  height=2, command=lambda i=i: play_move(i))
    btn.grid(row=i//3,column=i%3)
    buttons.append(btn)
graph_frame=tk.Frame(root)
graph_frame.pack(side="right",padx=10)
import sys
def close():
    root.destroy()
    sys.exit()
root.protocol("WM_DELETE_WINDOW",close)
root.mainloop()
        
# #241080009-Akshat Chauhan
# import tkinter as tk
# from tkinter import messagebox
# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# def check_winner(board):
#     wins=[(0,1,2),(3,4,5),(6,7,8),
#           (0,3,6),(1,4,7),(2,5,8),
#           (0,4,8),(2,4,6)]
#     for a,b,c in wins:
#         if board[a]==board[b]==board[c] and board[a]!=" ":
#             return board[a]
#     if " " not in board:
#             return "draw"
#     return None

# visited_nodes=0
# pruned_nodes=0

# def minimax(board, is_max, alpha,beta):
#     global visited_nodes, pruned_nodes
#     visited_nodes+=1
#     winner=check_winner(board)
#     if winner =="O":
#         return 1
#     if winner =="X":
#         return -1
#     if winner =="draw":
#         return 0
    
#     if is_max:
#         best=-float("inf")
#         for i in range(9):
#             if board[i]==" ":
#                 board[i]="O"
#                 val=minimax(board,False,alpha,beta)
#                 board[i]=" "
#                 best=max(best,val)
#                 alpha=max(alpha,best)
                
#                 if beta<=alpha:
#                     pruned_nodes+=1
#                     break
#         return best
#     else:
#         best=float("inf")
#         for i in range(9):
#             if board[i]==" ":
#                 board[i]="X"
#                 val=minimax(board,True,alpha,beta)
#                 board[i]=" "
#                 best=min(best,val)
#                 beta=min(beta,best)
#                 if beta<=alpha:
#                     pruned_nodes+=1
#                     break
#         return best

# def build_tree(board):
#     G=nx.DiGraph()
#     root="".join(board)
#     G.add_node(root, label=root+"\na=-inf b=+inf")
#     best_score=-float("inf")
#     best_node=None
#     alpha=-float("inf")
#     beta=float("inf")
#     for i in range(9):
#         if board[i]==" ":
#             board[i]="O"
#             score=minimax(board,False,alpha,beta)
#             child="".join(board)
#             label=child+ "\na=" +str(alpha)+ "b=" +str(beta)+ "\nscore="+str(score)
#             G.add_node(child, label=label)
#             G.add_edge(root,child)
            
#             if score>best_score:
#                 best_score=score
#                 best_node=child
#                 alpha=max(alpha,best_score)
#             board[i]=" "
#     return G,root,best_node

# def tree_layout(G,root):
#     pos={}
#     def dfs(node,depth,x):
#         children=list(G.successors(node))
#         if not children:
#             pos[node]=(x,-depth)
#             return x+1
#         start=x
#         for child in children:
#             x=dfs(child,depth+1,x)
            
#         mid=(start+x-1)/2
#         pos[node]=(mid,-depth)
#         return x
#     dfs(root,0,0)
#     return pos    

# def draw_graph(G,root,best_node):
#     for widget in graph_frame.winfo_children():
#         widget.destroy()
#     fig, ax=plt.subplots(figsize=(7,5))
#     pos=tree_layout(G,root)
#     labels=nx.get_node_attributes(G,'label')
#     node_colors=[]
#     for node in G.nodes():
#         if node==root:
#             node_colors.append("skyblue")
#         elif node==best_node:
#             node_colors.append("lightgreen")
#         else:
#             node_colors.append("lightcoral")
#     edge_colors=[]
#     for u,v in G.edges():
#         if v==best_node:
#             edge_colors.append("green")
#         else:
#             edge_colors.append("blue")
    
#     nx.draw(G,pos, labels=labels, with_labels=True,
#             node_color=node_colors,edge_color=edge_colors,
#             node_size=2500, font_size=8, ax=ax)
#     ax.set_title("alpha-beta pruning")
#     canvas=FigureCanvasTkAgg(fig,master=graph_frame)
#     canvas.draw()
#     canvas.get_tk_widget().pack()

# def check_game_over():
#     result=check_winner(board)
#     if result:
#         if result=="draw":
#             messagebox.showinfo("over","it is a draw")
#         else:
#             messagebox.showinfo("over",result+"won")
#         for btn in buttons:
#             btn.config(state="disabled")

# def computer_move():
#     global visited_nodes, pruned_nodes
#     visited_nodes=0
#     pruned_nodes=0
#     G,root,best_node=build_tree(board)
#     print("nodes visited: ", visited_nodes)
#     print("pruned nodes: ", pruned_nodes)
#     print(" ")
    
#     for i in range(9):
#         if board[i]==" ":
#             temp=board[:]
#             temp[i]="O"
#             if"".join(temp)==best_node:
#                 board[i]="O"
#                 buttons[i]["text"]="O"
#                 break
#     draw_graph(G,root,best_node)
#     check_game_over()

# def play_move(i):
#     if board[i]==" ":
#         board[i]="X"
#         buttons[i]["text"]="X"
#         check_game_over()
#         if not check_winner(board):
#             computer_move()

# root=tk.Tk()
# root.title("241080009_akshat_Alpha-Beta")
# board=[" "]*9
# buttons=[]
# board_frame=tk.Frame(root)
# board_frame.pack(side="left",padx=10)
# for i in range(9):
#     btn=tk.Button(board_frame,text=" ",width=5,
#                   height=2, command=lambda i=i: play_move(i))
#     btn.grid(row=i//3,column=i%3)
#     buttons.append(btn)
# graph_frame=tk.Frame(root)
# graph_frame.pack(side="right",padx=10)
# import sys
# def close():
#     root.destroy()
#     sys.exit()
# root.protocol("WM_DELETE_WINDOW",close)
# root.mainloop()
        
