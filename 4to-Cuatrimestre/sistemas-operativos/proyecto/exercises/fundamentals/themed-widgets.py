""" 
# Using the widget constructor when creating the widget
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
ttk.Label(root, text='Hi, there').pack()

root.mainloop() """

""" No me funcionó en Linux Fedora 44
# Using a dictionary index after widget creation
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label = ttk.Label(root)
label['text'] = 'Hi, there'
label.pack

root.mainloop()"""

"""
# Using the config() method with keyword arguments
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label = ttk.Label(root)
label.config(text='Hi, there')
label.pack()

root.mainloop()"""