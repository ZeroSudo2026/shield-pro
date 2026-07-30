import tkinter as tk
from tkinter import messagebox
import random, string

def generate_key():
    key = "SHIELD-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=4)) + "-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)

def activate_license():
    if len(key_entry.get().strip()) > 5:
        messagebox.showinfo("License Status", "Activation Successful! 🛡️\nProtection is Active.")
    else:
        messagebox.showerror("Error", "Invalid License Key!")

root = tk.Tk()
root.title("Shield Pro V2.0")
root.geometry("400x320")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="🛡️ Shield Pro V2.0", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="#00FF66")
title.pack(pady=20)

key_entry = tk.Entry(root, font=("Consolas", 12), width=24, justify="center")
key_entry.pack(pady=10)

btn1 = tk.Button(root, text="Generate License Key", command=generate_key, bg="#333333", fg="#FFFFFF", font=("Arial", 10))
btn1.pack(pady=8)

btn2 = tk.Button(root, text="Activate License", command=activate_license, bg="#00FF66", fg="#000000", font=("Arial", 10, "bold"))
btn2.pack(pady=10)

root.mainloop()
