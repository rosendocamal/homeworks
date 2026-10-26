import tkinter as tk

root = tk.Tk()
root.title('Title Place Geometry Manager')
root.geometry("600x400")

# Absolute positioning
label1 = tk.Label(master=root, text="Place", bg='red', fg='white')
label1.place(x=0, y=0, width=120, height=60)

# Relative positioning
label2 = tk.Label(master=root, text="Place", bg='red', fg='white')
label2.place(relx=0.5, rely=0.5, width=120, height=60)

label3 = tk.Label(master=root, text="Place", bg='blue', fg='white')
label3.place(relx=0.8, rely=0.8, width=120, height=60, anchor=tk.CENTER)

root.mainloop()