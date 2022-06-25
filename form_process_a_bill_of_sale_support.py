import sys
import variables
import sqlite3
import tkinter.messagebox as msgBox
from datetime import date

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

def button_current_owner_click():
    vin = w.entry_vin.get().strip()
    current_owner_fname = w.entry_cur_fname.get().strip()
    current_owner_lname = w.entry_cur_lname.get().strip()
    if vin and current_owner_fname and current_owner_lname:
        variables.cursor.execute('SELECT fname, lname FROM registrations WHERE vin = ? collate nocase Order by  expiry Desc Limit 1;', (vin,))
        owner = variables.cursor.fetchone()
        if not owner:
            msgBox.showerror("Error", "There is no car matching this vin!")
            return
        else:
            f = owner[0].upper()
            l = owner[1].upper()
            if ((current_owner_fname.upper() != f) or (current_owner_lname.upper() != l)):
                msgBox.showerror("Error", "Owner name doesn't match!")
                return
            else:
                w.entry_vin.configure(state='readonly')
                w.entry_cur_fname.configure(state='readonly')
                w.entry_cur_lname.configure(state='readonly')
                w.button_current_owner.configure(state='disabled')
                w.button_new_owner.configure(state='normal')
                w.entry_new_fname.configure(state='normal')
                w.entry_new_lname.configure(state='normal')
                w.entry_plate.configure(state='normal')
    else:
        msgBox.showerror("Error", "Fname/lname/vin cannot be empty!")

def button_new_owner_click():
    new_owner_fname = w.entry_new_fname.get().strip()
    new_owner_lname = w.entry_new_lname.get().strip()
    new_plate = w.entry_plate.get().strip()
    if new_owner_fname and new_owner_lname and new_plate:
        variables.cursor.execute('SELECT fname, lname FROM persons WHERE fname = ? collate nocase AND lname = ? collate nocase;', (new_owner_fname, new_owner_lname))
        fetched = variables.cursor.fetchone()
        if not fetched:
            destroy_window()
            msgBox.showerror("Error", "Cannot found new owner, transaction failed!")
            return
        variables.new_owner_fname = fetched[0]
        variables.new_owner_lname = fetched[1]
        w.entry_plate.configure(state='readonly')
        w.entry_new_fname.configure(state='readonly')
        w.entry_new_lname.configure(state='readonly')
        w.button_new_owner.configure(state='disabled')
        w.button_process.configure(state='normal')
    else:
        msgBox.showerror("Error", "Fname/lname/plate cannot be empty!")

def button_process_click():
    vin = w.entry_vin.get().strip()
    current_owner_fname = w.entry_cur_fname.get().strip()
    current_owner_lname = w.entry_cur_lname.get().strip()
    new_plate = w.entry_plate.get().strip()
    variables.cursor.execute('SELECT MAX(regno) FROM registrations;')
    regno = variables.cursor.fetchone()[0] + 1
    variables.cursor.execute('UPDATE registrations SET expiry = DATE(\'now\') WHERE vin = ? collate nocase AND fname = ? collate nocase AND lname = ? collate nocase;', (vin, current_owner_fname, current_owner_lname))
    variables.cursor.execute('INSERT INTO registrations VALUES (?, DATE(\'now\'), DATE(\'now\', \'+1 years\'), ?, ?, ?, ?);', (regno, new_plate, vin, variables.new_owner_fname, variables.new_owner_lname))
    variables.connection.commit()
    print('LOG:', 'Transfer complete:', (vin, current_owner_fname, current_owner_lname, variables.new_owner_fname, variables.new_owner_lname, new_plate, regno))
    destroy_window()
    msgBox.showinfo('Success', 'Successfully processed the bill of sale!');

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import form_process_a_bill_of_sale
    form_process_a_bill_of_sale.vp_start_gui()