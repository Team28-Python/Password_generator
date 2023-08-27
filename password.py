import random
import tkinter as tk


class PasswordGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")
        self.root.geometry("400x300")

        self.label_length = tk.Label(self.root, text="Password Length:")
        self.entry_length = tk.Entry(self.root)
        self.label_symbols = tk.Label(self.root, text="Include Symbols:")
        self.checkbox_symbols = tk.Checkbutton(self.root, text="Yes")
        self.label_numbers = tk.Label(self.root, text="Include Numbers:")
        self.checkbox_numbers = tk.Checkbutton(self.root, text="Yes")
        self.label_uppercase = tk.Label(self.root, text="Include Uppercase:")
        self.checkbox_uppercase = tk.Checkbutton(self.root, text="Yes")
        self.label_lowercase = tk.Label(self.root, text="Include Lowercase:")
        self.checkbox_lowercase = tk.Checkbutton(self.root, text="Yes")
        self.button_generate = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.label_password = tk.Label(self.root, text="Generated Password:")
        self.entry_password = tk.Entry(self.root, width=30)

        self.label_length.grid(row=0, column=0)
        self.entry_length.grid(row=0, column=1)
        self.label_symbols.grid(row=1, column=0)
        self.checkbox_symbols.grid(row=1, column=1)
        self.label_numbers.grid(row=2, column=0)
        self.checkbox_numbers.grid(row=2, column=1)
        self.label_uppercase.grid(row=3, column=0)
        self.checkbox_uppercase.grid(row=3, column=1)
        self.label_lowercase.grid(row=4, column=0)
        self.checkbox_lowercase.grid(row=4, column=1)
        self.button_generate.grid(row=5, column=0)
        self.label_password.grid(row=6, column=0)
        self.entry_password.grid(row=6, column=1)

        self.root.mainloop()

    def generate_password(self):
        length = int(self.entry_length)
        symbols = bool(self.checkbox_symbols)
        numbers = bool(self.checkbox_numbers)
        uppercase = bool(self.checkbox_uppercase)
        lowercase = bool(self.checkbox_lowercase)
        password = ""
        for i in range(length):
            char = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()-_=+")
            if symbols and char in string.punctuation:
                continue
            if numbers and char.isdigit():
                continue
            if uppercase and char.isupper():
                continue

            password += char

        self.entry_password.delete(0, END)
        self.entry_password.insert(0, password)


if __name__ == "__main__":
    PasswordGenerator()

