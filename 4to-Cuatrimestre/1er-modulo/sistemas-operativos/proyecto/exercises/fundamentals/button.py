import tkinter as tk
from tkinter import ttk

# main window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Button Demo')

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

from tkinter.messagebox import showinfo

def handle_click():
    showinfo(
        title='Information',
        message='Download button clicked!'
    )

download_icon = tk.PhotoImage(file='../assets/python.png')
download_button = ttk.Button(
    root,
    image=download_icon,
    command=handle_click
)

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()

