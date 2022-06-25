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

import form_register_a_birth_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = form_register_a_birth (root)
    form_register_a_birth_support.init(root, top)
    root.mainloop()

w = None
def create_form_register_a_birth(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = form_register_a_birth (w)
    form_register_a_birth_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_form_register_a_birth():
    global w
    w.destroy()
    w = None

class form_register_a_birth:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("434x344+500+500")
        top.title("Agent - Register a birth")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.label_fname = tk.Label(top)
        self.label_fname.place(relx=0.023, rely=0.058, height=25, width=130)
        self.label_fname.configure(activebackground="#f9f9f9")
        self.label_fname.configure(activeforeground="black")
        self.label_fname.configure(background="#d9d9d9")
        self.label_fname.configure(disabledforeground="#a3a3a3")
        self.label_fname.configure(foreground="#000000")
        self.label_fname.configure(highlightbackground="#d9d9d9")
        self.label_fname.configure(highlightcolor="black")
        self.label_fname.configure(text='''First name:''')

        self.label_lname = tk.Label(top)
        self.label_lname.place(relx=0.023, rely=0.145, height=25, width=130)
        self.label_lname.configure(activebackground="#f9f9f9")
        self.label_lname.configure(activeforeground="black")
        self.label_lname.configure(background="#d9d9d9")
        self.label_lname.configure(disabledforeground="#a3a3a3")
        self.label_lname.configure(foreground="#000000")
        self.label_lname.configure(highlightbackground="#d9d9d9")
        self.label_lname.configure(highlightcolor="black")
        self.label_lname.configure(text='''Last name:''')

        self.label_gender = tk.Label(top)
        self.label_gender.place(relx=0.023, rely=0.233, height=25, width=130)
        self.label_gender.configure(activebackground="#f9f9f9")
        self.label_gender.configure(activeforeground="black")
        self.label_gender.configure(background="#d9d9d9")
        self.label_gender.configure(disabledforeground="#a3a3a3")
        self.label_gender.configure(foreground="#000000")
        self.label_gender.configure(highlightbackground="#d9d9d9")
        self.label_gender.configure(highlightcolor="black")
        self.label_gender.configure(text='''Gender:''')

        self.label_bplace = tk.Label(top)
        self.label_bplace.place(relx=0.023, rely=0.407, height=25, width=130)
        self.label_bplace.configure(activebackground="#f9f9f9")
        self.label_bplace.configure(activeforeground="black")
        self.label_bplace.configure(background="#d9d9d9")
        self.label_bplace.configure(disabledforeground="#a3a3a3")
        self.label_bplace.configure(foreground="#000000")
        self.label_bplace.configure(highlightbackground="#d9d9d9")
        self.label_bplace.configure(highlightcolor="black")
        self.label_bplace.configure(text='''Birth place:''')

        self.label_bdate = tk.Label(top)
        self.label_bdate.place(relx=0.023, rely=0.32, height=25, width=130)
        self.label_bdate.configure(activebackground="#f9f9f9")
        self.label_bdate.configure(activeforeground="black")
        self.label_bdate.configure(background="#d9d9d9")
        self.label_bdate.configure(disabledforeground="#a3a3a3")
        self.label_bdate.configure(foreground="#000000")
        self.label_bdate.configure(highlightbackground="#d9d9d9")
        self.label_bdate.configure(highlightcolor="black")
        self.label_bdate.configure(text='''Birth date:''')

        self.label_f_fname = tk.Label(top)
        self.label_f_fname.place(relx=0.023, rely=0.494, height=25, width=130)
        self.label_f_fname.configure(activebackground="#f9f9f9")
        self.label_f_fname.configure(activeforeground="black")
        self.label_f_fname.configure(background="#d9d9d9")
        self.label_f_fname.configure(disabledforeground="#a3a3a3")
        self.label_f_fname.configure(foreground="#000000")
        self.label_f_fname.configure(highlightbackground="#d9d9d9")
        self.label_f_fname.configure(highlightcolor="black")
        self.label_f_fname.configure(text='''Father first name:''')

        self.label_f_lname = tk.Label(top)
        self.label_f_lname.place(relx=0.023, rely=0.581, height=25, width=130)
        self.label_f_lname.configure(activebackground="#f9f9f9")
        self.label_f_lname.configure(activeforeground="black")
        self.label_f_lname.configure(background="#d9d9d9")
        self.label_f_lname.configure(disabledforeground="#a3a3a3")
        self.label_f_lname.configure(foreground="#000000")
        self.label_f_lname.configure(highlightbackground="#d9d9d9")
        self.label_f_lname.configure(highlightcolor="black")
        self.label_f_lname.configure(text='''Father last name:''')

        self.label_m_fname = tk.Label(top)
        self.label_m_fname.place(relx=0.023, rely=0.669, height=25, width=130)
        self.label_m_fname.configure(activebackground="#f9f9f9")
        self.label_m_fname.configure(activeforeground="black")
        self.label_m_fname.configure(background="#d9d9d9")
        self.label_m_fname.configure(disabledforeground="#a3a3a3")
        self.label_m_fname.configure(foreground="#000000")
        self.label_m_fname.configure(highlightbackground="#d9d9d9")
        self.label_m_fname.configure(highlightcolor="black")
        self.label_m_fname.configure(text='''Mother first name:''')

        self.label_m_lname = tk.Label(top)
        self.label_m_lname.place(relx=0.023, rely=0.756, height=25, width=130)
        self.label_m_lname.configure(activebackground="#f9f9f9")
        self.label_m_lname.configure(activeforeground="black")
        self.label_m_lname.configure(background="#d9d9d9")
        self.label_m_lname.configure(disabledforeground="#a3a3a3")
        self.label_m_lname.configure(foreground="#000000")
        self.label_m_lname.configure(highlightbackground="#d9d9d9")
        self.label_m_lname.configure(highlightcolor="black")
        self.label_m_lname.configure(text='''Mother last name:''')

        self.entry_fname = tk.Entry(top)
        self.entry_fname.place(relx=0.3, rely=0.073,height=17, relwidth=0.608)
        self.entry_fname.configure(background="white")
        self.entry_fname.configure(disabledforeground="#a3a3a3")
        self.entry_fname.configure(font="TkFixedFont")
        self.entry_fname.configure(foreground="#000000")
        self.entry_fname.configure(highlightbackground="#d9d9d9")
        self.entry_fname.configure(highlightcolor="black")
        self.entry_fname.configure(insertbackground="black")
        self.entry_fname.configure(selectbackground="#c4c4c4")
        self.entry_fname.configure(selectforeground="black")

        self.entry_lname = tk.Entry(top)
        self.entry_lname.place(relx=0.3, rely=0.16,height=17, relwidth=0.608)
        self.entry_lname.configure(background="white")
        self.entry_lname.configure(disabledforeground="#a3a3a3")
        self.entry_lname.configure(font="TkFixedFont")
        self.entry_lname.configure(foreground="#000000")
        self.entry_lname.configure(highlightbackground="#d9d9d9")
        self.entry_lname.configure(highlightcolor="black")
        self.entry_lname.configure(insertbackground="black")
        self.entry_lname.configure(selectbackground="#c4c4c4")
        self.entry_lname.configure(selectforeground="black")

        self.entry_gender = tk.Entry(top)
        self.entry_gender.place(relx=0.3, rely=0.247,height=17, relwidth=0.608)
        self.entry_gender.configure(background="white")
        self.entry_gender.configure(disabledforeground="#a3a3a3")
        self.entry_gender.configure(font="TkFixedFont")
        self.entry_gender.configure(foreground="#000000")
        self.entry_gender.configure(highlightbackground="#d9d9d9")
        self.entry_gender.configure(highlightcolor="black")
        self.entry_gender.configure(insertbackground="black")
        self.entry_gender.configure(selectbackground="#c4c4c4")
        self.entry_gender.configure(selectforeground="black")

        self.entry_bdate = tk.Entry(top)
        self.entry_bdate.place(relx=0.3, rely=0.334,height=17, relwidth=0.608)
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
        self.entry_bplace.place(relx=0.3, rely=0.422,height=17, relwidth=0.608)
        self.entry_bplace.configure(background="white")
        self.entry_bplace.configure(disabledforeground="#a3a3a3")
        self.entry_bplace.configure(font="TkFixedFont")
        self.entry_bplace.configure(foreground="#000000")
        self.entry_bplace.configure(highlightbackground="#d9d9d9")
        self.entry_bplace.configure(highlightcolor="black")
        self.entry_bplace.configure(insertbackground="black")
        self.entry_bplace.configure(selectbackground="#c4c4c4")
        self.entry_bplace.configure(selectforeground="black")

        self.entry_f_fname = tk.Entry(top)
        self.entry_f_fname.place(relx=0.3, rely=0.509, height=17, relwidth=0.608)

        self.entry_f_fname.configure(background="white")
        self.entry_f_fname.configure(disabledforeground="#a3a3a3")
        self.entry_f_fname.configure(font="TkFixedFont")
        self.entry_f_fname.configure(foreground="#000000")
        self.entry_f_fname.configure(highlightbackground="#d9d9d9")
        self.entry_f_fname.configure(highlightcolor="black")
        self.entry_f_fname.configure(insertbackground="black")
        self.entry_f_fname.configure(selectbackground="#c4c4c4")
        self.entry_f_fname.configure(selectforeground="black")

        self.entry_f_lname = tk.Entry(top)
        self.entry_f_lname.place(relx=0.3, rely=0.596, height=17, relwidth=0.608)

        self.entry_f_lname.configure(background="white")
        self.entry_f_lname.configure(disabledforeground="#a3a3a3")
        self.entry_f_lname.configure(font="TkFixedFont")
        self.entry_f_lname.configure(foreground="#000000")
        self.entry_f_lname.configure(highlightbackground="#d9d9d9")
        self.entry_f_lname.configure(highlightcolor="black")
        self.entry_f_lname.configure(insertbackground="black")
        self.entry_f_lname.configure(selectbackground="#c4c4c4")
        self.entry_f_lname.configure(selectforeground="black")

        self.entry_m_fname = tk.Entry(top)
        self.entry_m_fname.place(relx=0.3, rely=0.683, height=17, relwidth=0.608)

        self.entry_m_fname.configure(background="white")
        self.entry_m_fname.configure(disabledforeground="#a3a3a3")
        self.entry_m_fname.configure(font="TkFixedFont")
        self.entry_m_fname.configure(foreground="#000000")
        self.entry_m_fname.configure(highlightbackground="#d9d9d9")
        self.entry_m_fname.configure(highlightcolor="black")
        self.entry_m_fname.configure(insertbackground="black")
        self.entry_m_fname.configure(selectbackground="#c4c4c4")
        self.entry_m_fname.configure(selectforeground="black")

        self.entry_m_lname = tk.Entry(top)
        self.entry_m_lname.place(relx=0.3, rely=0.77,height=17, relwidth=0.608)
        self.entry_m_lname.configure(background="white")
        self.entry_m_lname.configure(disabledforeground="#a3a3a3")
        self.entry_m_lname.configure(font="TkFixedFont")
        self.entry_m_lname.configure(foreground="#000000")
        self.entry_m_lname.configure(highlightbackground="#d9d9d9")
        self.entry_m_lname.configure(highlightcolor="black")
        self.entry_m_lname.configure(insertbackground="black")
        self.entry_m_lname.configure(selectbackground="#c4c4c4")
        self.entry_m_lname.configure(selectforeground="black")

        self.button_availability = tk.Button(top)
        self.button_availability.place(relx=0.323, rely=0.858, height=28, width=69)
        self.button_availability.configure(activebackground="#ececec")
        self.button_availability.configure(activeforeground="#000000")
        self.button_availability.configure(background="#d9d9d9")
        self.button_availability.configure(command=form_register_a_birth_support.button_availability_click)
        self.button_availability.configure(disabledforeground="#a3a3a3")
        self.button_availability.configure(foreground="#000000")
        self.button_availability.configure(highlightbackground="#d9d9d9")
        self.button_availability.configure(highlightcolor="black")
        self.button_availability.configure(pady="0")
        self.button_availability.configure(text='''Availability''')

        self.button_mother = tk.Button(top)
        self.button_mother.place(relx=0.484, rely=0.858, height=28, width=69)
        self.button_mother.configure(activebackground="#ececec")
        self.button_mother.configure(activeforeground="#000000")
        self.button_mother.configure(background="#d9d9d9")
        self.button_mother.configure(command=form_register_a_birth_support.button_mother_click)
        self.button_mother.configure(disabledforeground="#a3a3a3")
        self.button_mother.configure(foreground="#000000")
        self.button_mother.configure(highlightbackground="#d9d9d9")
        self.button_mother.configure(highlightcolor="black")
        self.button_mother.configure(pady="0")
        self.button_mother.configure(text='''Mother''')
        self.button_mother.configure(state='disabled')

        self.button_father = tk.Button(top)
        self.button_father.place(relx=0.645, rely=0.858, height=28, width=69)
        self.button_father.configure(activebackground="#ececec")
        self.button_father.configure(activeforeground="#000000")
        self.button_father.configure(background="#d9d9d9")
        self.button_father.configure(command=form_register_a_birth_support.button_father_click)
        self.button_father.configure(disabledforeground="#a3a3a3")
        self.button_father.configure(foreground="#000000")
        self.button_father.configure(highlightbackground="#d9d9d9")
        self.button_father.configure(highlightcolor="black")
        self.button_father.configure(pady="0")
        self.button_father.configure(text='''Father''')
        self.button_father.configure(state='disabled')

        self.button_register = tk.Button(top)
        self.button_register.place(relx=0.806, rely=0.858, height=28, width=69)
        self.button_register.configure(activebackground="#ececec")
        self.button_register.configure(activeforeground="#000000")
        self.button_register.configure(background="#d9d9d9")
        self.button_register.configure(command=form_register_a_birth_support.button_register_click)
        self.button_register.configure(disabledforeground="#a3a3a3")
        self.button_register.configure(foreground="#000000")
        self.button_register.configure(highlightbackground="#d9d9d9")
        self.button_register.configure(highlightcolor="black")
        self.button_register.configure(pady="0")
        self.button_register.configure(state='disabled')
        self.button_register.configure(text='''Register''')

if __name__ == '__main__':
    vp_start_gui()