import tkinter as tk
import time

class TrafficLight:
    def __init__(self, root):
        self.root = root
        self.root.title("Mô phỏng đèn giao thông")

        self.canvas = tk.Canvas(root, width=200, height=400, bg='gray')
        self.canvas.pack()

        # Vẽ khung đèn
        self.canvas.create_rectangle(50, 50, 150, 350, fill='black')

        # Vẽ các bóng đèn (red, yellow, green)
        self.red_light = self.canvas.create_oval(70, 70, 130, 130, fill='gray')
        self.yellow_light = self.canvas.create_oval(70, 160, 130, 220, fill='gray')
        self.green_light = self.canvas.create_oval(70, 250, 130, 310, fill='gray')

        self.update_lights()

    def update_lights(self):
        while True:
            # Đèn đỏ sáng
            self.canvas.itemconfig(self.red_light, fill='red')
            self.canvas.itemconfig(self.yellow_light, fill='gray')
            self.canvas.itemconfig(self.green_light, fill='gray')
            self.root.update()
            time.sleep(7)

            # Đèn vàng sáng
            self.canvas.itemconfig(self.red_light, fill='gray')
            self.canvas.itemconfig(self.yellow_light, fill='yellow')
            self.canvas.itemconfig(self.green_light, fill='gray')
            self.root.update()
            time.sleep(3)

            # Đèn xanh sáng
            self.canvas.itemconfig(self.red_light, fill='gray')
            self.canvas.itemconfig(self.yellow_light, fill='gray')
            self.canvas.itemconfig(self.green_light, fill='green')
            self.root.update()
            time.sleep(10)

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficLight(root)
