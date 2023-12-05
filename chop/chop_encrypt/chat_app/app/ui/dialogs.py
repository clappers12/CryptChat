import tkinter as tk
from tkinter import simpledialog

class LoginDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Username:").grid(row=0)
        tk.Label(master, text="Password:").grid(row=1)

        self.username = tk.Entry(master)
        self.password = tk.Entry(master, show="*")

        self.username.grid(row=0, column=1)
        self.password.grid(row=1, column=1)
        return self.username  # initial focus

    def apply(self):
        self.result = (self.username.get(), self.password.get())

class ChatDialog(tk.Toplevel):
    def __init__(self, parent, title="Chat"):
        super().__init__(parent)
        self.title(title)

        self.message_area = tk.Text(self, height=10, width=50, state=tk.DISABLED)
        self.message_area.pack()

        self.entry_field = tk.Entry(self, width=40)
        self.entry_field.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)

        self.send_button = tk.Button(self, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10)

    def send_message(self):
        message = self.entry_field.get()
        self.entry_field.delete(0, tk.END)
        # Here you would typically send the message to the server
        self.display_message(message)

    def display_message(self, message):
        self.message_area.configure(state=tk.NORMAL)
        self.message_area.insert(tk.END, f"{message}\n")
        self.message_area.configure(state=tk.DISABLED)
        self.message_area.see(tk.END)

# Example usage
if __name__ == "__main__":
    def on_login():
        username, password = login_dialog.result
        print(f"Logged in with username: {username}, password: {password}")
        chat_dialog = ChatDialog(root)
        chat_dialog.mainloop()

    root = tk.Tk()
    root.withdraw()  # Hide the main window
    login_dialog = LoginDialog(root, title="Login")
    root.after(0, on_login)
    root.mainloop()
