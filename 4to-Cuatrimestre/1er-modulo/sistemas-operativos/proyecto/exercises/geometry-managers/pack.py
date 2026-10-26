"""import tkinter as tk

root = tk.Tk()
root.title('Tkinter Pack Layout')
root.geometry('600x400')

# label1 = tk.Label(root, text='Tkinter', bg='red', fg='white')
# label2 = tk.Label(root, text='Pack Layout', bg='green', fg='white')
# label3 = tk.Label(root, text='Demo', bg='blue', fg='white')
# label4 = tk.Label(root, text='Label 4', bg='black', fg='white')

# label1.pack(side=tk.TOP, expand=True, fill=tk.X)
# label2.pack(side=tk.BOTTOM, expand=True, fill=tk.Y)
# label3.pack(side=tk.LEFT, expand=True, fill=tk.NONE)
# label4.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# from tkinter import ttk
# name_label = ttk.Label(root, text="Name: ")
# name_label.pack(side=tk.LEFT)

# name_entry = ttk.Entry(root)
# name_entry.pack(side=tk.LEFT)

# button = ttk.Button(root, text="Submit")
# button.pack(side=tk.LEFT)


from tkinter import ttk
label1 = tk.Label(root, text='Pack', bg='red', fg='white')
label2 = tk.Label(root, text='Pack', bg='green', fg='white')
label3 = tk.Label(root, text='Pack', bg='blue', fg='white')
label4 = tk.Label(root, text='Pack', bg='purple', fg='white')

label1.pack(side=tk.LEFT, padx=10, pady=10, anchor='n')
label2.pack(side=tk.LEFT, ipadx=40, padx=20, pady=20, anchor='e')
label3.pack(side=tk.LEFT, ipady=40, padx=30, pady=30, anchor='s')
label4.pack(side=tk.LEFT, ipadx=40, ipady=40, padx=40, pady=40, anchor='w')

root.mainloop()"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Login')
root.geometry("1920x1080")

fields = {}

fields['username_label'] = ttk.Label(root, text='Username:')
fields['username'] = ttk.Entry(root)

fields['password_label'] = ttk.Label(root, text='Passoword:')
fields['password'] = ttk.Entry(root, show="*")

for field in fields.values():
    field.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

ttk.Button(text='Login').pack(anchor=tk.W, padx=10, pady=10)

root.mainloop()