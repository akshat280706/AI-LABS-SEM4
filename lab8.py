#241080009-Akshat-IT
import tkinter as tk
from tkinter import messagebox

size=4
world={
    (0,3):"w",
    (2,2):"p",
    (3,1):"p",
    (3,3):"g"
}
player_pos=(0,0)
visited=set()
safe=set()
danger=set()
game_over=False
buttons={}

def get_percepts(x,y):
    percepts=[]
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx,ny=x+dx,y+dy
        if(nx,ny) in world:
            if world[(nx,ny)]=="w":
                percepts.append("stench")
            if world[(nx,ny)]=="p":
                percepts.append("breeze")
    return percepts

def is_adjacent(x,y):
    px,py=player_pos
    return abs(px-x)+abs(py-y)==1

def click_cell(x,y):
    global player_pos,game_over
    if game_over:
        return
    if(x,y)!=(0,0) and not is_adjacent(x,y):
        return
    player_pos=(x,y)
    reveal_cell(x,y)
    
def reveal_cell(x,y):
    global game_over
    cell=(x,y)
    visited.add(cell)
    
    for b in buttons.values():
        b.config(relief="raised")
    buttons[cell].config(relief="sunken")
    
    if cell in world:
        if world[cell]=="w":
            buttons[cell].config(text="wumpus",bg="red")
            messagebox.showerror("haha bye","wumpus loved you")
            game_over=True
            reveal_all()
            return
        
        if world[cell]=="p":
            buttons[cell].config(text="pit",bg="red")
            messagebox.showerror("booo","pitFall")
            game_over=True
            reveal_all()
            return
        
        if world[cell]=="g":
            buttons[cell].config(text="gold",bg="yellow")
            messagebox.showerror("damnn","you found gold")
            game_over=True
            reveal_all()
            return
        
    if cell not in world:
        percepts=get_percepts(x,y)
        text="\n".join(percepts) if percepts else "safe"
        buttons[cell].config(text=text, bg="lightgreen")
    infer(x,y,percepts)
    update_display()
    update_info()

def infer(x,y,percepts):
    neighbors=[]
    for dx,dy in [(-1,0),(1,0,),(0,-1),(0,1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<size and 0<=ny<size:
            neighbors.append((nx,ny))
    
    if not percepts:
        for n in neighbors:
            safe.add(n)
    else:
        for n in neighbors:
            if n not in safe:
                danger.add(n)
    safe.add((x,y))

def update_display():
    for cell in safe:
        if cell not in visited:
            buttons[cell].config(bg="lightblue")
    for cell in danger:
        if cell not in visited:
            buttons[cell].config(bg="pink")

def update_info():
    text=f"visited:{visited}\nsafe:{safe}\ndanger:{danger}"
    info_label.config(text=text)

def reveal_all():
    for cell,value in world.items():
        if value=="w":
            buttons[cell].config(text="w",bg="orange")
        
        if value=="p":
            buttons[cell].config(text="p",bg="brown")
        
        if value=="g":
            buttons[cell].config(text="g",bg="yellow")

root=tk.Tk()
root.title("241080009-Akshat-Wumpus")

for i in range(size):
    for j in range(size):
        btn=tk.Button(root,text="dk",width=10,height=4,
                    command=lambda x=i,y=j:click_cell(x,y))
        btn.grid(row=i,column=j)
        buttons[(i,j)]=btn

info_label=tk.Label(root,text="",justify="left",font=("Arial",10))        
info_label.grid(row=size,column=0,columnspan=size)
reveal_cell(0,0)
root.mainloop()        
