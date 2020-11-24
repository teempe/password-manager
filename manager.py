from tkinter import *
from tkinter import messagebox
from repository import JsonRepository
import password


WINDOW_BG = "#f4f4f2"
BUTTON_BG = "#e8e8e8"


def is_entry_valid(service, username, password):
    if service == "" or username == "" or password == "":
        return False
    return True


def clear_all_entries():
    site_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)


def save_data():
    service = site_entry.get()
    user = username_entry.get()
    password = password_entry.get()

    if is_entry_valid(service, user, password):
        storage.save(service, user, password)
        clear_all_entries()
        messagebox.showinfo("Success!", "Data have been saved.")
    else:
        messagebox.showerror("Error!", "Please fill all fields.")
    del_btn.config(state=DISABLED)


def find_data():
    service = site_entry.get()
    if service == "":
        messagebox.showerror("Error!", "Please fill search field.")
        return

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    results = storage.find(service)
    if results is None:
        messagebox.showerror("Error", f"No details of the {service} or no data file found.")
    else:
        username_entry.insert(0, results[1])
        password_entry.insert(0, results[2])
        del_btn.config(state=ACTIVE)


def delete_data():
    service = site_entry.get()
    if storage.delete(service):
        clear_all_entries()
        messagebox.showinfo("Success!", f"All data for {service} have been deleted.")
    else:
        messagebox.showerror("Error", f"No details of the {service} or no data file found.")
    del_btn.config(state=DISABLED)


def get_password():
    new_password = password.generate_password()
    password_entry.insert(0, new_password)

storage = JsonRepository()

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
site_entry = Entry(root, width=25)
site_entry.focus()
site_entry.grid(row=1, column=1, sticky=W)

username_entry = Entry(root, width=45)
username_entry.grid(row=2, column=1, columnspan=2, sticky=W)

password_entry = Entry(root, width=25)
password_entry.grid(row=3, column=1, sticky=W)

# Buttons
search_btn = Button(root, text="Search", bg=BUTTON_BG, width=16, command=find_data)
search_btn.grid(row=1, column=2)

gen_btn = Button(root, text="Generate Password", bg=BUTTON_BG, command=get_password)
gen_btn.grid(row=3, column=2)

add_btn = Button(root, text="Add / Update", width=42, bg=BUTTON_BG, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2, pady=5)

del_btn = Button(root, text="Delete", width=42, bg=BUTTON_BG, state=DISABLED, command=delete_data)
del_btn.grid(row=5, column=1, columnspan=2, pady=5)

root.mainloop()
