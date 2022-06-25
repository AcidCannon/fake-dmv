import sys
import variables
import tkinter.messagebox as msgBox
from datetime import date
import sqlite3

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
    tno = w.entry_tno.get().strip()
    if not tno:
        msgBox.showerror("Error", "Please input tno!")
    elif not tno.isnumeric():
        msgBox.showerror("Error", "Please input numeric tno!")
    else:
        variables.cursor.execute('SELECT fine FROM tickets WHERE tno = ?;', (tno,))
        fine = variables.cursor.fetchall()
        variables.cursor.execute('SELECT IFNULL(SUM(amount),0) FROM payments WHERE tno = ?;', (tno,))
        paid = variables.cursor.fetchall()
        if fine and paid:
            fine = fine[0]
            paid = paid[0]
            w.entry_fine.configure(state='normal')
            w.entry_paid.configure(state='normal')
            w.entry_fine.insert(0, fine)
            w.entry_paid.insert(0, paid)
            w.entry_fine.configure(state='readonly')
            w.entry_paid.configure(state='readonly')
            w.entry_tno.configure(state='readonly')
            w.entry_amount.configure(state='normal')
            w.button_pay.configure(state='normal')
            w.button_check.configure(state='disabled')
            # check tno validity and disable entry box
        else:
            # no corresponding record, thus cannot pay
            msgBox.showerror("Error", "No matching record!")

def button_pay_click():
    amount = w.entry_amount.get().strip()
    paid = w.entry_paid.get().strip()
    fine = w.entry_fine.get().strip()
    tno = w.entry_tno.get().strip()
    if not amount:
        msgBox.showerror("Error", "Please input amount!")
    elif not amount.isnumeric():
        msgBox.showerror("Error", "Please input numeric amount!")
    else:
        if int(paid) + int(amount) > int(fine):
            msgBox.showerror("Error", "Your payment exceed the fine!")
            return
        else:
            try:
                variables.cursor.execute('INSERT INTO payments VALUES (?, DATE(\'now\'), ?);', (tno, amount))
                variables.connection.commit()
                print('LOG:', 'Payments inserted for', tno)
                destroy_window()
                msgBox.showinfo('Success', 'Successfully paid!');
            except:
                msgBox.showerror("Error", "You can only pay once in a day, please try another day!")
                print('LOG:', 'Payments failed for', tno)
                destroy_window()

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
    import form_process_a_payment
    form_process_a_payment.vp_start_gui()
