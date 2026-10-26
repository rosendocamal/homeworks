import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.title('Entry Widget Demo')


name_label = ttk.Label(root, text="Name:")
name_label.pack(pady=2)

name_entry = ttk.Entry(root)
name_entry.pack()

email_label = ttk.Label(root, text='Email:')
email_label.pack(pady=2)

email_entry = ttk.Entry(root)
email_entry.pack(pady=5)
email_entry.focus()

password_label = ttk.Label(root, text='Password:')
password_label.pack(pady=2)

password_entry = ttk.Entry(root, show='*')
password_entry.pack(pady=5)

root.mainloop()
