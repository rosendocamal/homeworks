import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window Demo')

window_width = 300
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False) # Evita que sea dinámico el tamaño de la ventana

root.minsize(600, 400) # Asigna tamaño dinámico mínimo de la ventana
root.maxsize(1980, 1080) # Asigna tamaño dinámico máximo de la ventana
root.attributes('-alpha', 0.5) # Especifica transparencia de la ventana

# Ensure icon is in the assets folder relative in my script.
#root.iconbitmap('./assets/pythontutorial.ico')

try:
    # Use iconphoto on Linux and macOS
    photo = tk.PhotoImage(file="./assets/pythontutorial.png")
    root.iconphoto(False, photo)
except tk.TclError:
    print("icon file not found")

root.mainloop()