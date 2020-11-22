from tkinter import *


WINDOW_BG = "#f4f4f2"
BUTTON_BG = "#e8e8e8"


root = Tk()
root.title("Password Manager")
root.config(padx=40, pady=40, bg=WINDOW_BG)

# Logo
canvas = Canvas(root, width=200, height=200, highlightthickness=0, bg=WINDOW_BG)
logo = PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
site_label = Label(root, text="Service/Website:", bg=WINDOW_BG)
site_label.grid(row=1, column=0, padx=5, pady=5)

username_label = Label(root, text="Email/Username:", bg=WINDOW_BG)
username_label.grid(row=2, column=0, padx=5, pady=5)

password_label = Label(root, text="Password:", bg=WINDOW_BG)
password_label.grid(row=3, column=0, padx=5, pady=5)

# Entries
site_entry = Entry(root, width=45)
site_entry.grid(row=1, column=1, columnspan=2, sticky=W)

username_entry = Entry(root, width=45)
username_entry.grid(row=2, column=1, columnspan=2, sticky=W)

password_entry = Entry(root, width=25)
password_entry.grid(row=3, column=1, sticky=W)

# Buttons
gen_btn = Button(root, text="Generate Password", bg=BUTTON_BG)
gen_btn.grid(row=3, column=2)

add_btn = Button(root, text="Add", width=42, bg=BUTTON_BG)
add_btn.grid(row=4, column=1, columnspan=2, pady=5)

root.mainloop()
