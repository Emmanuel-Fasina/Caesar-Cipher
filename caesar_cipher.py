import tkinter as tk
from tkinter import messagebox


class CaesarCipherApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Emmanuel Caesar Cipher Encryptor")

        self.entry_text = tk.Entry(self.window, width=40)
        self.entry_text.pack(pady=20)

        self.label_result = tk.Label(self.window, text="Encrypted Message: ")
        self.label_result.pack(pady=10)

        self.label_prompt = tk.Label(self.window, text="Enter your message:")
        self.label_prompt.pack(pady=10)

        self.btn_encrypt = tk.Button(self.window, text="Encrypt", command=self.encrypt_message)
        self.btn_encrypt.pack(pady=10)

    def encrypt_message(self):
        text = self.entry_text.get()
        cipher = ""

        if not text:
            messagebox.showerror("Input Error", "Please enter a message to encrypt.")
            return

        for char in text:
            if not char.isalpha():
                continue
            char = char.upper()
            codes = ord(char) + 1
            if codes > ord("Z"):
                codes = ord("A")
            cipher += chr(codes)

        self.label_result['text'] = f"Encrypted Message: {cipher}"


def main():
    window = tk.Tk()
    CaesarCipherApp(window)
    window.mainloop()


main()
