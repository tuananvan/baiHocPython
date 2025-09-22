from tkinter import *
import random

# Khởi tạo cửa sổ
random.seed()
root = Tk()
root.title('Tài xỉu')
root.geometry("400x320")

# Danh sách mặt xúc xắc Unicode
dice_faces = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

# Biến thống kê
total_rolls = 0
tai_count = 0
xiu_count = 0

# Label hiển thị xúc xắc và kết quả
dice_label = Label(root, font=("Helvetica", 100))
result_label = Label(root, font=("Helvetica", 40))
stat_label = Label(root, font=("Helvetica", 14), justify=LEFT)

def roll():
    global total_rolls, tai_count, xiu_count

    # Quay xúc xắc
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    total = d1 + d2 + d3

    # Cập nhật hiển thị xúc xắc
    dice_label.config(text=f'{dice_faces[d1-1]}{dice_faces[d2-1]}{dice_faces[d3-1]}')
    dice_label.pack()

    # Kiểm tra kết quả và cập nhật thống kê
    if total > 10:
        result = "Tài"
        color = "red"
        tai_count += 1
    else:
        result = "Xỉu"
        color = "green"
        xiu_count += 1

    total_rolls += 1

    # Hiển thị kết quả
    result_label.config(text=result, foreground=color)
    result_label.pack(after=dice_label)

    # Hiển thị thống kê
    stat_text = f"Số lần quay: {total_rolls}\nTài: {tai_count} lần\nXỉu: {xiu_count} lần"
    stat_label.config(text=stat_text)
    stat_label.pack(after=result_label)

# Nút quay
b1 = Button(root, text="Quay tài xỉu", foreground='blue', font=("Helvetica", 14), command=roll)
b1.pack(pady=10)

# Chạy chương trình
root.mainloop()
