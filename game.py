import tkinter as tk
from tkinter import messagebox

# Khởi tạo cửa sổ
root = tk.Tk()
root.title("Caro 3x3 - Tic Tac Toe")
root.geometry("300x350")

# Biến điều khiển
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Kiểm tra thắng
def check_win(player):
    # Check hàng, cột
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    # Check đường chéo
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Kiểm tra hòa
def is_draw():
    return all(board[i][j] != "" for i in range(3) for j in range(3))

# Xử lý khi người chơi click ô
def handle_click(row, col):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")

        if check_win(current_player):
            messagebox.showinfo("Kết quả", f"🎉 Người chơi {current_player} thắng!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Kết quả", "⚖️ Hòa!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.config(text=f"Lượt của người chơi: {current_player}")

# Reset game
def reset_game():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    status_label.config(text="Lượt của người chơi: X")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")

# Giao diện - nút bấm
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", width=6, height=3, font=("Helvetica", 24),
                        command=lambda r=i, c=j: handle_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = btn

# Label trạng thái
status_label = tk.Label(root, text="Lượt của người chơi: X", font=("Helvetica", 14))
status_label.grid(row=3, column=0, columnspan=3, pady=10)

# Chạy ứng dụng
root.mainloop()
