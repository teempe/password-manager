from tkinter import *
from tkinter import messagebox
import repository
import password


WINDOW_BG = "#f4f4f2"
BUTTON_BG = "#e8e8e8"


def is_entry_valid(service, username, password):
    if service == "" or username == "" or password == "":
        return False
    return True


def clear_entries():
    site_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)


def save_data():
    service = site_entry.get()
    user = username_entry.get()
    password = password_entry.get()

    if is_entry_valid(service, user, password):
        answer = messagebox.askyesno(service, f"User: {user}\nPassword: {password}\nIs it OK to save?")
        if answer:
            repository.save(service, user, password)
            clear_entries()
            messagebox.showinfo("Success", "Data have been saved.")
    else:
        messagebox.showerror("Error", "Please fill all fields.")


def get_password():
    new_password = password.generate_password()
    password_entry.insert(0, new_password)


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
site_entry.focus()
site_entry.grid(row=1, column=1, columnspan=2, sticky=W)

username_entry = Entry(root, width=45)
username_entry.grid(row=2, column=1, columnspan=2, sticky=W)

password_entry = Entry(root, width=25)
password_entry.grid(row=3, column=1, sticky=W)

# Buttons
gen_btn = Button(root, text="Generate Password", bg=BUTTON_BG, command=get_password)
gen_btn.grid(row=3, column=2)

add_btn = Button(root, text="Add", width=42, bg=BUTTON_BG, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2, pady=5)

root.mainloop()
