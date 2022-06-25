import sys
import tkinter as tk
import time
import variables
import tkinter.messagebox as msgBox

# def button_check_click():
#     w.entry_vdate.configure(state='normal')
#     w.entry_violation.configure(state='normal')
#     w.entry_fine.configure(state='normal')
#     w.button_issue.configure(state='normal')
#     w.button_check.configure(state='disabled')
#     w.entry_vdate.insert(0,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

def button_check_click():
    regno = w.entry_regno.get().strip()
    if not regno:
        msgBox.showerror("Error", "Please input regno!")
    elif not regno.isnumeric():
        msgBox.showerror("Error", "Please input numeric regno!")
    else:
        variables.cursor.execute('SELECT p.fname, p.lname, v.make, v.model, v.year, v.color FROM registrations r, persons p, vehicles v WHERE r.regno = ? AND r.fname = p.fname AND r.lname = p.lname AND r.vin = v.vin;', (regno,))
        result = variables.cursor.fetchall()
        if result:
            result = result[0]
            w.entry_fname.configure(state='normal')
            w.entry_lname.configure(state='normal')
            w.entry_make.configure(state='normal')
            w.entry_model.configure(state='normal')
            w.entry_year.configure(state='normal')
            w.entry_color.configure(state='normal')
            w.entry_fname.insert(0,result[0])
            w.entry_lname.insert(0,result[1])
            w.entry_make.insert(0, result[2])
            w.entry_model.insert(0, result[3])
            w.entry_year.insert(0, result[4])
            w.entry_color.insert(0, result[5])
            w.entry_regno.configure(state='readonly')
            w.entry_fname.configure(state='readonly')
            w.entry_lname.configure(state='readonly')
            w.entry_make.configure(state='readonly')
            w.entry_model.configure(state='readonly')
            w.entry_year.configure(state='readonly')
            w.entry_color.configure(state='readonly')
            w.entry_vdate.configure(state='normal')
            w.entry_violation.configure(state='normal')
            w.entry_fine.configure(state='normal')
            w.button_issue.configure(state='normal')
            w.button_check.configure(state='disabled')
            # more detailed date and time
            # w.entry_vdate.insert(0,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            w.entry_vdate.insert(0,time.strftime("%Y-%m-%d", time.localtime()))
        else:
            msgBox.showerror("Error", "No matching record!")


def button_issue_click():
    regno = w.entry_regno.get().strip()
    tno = variables.cursor.execute('SELECT MAX(tno) FROM tickets').fetchall()
    if tno:
        tno = tno[0][0] + 1
    else:
        regno = 1
    vdate = w.entry_vdate.get().strip()
    violation = w.entry_violation.get().strip()
    fine = w.entry_fine.get().strip()
    if vdate and violation and fine:
        if not fine.isnumeric():
            msgBox.showerror("Error", "Please input numeric fine!")
            return
        variables.cursor.execute('INSERT INTO tickets values (?, ?, ?, ?, ?)', (tno, regno, fine, violation, vdate))
        variables.connection.commit()
        print('LOG:', 'Ticket inserted:', (tno, regno, fine, violation, vdate))
        destroy_window()
        msgBox.showinfo("Success", "Ticket successfully issued!")
    else:
        msgBox.showerror("Error", "Vdate/violation/fine cannot be empty!")

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
    import form_issue
    form_issue.vp_start_gui()