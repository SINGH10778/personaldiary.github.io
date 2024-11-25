import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3
from tkinter import font

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('personal_diary.db')
cursor = conn.cursor()

# Create a table for storing diary entries if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS diary_entries
                  (id INTEGER PRIMARY KEY, title TEXT, content TEXT)''')
conn.commit()

# Function to add a new diary entry
def add_entry():
    title = simpledialog.askstring("Title", "Enter the title of your diary entry:")
    if title:
        content = simpledialog.askstring("Content", "Enter the content of your diary entry:")
        if content:
            cursor.execute("INSERT INTO diary_entries (title, content) VALUES (?, ?)", (title, content))
            conn.commit()
            load_entries()
        else:
            messagebox.showwarning("Input Error", "Content cannot be empty.")
    else:
        messagebox.showwarning("Input Error", "Title cannot be empty.")

# Function to delete a selected diary entry
def delete_entry():
    selected_entry = entry_listbox.curselection()
    if selected_entry:
        entry_id = entry_listbox.get(selected_entry[0]).split(' - ')[0]
        cursor.execute("DELETE FROM diary_entries WHERE id=?", (entry_id,))
        conn.commit()
        load_entries()
    else:
        messagebox.showwarning("Selection Error", "Please select an entry to delete.")

# Function to load all diary entries into the listbox
def load_entries():
    entry_listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM diary_entries")
    entries = cursor.fetchall()
    for entry in entries:
        entry_listbox.insert(tk.END, f"{entry[0]} - {entry[1]}")

# Function to view the selected diary entry
def view_entry():
    selected_entry = entry_listbox.curselection()
    if selected_entry:
        entry_id = entry_listbox.get(selected_entry[0]).split(' - ')[0]
        cursor.execute("SELECT title, content FROM diary_entries WHERE id=?", (entry_id,))
        entry = cursor.fetchone()
        messagebox.showinfo(entry[0], entry[1])  # Show title and content in a popup
    else:
        messagebox.showwarning("Selection Error", "Please select an entry to view.")

# Create the main window
root = tk.Tk()
root.title("Personal Diary")
root.geometry("600x500")
root.config(bg="#f1f1f1")

# Define font styles
header_font = font.Font(family="Arial", size=18, weight="bold")
button_font = font.Font(family="Arial", size=14)

# Add a stylish title label
title_label = tk.Label(root, text="My Personal Diary", font=header_font, bg="#F39C12", fg="white", pady=10)
title_label.pack(fill="both")

# Create the diary entry listbox
entry_listbox = tk.Listbox(root, width=60, height=15, font=("Arial", 12), bd=2, relief="solid", bg="#ECF0F1", selectmode=tk.SINGLE)
entry_listbox.pack(padx=20, pady=20)

# Add a frame for the buttons for better organization
button_frame = tk.Frame(root, bg="#f1f1f1")
button_frame.pack()

# Add stylish buttons with icons
add_button = tk.Button(button_frame, text="Add Entry", font=button_font, command=add_entry, bg="#27AE60", fg="white", relief="flat", width=20, height=2)
add_button.grid(row=0, column=0, padx=10, pady=5)

view_button = tk.Button(button_frame, text="View Entry", font=button_font, command=view_entry, bg="#3498DB", fg="white", relief="flat", width=20, height=2)
view_button.grid(row=0, column=1, padx=10, pady=5)

delete_button = tk.Button(button_frame, text="Delete Entry", font=button_font, command=delete_entry, bg="#E74C3C", fg="white", relief="flat", width=20, height=2)
delete_button.grid(row=1, column=0, padx=10, pady=5)

# Load all entries into the listbox on startup
load_entries()

# Start the Tkinter main loop
root.mainloop()

# Close the database connection when the program is closed
conn.close()
