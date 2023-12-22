import tkinter as tk

window = tk.Tk()
message = tk.Label(text='Hello', foreground='black', background='red')
button = tk.Button(text='Click Me', width=25, height=5, background='blue', foreground='white')
message.pack()
button.pack()
window.mainloop()