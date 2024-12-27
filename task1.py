import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts a message using the Caesar cipher algorithm.

    :param text: The input message
    :param shift: The shift value for the cipher
    :param mode: 'encrypt' for encryption, 'decrypt' for decryption
    :return: The transformed text
    """
    if mode == "decrypt":
        shift = -shift
    result = ""

    for char in text:
        if char.isalpha():  
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  

    return result

def process_message(mode):
    text = message_entry.get()
    shift_value = shift_entry.get()

    if not text:
        messagebox.showerror("Error", "Please enter a message.")
        return

    try:
        shift = int(shift_value)
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer.")
        return

    result = caesar_cipher(text, shift, mode)
    result_label.config(text=f"Result: {result}")

app = tk.Tk()
app.title("Caesar Cipher")


frame = tk.Frame(app, padx=10, pady=10)
frame.pack()


tk.Label(frame, text="Message:").grid(row=0, column=0, sticky="w")
message_entry = tk.Entry(frame, width=30)
message_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Shift Value:").grid(row=1, column=0, sticky="w")
shift_entry = tk.Entry(frame, width=10)
shift_entry.grid(row=1, column=1, pady=5)
encrypt_button = tk.Button(frame, text="Encrypt", command=lambda: process_message("encrypt"))
encrypt_button.grid(row=2, column=0, pady=10)

decrypt_button = tk.Button(frame, text="Decrypt", command=lambda: process_message("decrypt"))
decrypt_button.grid(row=2, column=1, pady=10)
result_label = tk.Label(app, text="Result:", padx=10, pady=10)
result_label.pack()
app.mainloop()
