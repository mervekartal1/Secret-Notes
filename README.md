<img width="687" height="1102" alt="Ekran görüntüsü 2026-08-28 150545" src="https://github.com/user-attachments/assets/b6229fd7-2736-4d60-95c1-455b457783cb" />


# 🔐 Secret Notes

Secret Notes is a simple desktop application built with Python and Tkinter that allows users to create, encrypt, save, and decrypt private notes using a master key.

## ✨ Features

- Create a note with a custom title
- Encrypt notes using a master key
- Save encrypted notes to a text file
- Decrypt previously encrypted notes
- Simple graphical user interface (GUI)
- Input validation and error messages

## 🛠️ Technologies

- Python
- Tkinter
- Base64
- OS module

## 🔒 How It Works

The application uses a master key to encrypt and decrypt notes.

When a note is saved:

1. The user enters a title, secret note, and master key.
2. The note is encrypted using the master key.
3. The encrypted note is encoded with Base64.
4. The encrypted note is saved to `mysecret.txt` on the Desktop.

To decrypt a note:

1. Enter the encrypted text.
2. Enter the same master key used during encryption.
3. Click the **Decrypt** button.
4. The original note is displayed in the text box.

## 🚀 How to Run

Make sure Python is installed on your computer.

Clone this repository:

```bash
git clone https://github.com/mervekartal1/Secret-Notes.git
