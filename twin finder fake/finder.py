import tkinter as tk

# 1. Initialize the main window application
root = tk.Tk()
root.title("My First Python GUI")
root.geometry("400x200")  # Width x Height in pixels

# 2. Define functionality (Callback Function)
def on_submit():
    user_text = entry.get()
    result_label.config(text=f"Hello, {user_text}!")

# 3. Create visual components (Widgets)
title_label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
title_label.pack(pady=5)  # pack() handles layout spacing

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

submit_btn = tk.Button(root, text="Submit", command=on_submit, bg="lightblue")
submit_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# 4. Run the endless application event loop
root.mainloop()
