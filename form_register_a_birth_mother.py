import sys
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

import form_register_a_birth_mother_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = form_register_a_birth_mother (root)
    form_register_a_birth_mother_support.init(root, top)
    msgBox.showinfo('Info', 'Please input additional information (not required) about mother, and click \'Apply\'!')
    root.mainloop()

w = None
def create_form_register_a_birth_mother(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = form_register_a_birth_mother (w)
    form_register_a_birth_mother_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_form_register_a_birth_mother():
    global w
    w.destroy()
    w = None

class form_register_a_birth_mother:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("374x305+500+500")
        top.title("Agent - Register a birth - Mother")
        top.configure(background="#d9d9d9")

        self.label_fname = tk.Label(top)
        self.label_fname.place(relx=0.053, rely=0.066, height=23, width=55)
        self.label_fname.configure(background="#d9d9d9")
        self.label_fname.configure(disabledforeground="#a3a3a3")
        self.label_fname.configure(foreground="#000000")
        self.label_fname.configure(text='''Fname:''')

        self.label_lname = tk.Label(top)
        self.label_lname.place(relx=0.053, rely=0.197, height=23, width=55)
        self.label_lname.configure(activebackground="#f9f9f9")
        self.label_lname.configure(activeforeground="black")
        self.label_lname.configure(background="#d9d9d9")
        self.label_lname.configure(disabledforeground="#a3a3a3")
        self.label_lname.configure(foreground="#000000")
        self.label_lname.configure(highlightbackground="#d9d9d9")
        self.label_lname.configure(highlightcolor="black")
        self.label_lname.configure(text='''Lname:''')

        self.label_bdate = tk.Label(top)
        self.label_bdate.place(relx=0.053, rely=0.328, height=23, width=55)
        self.label_bdate.configure(activebackground="#f9f9f9")
        self.label_bdate.configure(activeforeground="black")
        self.label_bdate.configure(background="#d9d9d9")
        self.label_bdate.configure(disabledforeground="#a3a3a3")
        self.label_bdate.configure(foreground="#000000")
        self.label_bdate.configure(highlightbackground="#d9d9d9")
        self.label_bdate.configure(highlightcolor="black")
        self.label_bdate.configure(text='''Bdate:''')

        self.label_bplace = tk.Label(top)
        self.label_bplace.place(relx=0.053, rely=0.459, height=23, width=55)
        self.label_bplace.configure(activebackground="#f9f9f9")
        self.label_bplace.configure(activeforeground="black")
        self.label_bplace.configure(background="#d9d9d9")
        self.label_bplace.configure(disabledforeground="#a3a3a3")
        self.label_bplace.configure(foreground="#000000")
        self.label_bplace.configure(highlightbackground="#d9d9d9")
        self.label_bplace.configure(highlightcolor="black")
        self.label_bplace.configure(text='''Bplace:''')

        self.label_address = tk.Label(top)
        self.label_address.place(relx=0.053, rely=0.59, height=23, width=55)
        self.label_address.configure(activebackground="#f9f9f9")
        self.label_address.configure(activeforeground="black")
        self.label_address.configure(background="#d9d9d9")
        self.label_address.configure(disabledforeground="#a3a3a3")
        self.label_address.configure(foreground="#000000")
        self.label_address.configure(highlightbackground="#d9d9d9")
        self.label_address.configure(highlightcolor="black")
        self.label_address.configure(text='''Address:''')

        self.entry_fname = tk.Entry(top)
        self.entry_fname.place(relx=0.214, rely=0.066, height=17, relwidth=0.733)

        self.entry_fname.configure(background="white")
        self.entry_fname.configure(disabledforeground="#a3a3a3")
        self.entry_fname.configure(font="TkFixedFont")
        self.entry_fname.configure(foreground="#000000")
        self.entry_fname.configure(insertbackground="black")
        self.entry_fname.configure(state='readonly')

        self.entry_lname = tk.Entry(top)
        self.entry_lname.place(relx=0.214, rely=0.197, height=17, relwidth=0.733)

        self.entry_lname.configure(background="white")
        self.entry_lname.configure(disabledforeground="#a3a3a3")
        self.entry_lname.configure(font="TkFixedFont")
        self.entry_lname.configure(foreground="#000000")
        self.entry_lname.configure(highlightbackground="#d9d9d9")
        self.entry_lname.configure(highlightcolor="black")
        self.entry_lname.configure(insertbackground="black")
        self.entry_lname.configure(selectbackground="#c4c4c4")
        self.entry_lname.configure(selectforeground="black")
        self.entry_lname.configure(state='readonly')

        self.entry_bdate = tk.Entry(top)
        self.entry_bdate.place(relx=0.214, rely=0.328, height=17, relwidth=0.733)

        self.entry_bdate.configure(background="white")
        self.entry_bdate.configure(disabledforeground="#a3a3a3")
        self.entry_bdate.configure(font="TkFixedFont")
        self.entry_bdate.configure(foreground="#000000")
        self.entry_bdate.configure(highlightbackground="#d9d9d9")
        self.entry_bdate.configure(highlightcolor="black")
        self.entry_bdate.configure(insertbackground="black")
        self.entry_bdate.configure(selectbackground="#c4c4c4")
        self.entry_bdate.configure(selectforeground="black")

        self.entry_bplace = tk.Entry(top)
        self.entry_bplace.place(relx=0.214, rely=0.459, height=17
                , relwidth=0.733)
        self.entry_bplace.configure(background="white")
        self.entry_bplace.configure(disabledforeground="#a3a3a3")
        self.entry_bplace.configure(font="TkFixedFont")
        self.entry_bplace.configure(foreground="#000000")
        self.entry_bplace.configure(highlightbackground="#d9d9d9")
        self.entry_bplace.configure(highlightcolor="black")
        self.entry_bplace.configure(insertbackground="black")
        self.entry_bplace.configure(selectbackground="#c4c4c4")
        self.entry_bplace.configure(selectforeground="black")

        self.entry_address = tk.Entry(top)
        self.entry_address.place(relx=0.214, rely=0.59, height=17
                , relwidth=0.733)
        self.entry_address.configure(background="white")
        self.entry_address.configure(disabledforeground="#a3a3a3")
        self.entry_address.configure(font="TkFixedFont")
        self.entry_address.configure(foreground="#000000")
        self.entry_address.configure(highlightbackground="#d9d9d9")
        self.entry_address.configure(highlightcolor="black")
        self.entry_address.configure(insertbackground="black")
        self.entry_address.configure(selectbackground="#c4c4c4")
        self.entry_address.configure(selectforeground="black")

        self.entry_phone = tk.Entry(top)
        self.entry_phone.place(relx=0.214, rely=0.721, height=17, relwidth=0.733)

        self.entry_phone.configure(background="white")
        self.entry_phone.configure(disabledforeground="#a3a3a3")
        self.entry_phone.configure(font="TkFixedFont")
        self.entry_phone.configure(foreground="#000000")
        self.entry_phone.configure(highlightbackground="#d9d9d9")
        self.entry_phone.configure(highlightcolor="black")
        self.entry_phone.configure(insertbackground="black")
        self.entry_phone.configure(selectbackground="#c4c4c4")
        self.entry_phone.configure(selectforeground="black")

        self.label_phone = tk.Label(top)
        self.label_phone.place(relx=0.053, rely=0.721, height=23, width=55)
        self.label_phone.configure(activebackground="#f9f9f9")
        self.label_phone.configure(activeforeground="black")
        self.label_phone.configure(background="#d9d9d9")
        self.label_phone.configure(disabledforeground="#a3a3a3")
        self.label_phone.configure(foreground="#000000")
        self.label_phone.configure(highlightbackground="#d9d9d9")
        self.label_phone.configure(highlightcolor="black")
        self.label_phone.configure(text='''Phone:''')

        self.button_apply = tk.Button(top)
        self.button_apply.place(relx=0.802, rely=0.852, height=28, width=44)
        self.button_apply.configure(activebackground="#ececec")
        self.button_apply.configure(activeforeground="#000000")
        self.button_apply.configure(background="#d9d9d9")
        self.button_apply.configure(disabledforeground="#a3a3a3")
        self.button_apply.configure(foreground="#000000")
        self.button_apply.configure(highlightbackground="#d9d9d9")
        self.button_apply.configure(highlightcolor="black")
        self.button_apply.configure(pady="0")
        self.button_apply.configure(text='''Apply''')
        self.button_apply.configure(command=form_register_a_birth_mother_support.button_apply_click)

if __name__ == '__main__':
    vp_start_gui()





