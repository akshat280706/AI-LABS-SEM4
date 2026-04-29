

def check_winner(board):
    wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a]==board[b]==board[c] and board[a]!=" ":
            return board[a]
        if " " not in board:
            return "draw"
        return None

visited_nodes=0
pruned_nodes=0

def minimax(board,is_max,alpha,beta):
    global visited_nodes,pruned_nodes
    visited_nodes+=1
    winner=check_winner(board)
    if winner=="0":
        return 1
    if winner=="X":
        return -1
    if winner=="draw":
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
    