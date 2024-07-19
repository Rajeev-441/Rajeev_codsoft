import tkinter as tk
from tkinter import messagebox
import numpy as np

# Constants
PLAYER = 'X'
AI = 'O'
EMPTY = ' '

# Initialize the board
board = np.full((3, 3), EMPTY)

def check_winner(b, player):
    for row in b:
        if all([cell == player for cell in row]):
            return True
    for col in b.T:
        if all([cell == player for cell in col]):
            return True
    if all([b[i, i] == player for i in range(3)]) or all([b[i, 2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(b):
    return not any(EMPTY in row for row in b)

def minimax(b, depth, is_maximizing, alpha, beta):
    if check_winner(b, AI):
        return 1
    if check_winner(b, PLAYER):
        return -1
    if is_board_full(b):
        return 0
    
    if is_maximizing:
        max_eval = -np.inf
        for i in range(3):
            for j in range(3):
                if b[i, j] == EMPTY:
                    b[i, j] = AI
                    eval = minimax(b, depth + 1, False, alpha, beta)
                    b[i, j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = np.inf
        for i in range(3):
            for j in range(3):
                if b[i, j] == EMPTY:
                    b[i, j] = PLAYER
                    eval = minimax(b, depth + 1, True, alpha, beta)
                    b[i, j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move():
    best_val = -np.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i, j] == EMPTY:
                board[i, j] = AI
                move_val = minimax(board, 0, False, -np.inf, np.inf)
                board[i, j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def on_click(row, col):
    if board[row, col] == EMPTY:
        board[row, col] = PLAYER
        buttons[row][col].config(text=PLAYER)
        if check_winner(board, PLAYER):
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations! You win!")
            root.quit()
        elif is_board_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            root.quit()
        else:
            ai_move = best_move()
            if ai_move:
                board[ai_move[0], ai_move[1]] = AI
                buttons[ai_move[0]][ai_move[1]].config(text=AI)
                if check_winner(board, AI):
                    messagebox.showinfo("Tic-Tac-Toe", "You lose! AI wins!")
                    root.quit()
                elif is_board_full(board):
                    messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                    root.quit()

# Set up the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        button = tk.Button(root, text='', font='normal 20 bold', height=3, width=6,
                           command=lambda i=i, j=j: on_click(i, j))
        button.grid(row=i, column=j)
        buttons[i][j] = button

# Start the application
root.mainloop()
