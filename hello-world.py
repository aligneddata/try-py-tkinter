from tkinter import *
from tkinter import ttk

def on_search():
    pass

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# Search entry and button
search_entry = ttk.Entry(frm, width=50)
search_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=11)
search_button = ttk.Button(frm, text="Search", command=on_search)
search_button.grid(row=1, column=11, padx=1, pady=5)

root.mainloop()