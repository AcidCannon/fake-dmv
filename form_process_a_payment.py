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

import form_process_a_payment_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = form_process_a_payment (root)
    form_process_a_payment_support.init(root, top)
    root.mainloop()

w = None
def create_form_process_a_payment(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = form_process_a_payment (w)
    form_process_a_payment_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_form_process_a_payment():
    global w
    w.destroy()
    w = None

class form_process_a_payment:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("450x190+500+500")
        top.title("Agent - Process a payment")
        top.configure(background="#d9d9d9")

        self.entry_tno = tk.Entry(top)
        self.entry_tno.place(relx=0.178, rely=0.105,height=17, relwidth=0.787)
        self.entry_tno.configure(background="white")
        self.entry_tno.configure(disabledforeground="#a3a3a3")
        self.entry_tno.configure(font="TkFixedFont")
        self.entry_tno.configure(foreground="#000000")
        self.entry_tno.configure(insertbackground="black")

        self.entry_fine = tk.Entry(top)
        self.entry_fine.place(relx=0.178, rely=0.263,height=17, relwidth=0.787)
        self.entry_fine.configure(background="white")
        self.entry_fine.configure(disabledforeground="#a3a3a3")
        self.entry_fine.configure(font="TkFixedFont")
        self.entry_fine.configure(foreground="#000000")
        self.entry_fine.configure(highlightbackground="#d9d9d9")
        self.entry_fine.configure(highlightcolor="black")
        self.entry_fine.configure(insertbackground="black")
        self.entry_fine.configure(selectbackground="#c4c4c4")
        self.entry_fine.configure(selectforeground="black")
        self.entry_fine.configure(state='disabled')

        self.label_tno = tk.Label(top)
        self.label_tno.place(relx=0.044, rely=0.105, height=23, width=60)
        self.label_tno.configure(background="#d9d9d9")
        self.label_tno.configure(disabledforeground="#a3a3a3")
        self.label_tno.configure(foreground="#000000")
        self.label_tno.configure(text='''tno:''')

        self.label_fine = tk.Label(top)
        self.label_fine.place(relx=0.044, rely=0.263, height=23, width=60)
        self.label_fine.configure(background="#d9d9d9")
        self.label_fine.configure(disabledforeground="#a3a3a3")
        self.label_fine.configure(foreground="#000000")
        self.label_fine.configure(text='''fine:''')

        self.entry_paid = tk.Entry(top)
        self.entry_paid.place(relx=0.178, rely=0.421,height=17, relwidth=0.787)
        self.entry_paid.configure(background="white")
        self.entry_paid.configure(disabledforeground="#a3a3a3")
        self.entry_paid.configure(font="TkFixedFont")
        self.entry_paid.configure(foreground="#000000")
        self.entry_paid.configure(highlightbackground="#d9d9d9")
        self.entry_paid.configure(highlightcolor="black")
        self.entry_paid.configure(insertbackground="black")
        self.entry_paid.configure(selectbackground="#c4c4c4")
        self.entry_paid.configure(selectforeground="black")
        self.entry_paid.configure(state='disabled')

        self.entry_amount = tk.Entry(top)
        self.entry_amount.place(relx=0.178, rely=0.579, height=17
                , relwidth=0.787)
        self.entry_amount.configure(background="white")
        self.entry_amount.configure(disabledforeground="#a3a3a3")
        self.entry_amount.configure(font="TkFixedFont")
        self.entry_amount.configure(foreground="#000000")
        self.entry_amount.configure(highlightbackground="#d9d9d9")
        self.entry_amount.configure(highlightcolor="black")
        self.entry_amount.configure(insertbackground="black")
        self.entry_amount.configure(selectbackground="#c4c4c4")
        self.entry_amount.configure(selectforeground="black")
        self.entry_amount.configure(state='disabled')

        self.label_paid = tk.Label(top)
        self.label_paid.place(relx=0.044, rely=0.421, height=23, width=60)
        self.label_paid.configure(activebackground="#f9f9f9")
        self.label_paid.configure(activeforeground="black")
        self.label_paid.configure(background="#d9d9d9")
        self.label_paid.configure(disabledforeground="#a3a3a3")
        self.label_paid.configure(foreground="#000000")
        self.label_paid.configure(highlightbackground="#d9d9d9")
        self.label_paid.configure(highlightcolor="black")
        self.label_paid.configure(text='''paid:''')

        self.label_amount = tk.Label(top)
        self.label_amount.place(relx=0.022, rely=0.579, height=23, width=60)
        self.label_amount.configure(activebackground="#f9f9f9")
        self.label_amount.configure(activeforeground="black")
        self.label_amount.configure(background="#d9d9d9")
        self.label_amount.configure(disabledforeground="#a3a3a3")
        self.label_amount.configure(foreground="#000000")
        self.label_amount.configure(highlightbackground="#d9d9d9")
        self.label_amount.configure(highlightcolor="black")
        self.label_amount.configure(text='''amount:''')

        self.button_check = tk.Button(top)
        self.button_check.place(relx=0.733, rely=0.737, height=28, width=46)
        self.button_check.configure(activebackground="#ececec")
        self.button_check.configure(activeforeground="#000000")
        self.button_check.configure(background="#d9d9d9")
        self.button_check.configure(command=form_process_a_payment_support.button_check_click)
        self.button_check.configure(disabledforeground="#a3a3a3")
        self.button_check.configure(foreground="#000000")
        self.button_check.configure(highlightbackground="#d9d9d9")
        self.button_check.configure(highlightcolor="black")
        self.button_check.configure(pady="0")
        self.button_check.configure(text='''Check''')

        self.button_pay = tk.Button(top)
        self.button_pay.place(relx=0.856, rely=0.737, height=28, width=49)
        self.button_pay.configure(activebackground="#ececec")
        self.button_pay.configure(activeforeground="#000000")
        self.button_pay.configure(background="#d9d9d9")
        self.button_pay.configure(command=form_process_a_payment_support.button_pay_click)
        self.button_pay.configure(disabledforeground="#a3a3a3")
        self.button_pay.configure(foreground="#000000")
        self.button_pay.configure(highlightbackground="#d9d9d9")
        self.button_pay.configure(highlightcolor="black")
        self.button_pay.configure(pady="0")
        self.button_pay.configure(state='disabled')
        self.button_pay.configure(text='''Pay''')

if __name__ == '__main__':
    vp_start_gui()





