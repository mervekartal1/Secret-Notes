import base64
import os
import tkinter
from tkinter import *
from tkinter import messagebox


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec_bytes = base64.urlsafe_b64decode(enc.encode()).decode()
    dec = []
    for i in range(len(dec_bytes)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(dec_bytes[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def decrypt_notes():
    message_encrypted = title2_entry.get("1.0", END).strip()
    master_secret = title3_entry.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error", message="Please enter all info")
    else:
        try:
            decrypted_message = decode(master_secret, message_encrypted)
            title2_entry.delete("1.0", END)
            title2_entry.insert("1.0", decrypted_message)
        except Exception:
            messagebox.showerror(title="Error", message="Please make sure of encrypted text!")


def save_and_encrypt_notes():
    title = title_entry.get()
    message = title2_entry.get("1.0", END).strip()
    master_secret = title3_entry.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showerror("Error", "Please enter all required information")
    else:
        message_encrypted = encode(master_secret, message)

        # Masaüstü yolunu belirleme
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, "mysecret.txt")

        # Masaüstündeki dosyaya yazma
        with open(file_path, "a", encoding="utf-8") as myfile:
            myfile.write(f"\n{title}\n{message_encrypted}")

        # Alanları temizleme
        title_entry.delete(0, END)
        title2_entry.delete("1.0", END)
        title3_entry.delete(0, END)

window = tkinter.Tk()
window.title("Secret Notes")
window.config(padx=50, pady=50)

# User Interface
try:
    photo = PhotoImage(file="1.png")
    photo_label = tkinter.Label(window, image=photo)
    photo_label.pack()
except Exception:
    pass

FONT = ("Verdana", 12)
title_input_label = tkinter.Label(window, text="Enter your title", font=FONT)
title_input_label.pack()

title_entry = tkinter.Entry(window, width=30)
title_entry.pack()

title2_input_label = tkinter.Label(window, text="Enter your secret note", font=FONT)
title2_input_label.pack()

title2_entry = tkinter.Text(window, width=30, height=5)
title2_entry.pack()

title3_input_label = tkinter.Label(window, text="Enter master key", font=FONT)
title3_input_label.pack()

title3_entry = tkinter.Entry(window, width=30)
title3_entry.pack()

save_button = tkinter.Button(window, text="Save & Encrypt", command=save_and_encrypt_notes)
save_button.pack()

decrypt_button = tkinter.Button(window, text="Decrypt", command=decrypt_notes)
decrypt_button.pack()

window.mainloop()


