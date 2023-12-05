import tkinter as tk
from tkinter import messagebox
from dialogs import LoginDialog, ChatDialog  # Assuming dialogs.py is in the same directory

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chat Application")

        # Menu
        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Login", command=self.on_login)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.on_exit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.config(menu=self.menu_bar)

        # Status Bar
        self.status_bar = tk.Label(self, text="Not Connected", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Chat Dialog (hidden until login)
        self.chat_dialog = None

    def on_login(self):
        login_dialog = LoginDialog(self, title="Login")
        if login_dialog.result:
            username, password = login_dialog.result
            # Here, you'd normally authenticate the user
            self.status_bar.config(text=f"Logged in as {username}")
            self.open_chat_dialog()

    def open_chat_dialog(self):
        if not self.chat_dialog or not self.chat_dialog.winfo_exists():
            self.chat_dialog = ChatDialog(self)
            self.chat_dialog.protocol("WM_DELETE_WINDOW", self.on_chat_dialog_close)

    def on_chat_dialog_close(self):
        self.chat_dialog.destroy()
        self.chat_dialog = None

    def on_exit(self):
        self.destroy()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
