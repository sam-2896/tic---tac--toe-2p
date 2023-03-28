import tkinter as tk
from tkinter import messagebox
class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        master.title("0-X Game")

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = []

        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(master, text=" ", width=5, height=2,
                                   font=("Helvetica", 20, "bold"),
                                   command=lambda row=row, col=col: self.handle_click(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def handle_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.has_won():
                tk.messagebox.showinfo("Congratulations!", f"{self.current_player} has won!")
                self.reset()
            elif self.is_tie():
                tk.messagebox.showinfo("Tie!", "The game is a tie.")
                self.reset()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def has_won(self):
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)):
                return True
            if all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if all(self.board[i][2-i] == self.current_player for i in range(3)):
            return True
        return False

    def is_tie(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def reset(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")

root = tk.Tk()
tictactoe = TicTacToeGUI(root)
root.mainloop()
