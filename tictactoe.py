import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        root.title("Tic Tac Toe Game")
        self.current_player = 'X'
        self.board = ['' for _ in range(9)]
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            btn = tk.Button(self.root, text='', font=('normal', 40), width=5, height=2, 
                            command=lambda i=i: self.on_button_click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def on_button_click(self, i):
        if self.board[i] == '' and not self.check_winner():
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif '' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                        (0, 4, 8), (2, 4, 6)]
        for a, b, c in win_patterns:
            if self.board[a] == self.board[b] == self.board[c] != '':
                return True
        return False

    def reset_game(self):
        self.current_player = 'X'
        self.board = ['' for _ in range(9)]
        for btn in self.buttons:
            btn.config(text='')

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
