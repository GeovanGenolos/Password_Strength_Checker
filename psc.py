import string
import getpass
import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = password_entry.get()
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    # Providing remarks based on the strength of your password
    if strength == 1:
        remarks = ('That\'s a very bad password.'
                   ' Change it as soon as possible.')
    elif strength == 2:
        remarks = ('That\'s a weak password.'
                   ' You should consider using a tougher password.')
    elif strength == 3:
        remarks = 'Your password is okay, but it can be improved.'
    elif strength == 4:
        remarks = ('Your password is hard to guess.'
                   ' But you could make it even more secure.')
    elif strength == 5:
        remarks = ('Now that\'s one strong password!!!'
                   ' Hackers don\'t have a chance guessing that password!')

    messagebox.showinfo("Password Strength", 
                        f"Your password has:\n{lower_count} lowercase letters\n{upper_count} uppercase letters\n{num_count} digits\n{wspace_count} whitespaces\n{special_count} special characters\nPassword Score: {strength / 5}\nRemarks: {remarks}")

def on_submit():
    check_password_strength()
    password_entry.delete(0, tk.END)

if __name__ == '__main__':
    
    root = tk.Tk()
    root.title("Password Strength Checker")

    root.geometry("400x300")  

    label = tk.Label(root, text="Enter your password:")
    label.pack(pady=10)

    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    submit_button = tk.Button(root, text="Check Password", command=on_submit)
    submit_button.pack(pady=10)

    root.mainloop()
