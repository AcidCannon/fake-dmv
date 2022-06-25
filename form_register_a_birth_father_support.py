import sys
import variables

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def button_apply_click():
    bdate = w.entry_bdate.get().strip()
    bplace = w.entry_bplace.get().strip()
    address = w.entry_address.get().strip()
    phone = w.entry_phone.get().strip()
    variables.cursor.execute('INSERT INTO persons VALUES (?, ?, ?, ?, ?, ?);', (variables.father['fname'], variables.father['lname'], bdate, bplace, address, phone))
    destroy_window()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    w.entry_fname.configure(state='normal')
    w.entry_lname.configure(state='normal')
    w.entry_fname.insert(0, variables.father['fname'])
    w.entry_lname.insert(0, variables.father['lname'])
    w.entry_fname.configure(state='readonly')
    w.entry_lname.configure(state='readonly')

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import form_register_a_birth_father
    form_register_a_birth_father.vp_start_gui()