import sys
import sqlite3
from datetime import date
import variables
import functions
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

info_dic = {'p1_ready': False, 'p2_ready':False}

def create_regno(conn, c):
    c.execute('SELECT MAX(regno) FROM marriages;')
    regno = c.fetchone()[0] + 1
    conn.commit()
    return regno

def button_check_click():
    w.button_check.configure(state='disabled')

    p1_fname = w.entry_p1_fname.get().strip()
    p1_lname = w.entry_p1_lname.get().strip()
    p2_fname = w.entry_p2_fname.get().strip()
    p2_lname = w.entry_p2_lname.get().strip()
    info_dic['p1_fname'] = p1_fname
    info_dic['p1_lname'] = p1_lname
    info_dic['p2_fname'] = p2_fname
    info_dic['p2_lname'] = p2_lname

    if not (p1_fname and p1_lname and p2_fname and p2_lname):
        msgBox.showerror('Error', 'Please input all information!')
        w.button_check.configure(state='normal')
        return

    variables.cursor.execute('SELECT fname, lname FROM persons WHERE fname = ? collate nocase AND lname = ? collate nocase;', (p1_fname, p1_lname))
    p1 = variables.cursor.fetchone()
    if p1:
        p1_fname = p1[0]
        p1_lname = p1[1]
        info_dic['p1_fname'] = p1_fname
        info_dic['p1_lname'] = p1_lname
        info_dic['p1_ready'] = True
    else:
        w.button_p1_apply.configure(state='normal')
        w.entry_p1_bdate.configure(state='normal')
        w.entry_p1_bplace.configure(state='normal')
        w.entry_p1_address.configure(state='normal')
        w.entry_p1_phone.configure(state='normal')

    variables.cursor.execute('SELECT fname, lname FROM persons WHERE fname = ? collate nocase AND lname = ? collate nocase;', (p2_fname, p2_lname))
    p2 = variables.cursor.fetchone()
    if p2:
        p2_fname = p2[0]
        p2_lname = p2[1]
        info_dic['p2_fname'] = p2_fname
        info_dic['p2_lname'] = p2_lname
        info_dic['p2_ready'] = True
    else:
        w.button_p2_apply.configure(state='normal')
        w.entry_p2_bdate.configure(state='normal')
        w.entry_p2_bplace.configure(state='normal')
        w.entry_p2_address.configure(state='normal')
        w.entry_p2_phone.configure(state='normal')

    if info_dic['p1_ready'] and info_dic['p2_ready']:
        w.button_register.configure(state='normal')


def button_p1_apply_click():
    w.button_p1_apply.configure(state='disabled')
    info_dic['p1_ready'] = True

    p1_bdate = w.entry_p1_bdate.get().strip()
    p1_bplace = w.entry_p1_bplace.get().strip()
    p1_address = w.entry_p1_address.get().strip()
    p1_phone = w.entry_p1_phone.get().strip()

    variables.cursor.execute('INSERT INTO persons VALUES (?, ?, ?, ?, ?, ?);', (info_dic['p1_fname'], info_dic['p1_lname'], p1_bdate, p1_bplace, p1_address, p1_phone))
    if info_dic['p1_ready'] and info_dic['p2_ready']:
        w.button_register.configure(state='normal')

def button_p2_apply_click():
    w.button_p2_apply.configure(state='disabled')
    info_dic['p2_ready'] = True

    p2_bdate = w.entry_p2_bdate.get().strip()
    p2_bplace = w.entry_p2_bplace.get().strip()
    p2_address = w.entry_p2_address.get().strip()
    p2_phone = w.entry_p2_phone.get().strip()

    print('LOG:', 'formulated:', (info_dic['p2_fname'], info_dic['p2_lname'], p2_bdate, p2_bplace, p2_address, p2_phone))
    variables.cursor.execute('INSERT INTO persons VALUES (?, ?, ?, ?, ?, ?);', (info_dic['p2_fname'], info_dic['p2_lname'], p2_bdate, p2_bplace, p2_address, p2_phone))
    if info_dic['p1_ready'] and info_dic['p2_ready']:
        w.button_register.configure(state='normal')

def button_register_click():
    variables.cursor.execute('INSERT INTO marriages VALUES (?, DATE(\'now\'), ?, ?, ?, ?, ?);', (create_regno(variables.connection, variables.cursor), variables.user_city, info_dic['p1_fname'], info_dic['p1_lname'], info_dic['p2_fname'], info_dic['p2_lname']))
    try:
        variables.connection.commit()
        msgBox.showinfo('Success', 'Successfully registered!')
        print('LOG:', 'inserted:', 'birth record for', (info_dic['p1_fname'], info_dic['p1_lname']), 'and', (info_dic['p2_fname'], info_dic['p2_lname']))
    except:
        msgBox.showerror('Error', 'Database locked:\nPlease try again later!')
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
    import form_register_a_marriage
    form_register_a_marriage.vp_start_gui()