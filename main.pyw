import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

boss_list = []


def add_boss():
    boss_name = boss_entry.get()

    if boss_name:
        boss_list.append({"name": boss_name, "deaths": 0})
        boss_entry.delete(0, tk.END)
        update_boss_list()
    else:
        messagebox.showwarning("Empty Field", "Please enter a boss name.")


def remove_boss():
    selected_boss = boss_listbox.curselection()

    if selected_boss:
        boss_index = selected_boss[0]
        boss_list.pop(boss_index)
        update_boss_list()


def increment_deaths():
    selected_boss = boss_listbox.curselection()

    if selected_boss:
        boss_index = selected_boss[0]
        boss_list[boss_index]["deaths"] += 1
        update_boss_list()
        boss_listbox.selection_set(
            boss_index
        )  # Select the boss after incrementing deaths


def update_boss_list():
    boss_listbox.delete(0, tk.END)
    for boss in boss_list:
        boss_name = boss["name"]
        boss_deaths = boss["deaths"]
        boss_listbox.insert(tk.END, f"{boss_name} ({boss_deaths} deaths)")


def save_bosses():
    with open("bosses.json", "w") as file:
        json.dump(boss_list, file)


def load_bosses():
    global boss_list
    try:
        with open("bosses.json", "r") as file:
            boss_list = json.load(file)
    except FileNotFoundError:
        boss_list = []


# Load bosses from the JSON file
load_bosses()

# Create the main window
window = tk.Tk()
window.title("Boss Tracker")

# Set the style and theme
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TLabel", font=("Segoe UI", 12), padding=6)
style.configure("TEntry", font=("Segoe UI", 10), padding=6)
style.configure("TListbox", font=("Segoe UI", 10), padding=6)

# Create and pack the boss listbox
boss_listbox = tk.Listbox(window, height=10, width=30)
boss_listbox.pack(pady=10)

# Create and pack the boss entry field
boss_entry = ttk.Entry(window, width=30)
boss_entry.pack(pady=5)

# Create and pack the add boss button
add_button = ttk.Button(window, text="Add Boss", command=add_boss)
add_button.pack(pady=5)

# Create and pack the remove boss button
remove_button = ttk.Button(window, text="Remove Boss", command=remove_boss)
remove_button.pack(pady=5)

# Create and pack the increment deaths button
increment_button = ttk.Button(window, text="Add Death", command=increment_deaths)
increment_button.pack(pady=5)

# Update the boss list
update_boss_list()


# Define the on closing function
def on_closing():
    save_bosses()
    window.destroy()


# Add the on closing function to the window
window.protocol("WM_DELETE_WINDOW", on_closing)

# Start the main event loop
window.mainloop()
