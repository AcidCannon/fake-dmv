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

def create_regno(conn, c):
    c.execute('SELECT MAX(regno) FROM births;')
    regno = c.fetchone()[0] + 1
    conn.commit()
    return regno

def button_availability_click():
    fname = w.entry_fname.get().strip()
    lname = w.entry_lname.get().strip()
    gender = w.entry_gender.get().strip()
    bdate = w.entry_bdate.get().strip()
    bplace = w.entry_bplace.get().strip()
    f_fname = w.entry_f_fname.get().strip()
    f_lname = w.entry_f_lname.get().strip()
    m_fname = w.entry_m_fname.get().strip()
    m_lname = w.entry_m_lname.get().strip()

    if not (fname and lname and gender and bdate and bplace and f_fname and f_lname and m_fname and m_lname):
        msgBox.showerror('Error', 'Please input all information!')
        return

    variables.cursor.execute('SELECT * FROM persons WHERE fname = ? collate nocase AND lname = ? collate nocase;', (fname, lname))
    newborn = variables.cursor.fetchone()
    if newborn:
        destroy_window()
        msgBox.showerror('Error', 'Abort:\nNewborn with same name has already exist in database!')
        return
    w.button_availability.configure(state='disabled')
    w.button_mother.configure(state='normal')
    w.entry_fname.configure(state='readonly')
    w.entry_lname.configure(state='readonly')
    w.entry_gender.configure(state='readonly')
    w.entry_bdate.configure(state='readonly')
    w.entry_bplace.configure(state='readonly')
    w.entry_f_fname.configure(state='readonly')
    w.entry_f_lname.configure(state='readonly')
    w.entry_m_fname.configure(state='readonly')
    w.entry_m_lname.configure(state='readonly')

def button_mother_click():
    m_fname = w.entry_m_fname.get().strip()
    m_lname = w.entry_m_lname.get().strip()
    w.button_mother.configure(state='disabled')
    w.button_father.configure(state='normal')
    variables.cursor.execute('SELECT fname, lname FROM persons WHERE fname = ? collate nocase AND lname = ? collate nocase;', (m_fname, m_lname))
    mother = variables.cursor.fetchone()
    if mother:
        m_fname = mother[0]
        m_lname = mother[1]
        variables.parents['m_fname'] = m_fname
        variables.parents['m_lname'] = m_lname
        variables.cursor.execute('SELECT address, phone FROM persons WHERE fname = ? collate nocase AND lname = ? collate nocase;', (m_fname, m_lname))
        infor = variables.cursor.fetchone()
        if infor:
            if not infor[0]:
                newborn_address = ''
            else:
                newborn_address = infor[0]
            if not infor[1]:
                newborn_phone = ''
            else:
                newborn_phone = infor[1]
        else:
            newborn_address = ''
            newborn_phone = ''
        variables.newborn_user_input = {'address': newborn_address, 'phone': newborn_phone}
    else:
        variables.parents['m_fname'] = m_fname
        variables.parents['m_lname'] = m_lname
        variables.mother = {'fname':w.entry_m_fname.get().strip(), 'lname':w.entry_m_lname.get().strip()}
        import form_register_a_birth_mother
        form_register_a_birth_mother.vp_start_gui()

def button_father_click():
    f_fname = w.entry_f_fname.get().strip()
    f_lname = w.entry_f_lname.get().strip()
    w.button_father.configure(state='disabled')
    w.button_register.configure(state='normal')

    variables.cursor.execute('SELECT fname, lname FROM persons WHERE fname = ? collate nocase AND lname = ? collate nocase;', (f_fname, f_lname))
    father = variables.cursor.fetchone()
    if father:
        f_fname = father[0]
        f_lname = father[1]
        variables.parents['f_fname'] = f_fname
        variables.parents['f_lname'] = f_lname
    else:
        variables.parents['f_fname'] = f_fname
        variables.parents['f_lname'] = f_lname
        variables.father = {'fname':w.entry_f_fname.get().strip(), 'lname':w.entry_f_lname.get().strip()}
        import form_register_a_birth_father
        form_register_a_birth_father.vp_start_gui()

def button_register_click():
    fname = w.entry_fname.get().strip()
    lname = w.entry_lname.get().strip()
    bdate = w.entry_bdate.get().strip()
    bplace = w.entry_bplace.get().strip()
    gender = w.entry_gender.get().strip()
    f_fname = w.entry_f_fname.get().strip()
    f_lname = w.entry_f_lname.get().strip()
    m_fname = w.entry_m_fname.get().strip()
    m_lname = w.entry_m_lname.get().strip()

    variables.cursor.execute('INSERT INTO persons VALUES (?, ?, ?, ?, ?, ?);', (fname, lname, bdate, bplace, variables.newborn_user_input['address'], variables.newborn_user_input['phone']))
    variables.cursor.execute('INSERT INTO births VALUES (?, ?, ?, DATE(\'now\'), ?, ?, ?, ?, ?, ?);', (create_regno(variables.connection, variables.cursor), fname, lname, variables.user_city, gender.upper(), variables.parents['f_fname'], variables.parents['f_lname'], variables.parents['m_fname'], variables.parents['m_lname']))

    try:
        variables.connection.commit()
        msgBox.showinfo('Success', 'Successfully registered!')
        print('LOG:', 'inserted:', 'birth record for', fname, lname)
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
    import form_register_a_birth
    form_register_a_birth.vp_start_gui()