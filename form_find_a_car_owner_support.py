import sys
import variables
import sqlite3
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
    make = w.entry_make.get().strip()
    model = w.entry_model.get().strip()
    year = w.entry_year.get().strip()
    color = w.entry_color.get().strip()
    plate = w.entry_plate.get().strip()
    for row in w.scrolledtreeview_result.get_children():
        w.scrolledtreeview_result.delete(row)
    w.entry_fname.configure(state='normal')
    w.entry_lname.configure(state='normal')
    w.entry_regdate.configure(state='normal')
    w.entry_expiry.configure(state='normal')
    w.entry_details_make.configure(state='normal')
    w.entry_details_model.configure(state='normal')
    w.entry_details_year.configure(state='normal')
    w.entry_details_color.configure(state='normal')
    w.entry_details_plate.configure(state='normal')
    w.entry_fname.delete(0, 'end')
    w.entry_lname.delete(0, 'end')
    w.entry_regdate.delete(0, 'end')
    w.entry_expiry.delete(0, 'end')
    w.entry_details_make.delete(0, 'end')
    w.entry_details_model.delete(0, 'end')
    w.entry_details_year.delete(0, 'end')
    w.entry_details_color.delete(0, 'end')
    w.entry_details_plate.delete(0, 'end')
    w.entry_fname.configure(state='readonly')
    w.entry_lname.configure(state='readonly')
    w.entry_regdate.configure(state='readonly')
    w.entry_expiry.configure(state='readonly')
    w.entry_details_make.configure(state='readonly')
    w.entry_details_model.configure(state='readonly')
    w.entry_details_year.configure(state='readonly')
    w.entry_details_color.configure(state='readonly')
    w.entry_details_plate.configure(state='readonly')

    if not (make or model or year or color or plate):
        msgBox.showerror('Error', 'At least one of make/model/year/plate/color is not empty!')
        return

    if year:
        if not year.isnumeric():
            msgBox.showerror('Error', 'Please input numeric year!')
            return

    input_args = [make, model, year, plate, color]
    input_text = ['make = ? collate nocase', 'model = ? collate nocase', 'year = ? collate nocase', 'plate = ? collate nocase', 'color = ? collate nocase']
    first_arg_flag = True
    pass_in = []

    for i in range(5):
        if not input_args[i]:
            input_text[i] = ''
        else:
            pass_in.append(input_args[i])
            if first_arg_flag:
                first_arg_flag = False
            else:
                input_text[i] = ' AND ' + input_text[i]

    print('LOG:', 'passed in:', pass_in)
    cat_args = ''.join(input_text)
    print('LOG:', 'concatenated:', cat_args)

    query = 'SELECT v.make, v.model, v.year, v.color, r.plate FROM vehicles v, registrations r WHERE '
    query = query + cat_args
    query = query + ' AND r.vin = v.vin;'

    print('LOG:', 'executed:', query)

    variables.cursor.execute(query, tuple(pass_in))
    result = variables.cursor.fetchall()

    query_set = []

    if not result:
        msgBox.showerror('Error', 'No matching record:\nNo satisfied vehicles, thus no owner can be found!')
        return
    else:
        if(len(result) > 4):
            for row in w.scrolledtreeview_result.get_children():
                w.scrolledtreeview_result.delete(row)
            for index, record in enumerate(result):
                print('LOG:', 'fetched:', index, record)
                w.scrolledtreeview_result.insert('', index, text=index, values=record[0:])
            msgBox.showinfo("Info", "Number of records >= 4\nBy double-click specific record below to see details!")
        else:
            for row in w.scrolledtreeview_result.get_children():
                w.scrolledtreeview_result.delete(row)
            for index, record in enumerate(result):
                print('LOG:', 'fetched:', index, record)
                w.scrolledtreeview_result.insert('', index, text=index, values=record[0:])
                for each in result:
                    query_set.append(each)
            query = '''
                      SELECT v.make, v.model, v.year, v.color, r.plate, r.regdate, r.expiry, r.fname, r.lname FROM vehicles v, registrations r
                      WHERE v.make = ? collate nocase AND v.model = ? collate nocase AND v.year = ? collate nocase AND v.color = ? collate nocase AND r.plate = ? collate nocase AND r.vin = v.vin collate nocase
                      ORDER BY r.regdate DESC
                      LIMIT 1;
                    '''
            result = []
            for each in query_set:
                variables.cursor.execute(query, (each[0], each[1], each[2], each[3], each[4]))
                temp = variables.cursor.fetchall()
                result.append(temp)

            if not result:
                msgBox.showerror('Error', 'No matching record:\nCannot found any owner of the vehicles shown below, because they are not registered!\nThus details cannot be shown!')
                return

            result_dic = {}

            for index, fetched in enumerate(result):
                result_dic[fetched[0][5]] = fetched[0]
            print('LOG', 'processed:', result_dic)
            details = result_dic[sorted(result_dic)[-1]]
            print('LOG:', 'details:', details)
            # (make, model, year, color, plate, regdate, expiry, fname, lname)
            w.entry_fname.configure(state='normal')
            w.entry_lname.configure(state='normal')
            w.entry_regdate.configure(state='normal')
            w.entry_expiry.configure(state='normal')
            w.entry_details_make.configure(state='normal')
            w.entry_details_model.configure(state='normal')
            w.entry_details_year.configure(state='normal')
            w.entry_details_color.configure(state='normal')
            w.entry_details_plate.configure(state='normal')
            w.entry_fname.insert(0, details[7])
            w.entry_lname.insert(0, details[8])
            w.entry_regdate.insert(0, details[5])
            w.entry_expiry.insert(0, details[6])
            w.entry_details_make.insert(0, details[0])
            w.entry_details_model.insert(0, details[1])
            w.entry_details_year.insert(0, details[2])
            w.entry_details_color.insert(0, details[3])
            w.entry_details_plate.insert(0, details[4])
            w.entry_fname.configure(state='readonly')
            w.entry_lname.configure(state='readonly')
            w.entry_regdate.configure(state='readonly')
            w.entry_expiry.configure(state='readonly')
            w.entry_details_make.configure(state='readonly')
            w.entry_details_model.configure(state='readonly')
            w.entry_details_year.configure(state='readonly')
            w.entry_details_color.configure(state='readonly')
            w.entry_details_plate.configure(state='readonly')
            msgBox.showinfo("Info", "Number of records < 4\nDetails already shown!")

def scrolledtreeview_result_double_click(*args):
    item = w.scrolledtreeview_result.selection()
    if item:
        item = item[0]
    else:
        return
    w.entry_fname.configure(state='normal')
    w.entry_lname.configure(state='normal')
    w.entry_regdate.configure(state='normal')
    w.entry_expiry.configure(state='normal')
    w.entry_details_make.configure(state='normal')
    w.entry_details_model.configure(state='normal')
    w.entry_details_year.configure(state='normal')
    w.entry_details_color.configure(state='normal')
    w.entry_details_plate.configure(state='normal')
    w.entry_fname.delete(0, 'end')
    w.entry_lname.delete(0, 'end')
    w.entry_regdate.delete(0, 'end')
    w.entry_expiry.delete(0, 'end')
    w.entry_details_make.delete(0, 'end')
    w.entry_details_model.delete(0, 'end')
    w.entry_details_year.delete(0, 'end')
    w.entry_details_color.delete(0, 'end')
    w.entry_details_plate.delete(0, 'end')
    w.entry_fname.configure(state='readonly')
    w.entry_lname.configure(state='readonly')
    w.entry_regdate.configure(state='readonly')
    w.entry_expiry.configure(state='readonly')
    w.entry_details_make.configure(state='readonly')
    w.entry_details_model.configure(state='readonly')
    w.entry_details_year.configure(state='readonly')
    w.entry_details_color.configure(state='readonly')
    w.entry_details_plate.configure(state='readonly')
    selected = w.scrolledtreeview_result.item(item, "values")
    print('LOG:', 'selected:', selected)
    query = '''
          SELECT v.make, v.model, v.year, v.color, r.plate, r.regdate, r.expiry, r.fname, r.lname FROM vehicles v, registrations r
          WHERE v.make = ? collate nocase AND v.model = ? collate nocase AND v.year = ? collate nocase AND v.color = ? collate nocase AND r.plate = ? collate nocase AND r.vin = v.vin collate nocase
          ORDER BY r.regdate DESC
          LIMIT 1;
        '''
    result = variables.cursor.execute(query, selected)
    if result:
        result = variables.cursor.fetchall()[0]
    else:
        msgBox.showerror('Error', 'No matching record:\nCannot found owner for this vehicle, because it is not registered!\nThus details cannot be shown!')
        return
    print('LOG:', 'fetched:', result)
    w.entry_fname.configure(state='normal')
    w.entry_lname.configure(state='normal')
    w.entry_regdate.configure(state='normal')
    w.entry_expiry.configure(state='normal')
    w.entry_details_make.configure(state='normal')
    w.entry_details_model.configure(state='normal')
    w.entry_details_year.configure(state='normal')
    w.entry_details_color.configure(state='normal')
    w.entry_details_plate.configure(state='normal')
    w.entry_fname.insert(0, result[7])
    w.entry_lname.insert(0, result[8])
    w.entry_regdate.insert(0, result[5])
    w.entry_expiry.insert(0, result[6])
    w.entry_details_make.insert(0, result[0])
    w.entry_details_model.insert(0, result[1])
    w.entry_details_year.insert(0, result[2])
    w.entry_details_color.insert(0, result[3])
    w.entry_details_plate.insert(0, result[4])
    w.entry_fname.configure(state='readonly')
    w.entry_lname.configure(state='readonly')
    w.entry_regdate.configure(state='readonly')
    w.entry_expiry.configure(state='readonly')
    w.entry_details_make.configure(state='readonly')
    w.entry_details_model.configure(state='readonly')
    w.entry_details_year.configure(state='readonly')
    w.entry_details_color.configure(state='readonly')
    w.entry_details_plate.configure(state='readonly')

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
    import form_find_a_car_owner
    form_find_a_car_owner.vp_start_gui()