import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai

API_KEY = "AIzaSyDn95xef2pIW1c5UMTzMh22tUgDO0df8UY"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chat_window.insert(tk.END, f"You: {user_input}\n")
    entry.delete(0, tk.END)

    try:
        response = chat.send_message(user_input)
        chat_window.insert(tk.END, f"GPT: {response.text}\n\n")
        chat_window.see(tk.END)
    except Exception as e:
        chat_window.insert(tk.END, f"Error: {str(e)}\n")

root = tk.Tk()
root.title("Chat GPT do Đặng Minh Tuấn viết")
root.geometry("600x500")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(padx=10, pady=(0,10), fill=tk.X)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Gửi", font=("Arial", 14), command=send_message)
send_button.pack(pady=(0,10))

root.mainloop()
