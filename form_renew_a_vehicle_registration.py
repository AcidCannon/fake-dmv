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

import form_renew_a_vehicle_registration_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = form_renew_a_vehicle_registration (root)
    form_renew_a_vehicle_registration_support.init(root, top)
    root.mainloop()

w = None
def create_form_renew_a_vehicle_registration(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = form_renew_a_vehicle_registration (w)
    form_renew_a_vehicle_registration_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_form_renew_a_vehicle_registration():
    global w
    w.destroy()
    w = None

class form_renew_a_vehicle_registration:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("470x120+500+500")
        top.title("Agent - Renew a vehicle registration")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.label_regno = tk.Label(top)
        self.label_regno.place(relx=0.043, rely=0.083, height=23, width=44)
        self.label_regno.configure(activebackground="#f9f9f9")
        self.label_regno.configure(activeforeground="black")
        self.label_regno.configure(background="#d9d9d9")
        self.label_regno.configure(disabledforeground="#a3a3a3")
        self.label_regno.configure(foreground="#000000")
        self.label_regno.configure(highlightbackground="#d9d9d9")
        self.label_regno.configure(highlightcolor="black")
        self.label_regno.configure(text='''regno:''')

        self.label_expiry = tk.Label(top)
        self.label_expiry.place(relx=0.043, rely=0.333, height=23, width=44)
        self.label_expiry.configure(activebackground="#f9f9f9")
        self.label_expiry.configure(activeforeground="black")
        self.label_expiry.configure(background="#d9d9d9")
        self.label_expiry.configure(disabledforeground="#a3a3a3")
        self.label_expiry.configure(foreground="#000000")
        self.label_expiry.configure(highlightbackground="#d9d9d9")
        self.label_expiry.configure(highlightcolor="black")
        self.label_expiry.configure(text='''expiry:''')

        self.entry_expiry = tk.Entry(top)
        self.entry_expiry.place(relx=0.138, rely=0.357, height=17
                , relwidth=0.796)
        self.entry_expiry.configure(background="white")
        self.entry_expiry.configure(disabledforeground="#a3a3a3")
        self.entry_expiry.configure(font="TkFixedFont")
        self.entry_expiry.configure(foreground="#000000")
        self.entry_expiry.configure(highlightbackground="#d9d9d9")
        self.entry_expiry.configure(highlightcolor="black")
        self.entry_expiry.configure(insertbackground="black")
        self.entry_expiry.configure(selectbackground="#c4c4c4")
        self.entry_expiry.configure(selectforeground="black")
        self.entry_expiry.configure(state='readonly')

        self.entry_regno = tk.Entry(top)
        self.entry_regno.place(relx=0.138, rely=0.108, height=17, relwidth=0.796)

        self.entry_regno.configure(background="white")
        self.entry_regno.configure(disabledforeground="#a3a3a3")
        self.entry_regno.configure(font="TkFixedFont")
        self.entry_regno.configure(foreground="#000000")
        self.entry_regno.configure(highlightbackground="#d9d9d9")
        self.entry_regno.configure(highlightcolor="black")
        self.entry_regno.configure(insertbackground="black")
        self.entry_regno.configure(selectbackground="#c4c4c4")
        self.entry_regno.configure(selectforeground="black")

        self.button_check = tk.Button(top)
        self.button_check.place(relx=0.702, rely=0.667, height=28, width=46)
        self.button_check.configure(activebackground="#ececec")
        self.button_check.configure(activeforeground="#000000")
        self.button_check.configure(background="#d9d9d9")
        self.button_check.configure(command=form_renew_a_vehicle_registration_support.button_check_click)
        self.button_check.configure(disabledforeground="#a3a3a3")
        self.button_check.configure(foreground="#000000")
        self.button_check.configure(highlightbackground="#d9d9d9")
        self.button_check.configure(highlightcolor="black")
        self.button_check.configure(pady="0")
        self.button_check.configure(text='''Check''')

        self.button_renew = tk.Button(top)
        self.button_renew.place(relx=0.83, rely=0.667, height=28, width=46)
        self.button_renew.configure(activebackground="#ececec")
        self.button_renew.configure(activeforeground="#000000")
        self.button_renew.configure(background="#d9d9d9")
        self.button_renew.configure(command=form_renew_a_vehicle_registration_support.button_renew_click)
        self.button_renew.configure(disabledforeground="#a3a3a3")
        self.button_renew.configure(foreground="#000000")
        self.button_renew.configure(highlightbackground="#d9d9d9")
        self.button_renew.configure(highlightcolor="black")
        self.button_renew.configure(pady="0")
        self.button_renew.configure(state='disabled')
        self.button_renew.configure(text='''Renew''')

if __name__ == '__main__':
    vp_start_gui()