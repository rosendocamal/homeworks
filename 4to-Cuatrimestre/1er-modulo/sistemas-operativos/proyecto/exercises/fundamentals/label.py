import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Label Widget Demo')

# Create a label
label = ttk.Label(root, text='This is a label', font=("Liberations", 8))
label.pack()

# Create image labels
photo = tk.PhotoImage(file='../assets/python.png')
image_label = ttk.Label(
    root,
    image=photo,
    text='Python',
    padding=5,
    compound=tk.TOP
)
image_label.pack(anchor='center')

root.mainloop()