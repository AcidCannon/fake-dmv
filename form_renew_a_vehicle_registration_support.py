import sys
import datetime
import variables
import tkinter.messagebox as msgBox

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

def button_check_click():
    # remove starting and trailing space
    regno = w.entry_regno.get().strip()
    if not regno:
        msgBox.showerror("Error", "Please input regno!")
    elif not regno.isnumeric():
        msgBox.showerror("Error", "Please input numeric regno!")
    else:
        variables.cursor.execute('SELECT expiry FROM registrations WHERE regno = ?;', (regno,))
        result = variables.cursor.fetchall()
        if result:
            result = result[0]
            w.entry_expiry.configure(state='normal')
            w.entry_expiry.insert(0, result)
            w.entry_regno.configure(state='readonly')
            w.entry_expiry.configure(state='readonly')
            w.button_renew.configure(state='normal')
            w.button_check.configure(state='disabled')
            # check regno validity and disable entry box
        else:
            # no corresponding record, thus cannot renew
            msgBox.showerror("Error", "No matching record!")

def button_renew_click():
    regno = w.entry_regno.get().strip()
    expiry = w.entry_expiry.get().strip()
    # yyyy-mm-dd
    # 0123456789
    # transform string expiry date into native comparable date
    exp = datetime.datetime(int(expiry[:4]), int(expiry[5:7]), int(expiry[8:]))
    today = datetime.datetime.now()
    if today >= exp:
        # (today, today + 1 year)
        variables.cursor.execute('UPDATE registrations SET expiry=date(?, ?) WHERE regno=?;',('now', '+1 years', regno))
    else:
        # (expiry, expiry + 1 year)
        variables.cursor.execute('UPDATE registrations SET expiry=date(?, ?) WHERE regno=?;',(expiry, '+1 years', regno))
    variables.connection.commit()
    print('LOG:', 'Registrations updated for', regno)
    destroy_window()
    msgBox.showinfo('Success', 'Registration successfully renewed!');

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
    import form_renew_a_vehicle_registration
    form_renew_a_vehicle_registration.vp_start_gui()