import sys

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

import form_process_a_bill_of_sale_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = form_process_a_bill_of_sale (root)
    form_process_a_bill_of_sale_support.init(root, top)
    root.mainloop()

w = None
def create_form_process_a_bill_of_sale(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = form_process_a_bill_of_sale (w)
    form_process_a_bill_of_sale_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_form_process_a_bill_of_sale():
    global w
    w.destroy()
    w = None

class form_process_a_bill_of_sale:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("754x256+500+500")
        top.title("Agent - Process a bill of sale")
        top.configure(background="#d9d9d9")

        self.labelframe_current_owner = tk.LabelFrame(top)
        self.labelframe_current_owner.place(relx=0.027, rely=0.039
                , relheight=0.879, relwidth=0.411)
        self.labelframe_current_owner.configure(relief='groove')
        self.labelframe_current_owner.configure(foreground="black")
        self.labelframe_current_owner.configure(text='''Current owner''')
        self.labelframe_current_owner.configure(background="#d9d9d9")

        self.label_cur_fname = tk.Label(self.labelframe_current_owner)
        self.label_cur_fname.place(relx=0.097, rely=0.222, height=23, width=45
                , bordermode='ignore')
        self.label_cur_fname.configure(background="#d9d9d9")
        self.label_cur_fname.configure(disabledforeground="#a3a3a3")
        self.label_cur_fname.configure(foreground="#000000")
        self.label_cur_fname.configure(text='''fname:''')

        self.label_cur_lname = tk.Label(self.labelframe_current_owner)
        self.label_cur_lname.place(relx=0.097, rely=0.489, height=23, width=44
                , bordermode='ignore')
        self.label_cur_lname.configure(background="#d9d9d9")
        self.label_cur_lname.configure(disabledforeground="#a3a3a3")
        self.label_cur_lname.configure(foreground="#000000")
        self.label_cur_lname.configure(text='''lname:''')

        self.label_vin = tk.Label(self.labelframe_current_owner)
        self.label_vin.place(relx=0.161, rely=0.756, height=23, width=25
                , bordermode='ignore')
        self.label_vin.configure(background="#d9d9d9")
        self.label_vin.configure(disabledforeground="#a3a3a3")
        self.label_vin.configure(foreground="#000000")
        self.label_vin.configure(text='''vin:''')

        self.entry_cur_fname = tk.Entry(self.labelframe_current_owner)
        self.entry_cur_fname.place(relx=0.242, rely=0.222, height=17
                , relwidth=0.69, bordermode='ignore')
        self.entry_cur_fname.configure(background="white")
        self.entry_cur_fname.configure(disabledforeground="#a3a3a3")
        self.entry_cur_fname.configure(font="TkFixedFont")
        self.entry_cur_fname.configure(foreground="#000000")
        self.entry_cur_fname.configure(insertbackground="black")

        self.entry_cur_lname = tk.Entry(self.labelframe_current_owner)
        self.entry_cur_lname.place(relx=0.242, rely=0.489, height=17
                , relwidth=0.69, bordermode='ignore')
        self.entry_cur_lname.configure(background="white")
        self.entry_cur_lname.configure(disabledforeground="#a3a3a3")
        self.entry_cur_lname.configure(font="TkFixedFont")
        self.entry_cur_lname.configure(foreground="#000000")
        self.entry_cur_lname.configure(highlightbackground="#d9d9d9")
        self.entry_cur_lname.configure(highlightcolor="black")
        self.entry_cur_lname.configure(insertbackground="black")
        self.entry_cur_lname.configure(selectbackground="#c4c4c4")
        self.entry_cur_lname.configure(selectforeground="black")

        self.entry_vin = tk.Entry(self.labelframe_current_owner)
        self.entry_vin.place(relx=0.242, rely=0.756, height=17, relwidth=0.69
                , bordermode='ignore')
        self.entry_vin.configure(background="white")
        self.entry_vin.configure(disabledforeground="#a3a3a3")
        self.entry_vin.configure(font="TkFixedFont")
        self.entry_vin.configure(foreground="#000000")
        self.entry_vin.configure(highlightbackground="#d9d9d9")
        self.entry_vin.configure(highlightcolor="black")
        self.entry_vin.configure(insertbackground="black")
        self.entry_vin.configure(selectbackground="#c4c4c4")
        self.entry_vin.configure(selectforeground="black")

        self.labelframe_new_owner = tk.LabelFrame(top)
        self.labelframe_new_owner.place(relx=0.557, rely=0.039, relheight=0.879
                , relwidth=0.411)
        self.labelframe_new_owner.configure(relief='groove')
        self.labelframe_new_owner.configure(foreground="black")
        self.labelframe_new_owner.configure(text='''New owner''')
        self.labelframe_new_owner.configure(background="#d9d9d9")

        self.label_new_fname = tk.Label(self.labelframe_new_owner)
        self.label_new_fname.place(relx=0.097, rely=0.222, height=23, width=37
                , bordermode='ignore')
        self.label_new_fname.configure(activebackground="#f9f9f9")
        self.label_new_fname.configure(activeforeground="black")
        self.label_new_fname.configure(background="#d9d9d9")
        self.label_new_fname.configure(disabledforeground="#a3a3a3")
        self.label_new_fname.configure(foreground="#000000")
        self.label_new_fname.configure(highlightbackground="#d9d9d9")
        self.label_new_fname.configure(highlightcolor="black")
        self.label_new_fname.configure(text='''fname:''')

        self.label_new_lname = tk.Label(self.labelframe_new_owner)
        self.label_new_lname.place(relx=0.097, rely=0.489, height=23, width=37
                , bordermode='ignore')
        self.label_new_lname.configure(activebackground="#f9f9f9")
        self.label_new_lname.configure(activeforeground="black")
        self.label_new_lname.configure(background="#d9d9d9")
        self.label_new_lname.configure(disabledforeground="#a3a3a3")
        self.label_new_lname.configure(foreground="#000000")
        self.label_new_lname.configure(highlightbackground="#d9d9d9")
        self.label_new_lname.configure(highlightcolor="black")
        self.label_new_lname.configure(text='''lname:''')

        self.label_plate = tk.Label(self.labelframe_new_owner)
        self.label_plate.place(relx=0.097, rely=0.756, height=23, width=37
                , bordermode='ignore')
        self.label_plate.configure(activebackground="#f9f9f9")
        self.label_plate.configure(activeforeground="black")
        self.label_plate.configure(background="#d9d9d9")
        self.label_plate.configure(disabledforeground="#a3a3a3")
        self.label_plate.configure(foreground="#000000")
        self.label_plate.configure(highlightbackground="#d9d9d9")
        self.label_plate.configure(highlightcolor="black")
        self.label_plate.configure(text='''plate:''')

        self.entry_new_fname = tk.Entry(self.labelframe_new_owner)
        self.entry_new_fname.place(relx=0.242, rely=0.222, height=17
                , relwidth=0.69, bordermode='ignore')
        self.entry_new_fname.configure(background="white")
        self.entry_new_fname.configure(disabledforeground="#a3a3a3")
        self.entry_new_fname.configure(font="TkFixedFont")
        self.entry_new_fname.configure(foreground="#000000")
        self.entry_new_fname.configure(highlightbackground="#d9d9d9")
        self.entry_new_fname.configure(highlightcolor="black")
        self.entry_new_fname.configure(insertbackground="black")
        self.entry_new_fname.configure(selectbackground="#c4c4c4")
        self.entry_new_fname.configure(selectforeground="black")
        self.entry_new_fname.configure(state='disabled')

        self.entry_new_lname = tk.Entry(self.labelframe_new_owner)
        self.entry_new_lname.place(relx=0.242, rely=0.489, height=17
                , relwidth=0.69, bordermode='ignore')
        self.entry_new_lname.configure(background="white")
        self.entry_new_lname.configure(disabledforeground="#a3a3a3")
        self.entry_new_lname.configure(font="TkFixedFont")
        self.entry_new_lname.configure(foreground="#000000")
        self.entry_new_lname.configure(highlightbackground="#d9d9d9")
        self.entry_new_lname.configure(highlightcolor="black")
        self.entry_new_lname.configure(insertbackground="black")
        self.entry_new_lname.configure(selectbackground="#c4c4c4")
        self.entry_new_lname.configure(selectforeground="black")
        self.entry_new_lname.configure(state='disabled')

        self.entry_plate = tk.Entry(self.labelframe_new_owner)
        self.entry_plate.place(relx=0.242, rely=0.756, height=17, relwidth=0.69
                , bordermode='ignore')
        self.entry_plate.configure(background="white")
        self.entry_plate.configure(disabledforeground="#a3a3a3")
        self.entry_plate.configure(font="TkFixedFont")
        self.entry_plate.configure(foreground="#000000")
        self.entry_plate.configure(highlightbackground="#d9d9d9")
        self.entry_plate.configure(highlightcolor="black")
        self.entry_plate.configure(insertbackground="black")
        self.entry_plate.configure(selectbackground="#c4c4c4")
        self.entry_plate.configure(selectforeground="black")
        self.entry_plate.configure(state='disabled')

        self.button_current_owner = tk.Button(top)
        self.button_current_owner.place(relx=0.464, rely=0.156, height=28
                , width=56)
        self.button_current_owner.configure(activebackground="#ececec")
        self.button_current_owner.configure(activeforeground="#000000")
        self.button_current_owner.configure(background="#d9d9d9")
        self.button_current_owner.configure(command=form_process_a_bill_of_sale_support.button_current_owner_click)
        self.button_current_owner.configure(disabledforeground="#a3a3a3")
        self.button_current_owner.configure(foreground="#000000")
        self.button_current_owner.configure(highlightbackground="#d9d9d9")
        self.button_current_owner.configure(highlightcolor="black")
        self.button_current_owner.configure(pady="0")
        self.button_current_owner.configure(text='''Check''')

        self.button_new_owner = tk.Button(top)
        self.button_new_owner.place(relx=0.464, rely=0.43, height=28, width=56)
        self.button_new_owner.configure(activebackground="#ececec")
        self.button_new_owner.configure(activeforeground="#000000")
        self.button_new_owner.configure(background="#d9d9d9")
        self.button_new_owner.configure(command=form_process_a_bill_of_sale_support.button_new_owner_click)
        self.button_new_owner.configure(disabledforeground="#a3a3a3")
        self.button_new_owner.configure(foreground="#000000")
        self.button_new_owner.configure(highlightbackground="#d9d9d9")
        self.button_new_owner.configure(highlightcolor="black")
        self.button_new_owner.configure(pady="0")
        self.button_new_owner.configure(state='disabled')
        self.button_new_owner.configure(text='''Check''')

        self.button_process = tk.Button(top)
        self.button_process.place(relx=0.464, rely=0.703, height=28, width=56)
        self.button_process.configure(activebackground="#ececec")
        self.button_process.configure(activeforeground="#000000")
        self.button_process.configure(background="#d9d9d9")
        self.button_process.configure(command=form_process_a_bill_of_sale_support.button_process_click)
        self.button_process.configure(disabledforeground="#a3a3a3")
        self.button_process.configure(foreground="#000000")
        self.button_process.configure(highlightbackground="#d9d9d9")
        self.button_process.configure(highlightcolor="black")
        self.button_process.configure(pady="0")
        self.button_process.configure(state='disabled')
        self.button_process.configure(text='''Process''')

if __name__ == '__main__':
    vp_start_gui()





