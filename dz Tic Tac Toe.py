import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.winning_combination = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.animate_winner()
                self.show_message(f"Игрок {self.current_player} победил!")
                self.root.after(3000, self.reset_board)
            elif "" not in self.board:
                self.show_message("Ничья!")
                self.root.after(3000, self.reset_board)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "":
                self.winning_combination = condition
                return True
        return False

    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", bg="SystemButtonFace")
        self.current_player = "X"
        self.winning_combination = []

    def animate_winner(self):
        colors = ["lightgreen", "green", "darkgreen"]
        for color in colors:
            for index in self.winning_combination:
                self.buttons[index].config(bg=color)
            self.root.update()
            self.root.after(500)

    def show_message(self, message):
        message_label = tk.Label(self.root, text=message, font=('normal', 20), fg="blue")
        message_label.grid(row=3, column=0, columnspan=3)
        self.root.after(2000, message_label.grid_forget)  


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
