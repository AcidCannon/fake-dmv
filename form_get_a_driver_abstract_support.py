import sys
import sqlite3
import variables
from datetime import datetime
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

def tickets_num(conn, c, fname, lname):
    ticket =  '''
                SELECT IFNULL(count(*),0)
                FROM (tickets t LEFT OUTER JOIN registrations r ON t.regno = r.regno) T
                WHERE T.fname = ? collate nocase AND T.lname = ? collate nocase;
            '''
    c.execute(ticket, (fname, lname))
    num = c.fetchone()[0]
    return num

def ticket_num_twoyear(conn, c, fname, lname):
    ticket =  '''
                SELECT IFNULL(count(*),0)
                FROM (tickets t LEFT OUTER JOIN registrations r ON t.regno = r.regno) T
                WHERE T.fname = ? collate nocase AND T.lname = ? collate nocase
                AND T.vdate >= DATE('now', '-2 years');
            '''
    c.execute(ticket, (fname, lname))
    num = c.fetchone()[0]
    return num

def demerit_notices_num(conn, c, fname, lname):
    notice = '''
                SELECT IFNULL(count(*), 0)
                FROM demeritNotices
                WHERE fname = ? collate nocase AND lname = ? collate nocase;
            '''
    c.execute(notice, (fname, lname))
    num = c.fetchone()[0]
    return num

def demerit_notices_num_twoyear(conn, c, fname, lname):
    notice = '''
                SELECT IFNULL(count(*), 0)
                FROM demeritNotices
                WHERE fname = ? collate nocase AND lname = ? collate nocase
                AND ddate >= DATE('now', '-2 years');
            '''
    c.execute(notice, (fname, lname))
    num = c.fetchone()[0]
    return num


def demerit_points_twoyear(conn, c, fname, lname):
    past_two_year = '''
                        SELECT IFNULL(sum(points), 0)
                        FROM demeritNotices
                        WHERE fname = ? collate nocase AND lname = ? collate nocase
                        AND ddate >= DATE('now', '-2 years');
                    '''

    c.execute(past_two_year, (fname, lname))
    num = c.fetchone()[0]
    return num

def demerit_points_total(conn, c, fname, lname):
    lifetime_point = '''
                        SELECT IFNULL(sum(points), 0)
                        FROM demeritNotices
                        WHERE fname = ? collate nocase AND lname = ? collate nocase;
                    '''
    c.execute(lifetime_point, (fname, lname))
    num = c.fetchone()[0]
    return num

def button_check_click():
    fname = w.entry_fname.get().strip()
    lname = w.entry_lname.get().strip()
    variables.cursor.execute('SELECT fname, lname FROM persons WHERE fname = ? collate nocase AND lname = ? collate nocase;', (fname, lname))
    result = variables.cursor.fetchone()
    if fname and lname:
        if result:
            w.entry_fname.configure(state='readonly')
            w.entry_lname.configure(state='readonly')
            w.button_check.configure(state='disabled')
            tickets_2year = ticket_num_twoyear(variables.connection, variables.cursor, fname, lname)
            tickets_lifetime = tickets_num(variables.connection, variables.cursor, fname, lname)
            notices_2year = demerit_notices_num_twoyear(variables.connection, variables.cursor, fname, lname)
            notices_lifetime = demerit_notices_num(variables.connection, variables.cursor, fname, lname)
            points_2year = demerit_points_twoyear(variables.connection, variables.cursor, fname, lname)
            points_lifetime = demerit_points_total(variables.connection, variables.cursor, fname, lname)
            w.entry_tickets_2year.configure(state='normal')
            w.entry_tickets_lifetime.configure(state='normal')
            w.entry_demerit_notices_2year.configure(state='normal')
            w.entry_demerit_notices_lifetime.configure(state='normal')
            w.entry_demerit_points_2_year.configure(state='normal')
            w.entry_demerit_points_lifetime.configure(state='normal')
            w.entry_tickets_2year.insert(0, tickets_2year)
            w.entry_tickets_lifetime.insert(0, tickets_lifetime)
            w.entry_demerit_notices_2year.insert(0, notices_2year)
            w.entry_demerit_notices_lifetime.insert(0, notices_lifetime)
            w.entry_demerit_points_2_year.insert(0, points_2year)
            w.entry_demerit_points_lifetime.insert(0, points_lifetime)
            w.entry_tickets_2year.configure(state='readonly')
            w.entry_tickets_lifetime.configure(state='readonly')
            w.entry_demerit_notices_2year.configure(state='readonly')
            w.entry_demerit_notices_lifetime.configure(state='readonly')
            w.entry_demerit_points_2_year.configure(state='readonly')
            w.entry_demerit_points_lifetime.configure(state='readonly')
            print('LOG:', "fetched", (tickets_2year, tickets_lifetime, notices_2year, notices_lifetime, points_2year, points_lifetime))
            if tickets_lifetime != 0:
                w.button_show.configure(state='normal')
                msgBox.showinfo("Info", "You have tickets, click button \'show\' to see details!")
        else:
            msgBox.showerror("Error", "No matching record!")
    else:
        msgBox.showerror("Error", "Fname/lname cannot be empty!")

def button_more_click():
    for row in w.scrolledtreeview_tickets.get_children():
        w.scrolledtreeview_tickets.delete(row)
    if len(variables.tickets) > 5:
        for i, record in enumerate(variables.tickets[:5]):
            print('LOG:', 'fetched', record)
            w.scrolledtreeview_tickets.insert('', i, values=record[0:])
        variables.tickets = variables.tickets[5:]
    else:
        for i, record in enumerate(variables.tickets):
            print('LOG:', 'fetched', record)
            w.scrolledtreeview_tickets.insert('', i, values=record[0:])
        w.button_more.configure(state='disabled')
        msgBox.showinfo("Info", "No more tickets to show, you can close the window now!")

def button_show_click():
    w.button_show.configure(state='disabled')
    w.button_more.configure(state='normal')
    fname = w.entry_fname.get().strip()
    lname = w.entry_lname.get().strip()
    select_ticket = ''' 
                        SELECT T.tno, T.vdate, T.violation, T.fine, T.regno, T.make, T.model
                        FROM (tickets t LEFT OUTER JOIN registrations r ON t.regno = r.regno LEFT OUTER JOIN vehicles v ON r.vin = v.vin) T
                        WHERE T.fname = ? collate nocase AND T.lname = ? collate nocase
                        ORDER BY T.vdate DESC;
                    '''
    variables.cursor.execute(select_ticket, (fname, lname))
    variables.tickets = variables.cursor.fetchall()
    for row in w.scrolledtreeview_tickets.get_children():
        w.scrolledtreeview_tickets.delete(row)
    if len(variables.tickets) > 5:
        for i, record in enumerate(variables.tickets[:5]):
            print('LOG:', 'fetched', record)
            w.scrolledtreeview_tickets.insert('', i, values=record[0:])
        variables.tickets = variables.tickets[5:]
    else:
        for i, record in enumerate(variables.tickets):
            print('LOG:', 'fetched', record)
            w.scrolledtreeview_tickets.insert('', i, values=record[0:])
        w.button_more.configure(state='disabled')
        msgBox.showinfo("Info", "No more tickets to show, you can close the window now!")

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
    import form_get_a_driver_abstract
    form_get_a_driver_abstract.vp_start_gui()