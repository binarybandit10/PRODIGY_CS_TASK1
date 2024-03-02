import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    if mode == "encrypt":
        return result
    elif mode == "decrypt":
        return caesar_cipher(result, -shift, "encrypt")

def encrypt_text():
    message = message_entry.get()
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(message, shift, "encrypt")
    result_label.config(text=encrypted_text)

def decrypt_text():
    message = message_entry.get()
    shift = int(shift_entry.get())
    decrypted_text = caesar_cipher(message, shift, "decrypt")
    result_label.config(text=decrypted_text)

root = tk.Tk()
root.title("Caesar Cipher")

frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

message_label = ttk.Label(frame, text="Message:")
message_label.grid(row=0, column=0, sticky="w")
message_entry = ttk.Entry(frame, width=30)
message_entry.grid(row=0, column=1, padx=(0, 10))

shift_label = ttk.Label(frame, text="Shift:")
shift_label.grid(row=1, column=0, sticky="w")
shift_entry = ttk.Entry(frame, width=5)
shift_entry.grid(row=1, column=1, padx=(0, 10))

encrypt_button = ttk.Button(frame, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=2, column=0, padx=(0, 10))

decrypt_button = ttk.Button(frame, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=2, column=1, padx=(0, 10))

result_frame = ttk.Frame(frame, padding="10")
result_frame.grid(row=3, column=0, columnspan=2, padx=(0, 10))

result_label = ttk.Label(result_frame, text="")
result_label.pack()

root.mainloop()