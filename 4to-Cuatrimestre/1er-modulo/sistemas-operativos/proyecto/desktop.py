import tkinter as tk
from tkinter import messagebox
import time

class Desktop:
    def __init__(self, root):
        self.root = root
        self.screen_width = int(root.winfo_screenwidth() * 0.5)
        self.screen_height = int(root.winfo_screenheight() * 0.5)
        x = self.screen_width // 2
        y = self.screen_height // 2

        self.root.title("SESSION INIT")
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+{x}+{y}")
        self.root.resizable(False, False)
        self.root.maxsize(1920, 1080)
        self.root.configure(bg="#9209C8")


        # Authentication & Authorization
        self.login = tk.Frame(self.root, bg="#CE63F8", bd=2, relief="groove")
        self.login.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=self.screen_width, height=self.screen_height)

        tk.Label(self.login, text="USER LOGIN", font=("Arial", 35, "bold"), bg="#CE63F8", fg="white").pack(expand=True)


        tk.Label(self.login, text='@rosendocamal', font=("Arial", 20, "bold"), bg="#CE63F8", fg="white").pack()

        
        self.entry_password = tk.Entry(self.login, font=("Arial", 20), bd=2, show="*")
        self.entry_password.pack(pady=15)
        self.entry_password.focus()
        
        # Login button
        btn_login = tk.Button(self.login, text="LOGIN", font=("Arial", 20, "bold"), bg="#F527C8", fg="white", activebackground="#E9BBFC", activeforeground="white", relief="flat", command=self.auth)
        btn_login.pack(expand=True)
        

        self.root.bind('<Return>', lambda event: self.auth())


        # Screensave
        self.screensave = tk.Frame(self.root, bg="#CE63F8", bd=2, relief="groove")
        self.screensave.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=self.screen_width, height=self.screen_height)

        self.clock_label = tk.Label(self.screensave, bg="#CE63F8", fg="white", font=("Arial", 50))
        self.clock_label.pack(anchor=tk.CENTER, expand=True)
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)

        self.date_label = tk.Label(self.screensave, bg="#CE63F8", fg="white", font=("Arial", 35))
        self.date_label.pack(anchor=tk.CENTER, expand=True)
        current_date = time.strftime("%A %B %d")
        self.date_label.config(text=current_date)

        self.root.bind('<Return>', lambda event: self.screensave.destroy())

    def auth(self):
        password = "1234"
        
        if self.entry_password.get() == password:
            self.login.destroy()
            self.root.unbind('<Return>')
            self.load_desktop()
        else:
            messagebox.showerror("ACCESS ERROR", "INCORRECT PASSWORD!")

    def load_desktop(self):
        self.root.title("DESKTOP USER")
        
        self.desktop = tk.Frame(self.root, bg="#520570", highlightthickness=0)
        self.desktop.pack(anchor=tk.CENTER, fill=tk.BOTH, expand=False)        

        self.taskbar = tk.Frame(self.root, bg="#72079C", height=self.screen_height*0.1)
        self.taskbar.pack(fill=tk.X, side=tk.BOTTOM, anchor=tk.CENTER)
        self.taskbar.pack_propagate(False)

        selected_option = tk.StringVar()
        options = ('REBOOT', 'POWER OFF', 'LOG OUT')
        self.menu_button = tk.Menubutton(self.taskbar, text="START", direction="above", bg="#BB27F5", fg="white", font=("Arial", 12, "bold"), activebackground="#72079C", activeforeground="white", relief="flat")
        menu = tk.Menu(self.menu_button, tearoff=0, bg="#BB27F5", fg="white", font=("Arial", 12, "bold"))
        for option in options:
            menu.add_radiobutton(
                label=option,
                value=option,
                variable=selected_option,
                command=lambda option=option: self.menu_options(option)
            )

        self.menu_button["menu"] = menu
        self.menu_button.pack(side=tk.LEFT, fill=tk.Y)
        

        self.time_label = tk.Label(self.taskbar, bg="#72079C", fg="white", font=("Arial", 11, "bold"))
        self.time_label.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=5)
        self.update_clock()

  
        self.create_icon("ŧ\nObsidian", self.open_note)
        self.create_icon("ð\nCalculadora", self.open_calc)

    def update_clock(self):
        clock = time.strftime("%H:%M:%S")
        date = time.strftime("%Y-%m-%d")
        self.time_label.config(text=f"{clock}\n{date}")
        self.root.after(1000, self.update_clock)

    def create_icon(self, name_icon, command):
        btn_icon = tk.Button(self.taskbar, text=name_icon, font=("Arial", 12), bg="#CE63F8", fg="white", activebackground="#B20BF4", activeforeground="white", bd=0, relief="flat", cursor="hand2", command=command)
        btn_icon.pack(side="left", fill=tk.Y, ipadx=5)

    def menu_options(self, option):
        match option:
            case 'LOG OUT':
                answer = messagebox.askyesno("LOG OUT", "¿You want to log out?")
                if answer:
                    self.__init__(self.root)
                    time.sleep(2)
                    self.desktop.destroy()
                    self.taskbar.destroy()

            case 'REBOOT':
                answer = messagebox.askyesno("REBOOT", "¿You want to reboot now?")
                if answer:
                    self.__init__(self.root)
                    time.sleep(3)
                    self.desktop.destroy()
                    self.taskbar.destroy()
                    time.sleep(2)
                    

                    import os
                    os.system('reboot')
            case 'POWER OFF':
                answer = messagebox.askyesno("POWER OFF", "¿You want to shutdown now?")
                if answer:
                    self.root.quit()
                    time.sleep(0.5)
                    self.desktop.destroy()
                    time.sleep(0.5)
                    self.taskbar.destroy()
                    time.sleep(1)


                    import os
                    os.system('shutdown now')
            case _:
                pass

    def open_note(self):
        import os
        os.system('flatpak run md.obsidian.Obsidian &')

    def open_calc(self):
        import os
        os.system('gnome-calculator &')
  
if __name__ == "__main__":
    root = tk.Tk()
    app = Desktop(root)
    root.mainloop()