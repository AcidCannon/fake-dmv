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

import form_register_a_marriage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = form_register_a_marriage (root)
    form_register_a_marriage_support.init(root, top)
    root.mainloop()

w = None
def create_form_register_a_marriage(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = form_register_a_marriage (w)
    form_register_a_marriage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_form_register_a_marriage():
    global w
    w.destroy()
    w = None

class form_register_a_marriage:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1161x317+500+500")
        top.title("Agent - Register a marriage")
        top.configure(background="#d9d9d9")

        self.labelframe_partners = tk.LabelFrame(top)
        self.labelframe_partners.place(relx=0.017, rely=0.032, relheight=0.804
                , relwidth=0.31)
        self.labelframe_partners.configure(relief='groove')
        self.labelframe_partners.configure(foreground="black")
        self.labelframe_partners.configure(text='''Partners''')
        self.labelframe_partners.configure(background="#d9d9d9")

        self.label_p1_fname = tk.Label(self.labelframe_partners)
        self.label_p1_fname.place(relx=0.083, rely=0.157, height=23, width=69
                , bordermode='ignore')
        self.label_p1_fname.configure(background="#d9d9d9")
        self.label_p1_fname.configure(disabledforeground="#a3a3a3")
        self.label_p1_fname.configure(foreground="#000000")
        self.label_p1_fname.configure(text='''First name:''')

        self.label_p1_lname = tk.Label(self.labelframe_partners)
        self.label_p1_lname.place(relx=0.083, rely=0.353, height=23, width=68
                , bordermode='ignore')
        self.label_p1_lname.configure(background="#d9d9d9")
        self.label_p1_lname.configure(disabledforeground="#a3a3a3")
        self.label_p1_lname.configure(foreground="#000000")
        self.label_p1_lname.configure(text='''Last name:''')

        self.label_p2_fname = tk.Label(self.labelframe_partners)
        self.label_p2_fname.place(relx=0.083, rely=0.549, height=23, width=69
                , bordermode='ignore')
        self.label_p2_fname.configure(background="#d9d9d9")
        self.label_p2_fname.configure(disabledforeground="#a3a3a3")
        self.label_p2_fname.configure(foreground="#000000")
        self.label_p2_fname.configure(text='''First name:''')

        self.label_p2_lname = tk.Label(self.labelframe_partners)
        self.label_p2_lname.place(relx=0.083, rely=0.745, height=23, width=68
                , bordermode='ignore')
        self.label_p2_lname.configure(background="#d9d9d9")
        self.label_p2_lname.configure(disabledforeground="#a3a3a3")
        self.label_p2_lname.configure(foreground="#000000")
        self.label_p2_lname.configure(text='''Last name:''')

        self.entry_p1_fname = tk.Entry(self.labelframe_partners)
        self.entry_p1_fname.place(relx=0.306, rely=0.157, height=17
                , relwidth=0.622, bordermode='ignore')
        self.entry_p1_fname.configure(background="white")
        self.entry_p1_fname.configure(disabledforeground="#a3a3a3")
        self.entry_p1_fname.configure(font="TkFixedFont")
        self.entry_p1_fname.configure(foreground="#000000")
        self.entry_p1_fname.configure(insertbackground="black")

        self.entry_p1_lname = tk.Entry(self.labelframe_partners)
        self.entry_p1_lname.place(relx=0.306, rely=0.353, height=17
                , relwidth=0.622, bordermode='ignore')
        self.entry_p1_lname.configure(background="white")
        self.entry_p1_lname.configure(disabledforeground="#a3a3a3")
        self.entry_p1_lname.configure(font="TkFixedFont")
        self.entry_p1_lname.configure(foreground="#000000")
        self.entry_p1_lname.configure(insertbackground="black")

        self.entry_p2_fname = tk.Entry(self.labelframe_partners)
        self.entry_p2_fname.place(relx=0.306, rely=0.549, height=17
                , relwidth=0.622, bordermode='ignore')
        self.entry_p2_fname.configure(background="white")
        self.entry_p2_fname.configure(disabledforeground="#a3a3a3")
        self.entry_p2_fname.configure(font="TkFixedFont")
        self.entry_p2_fname.configure(foreground="#000000")
        self.entry_p2_fname.configure(insertbackground="black")

        self.entry_p2_lname = tk.Entry(self.labelframe_partners)
        self.entry_p2_lname.place(relx=0.306, rely=0.745, height=17
                , relwidth=0.622, bordermode='ignore')
        self.entry_p2_lname.configure(background="white")
        self.entry_p2_lname.configure(disabledforeground="#a3a3a3")
        self.entry_p2_lname.configure(font="TkFixedFont")
        self.entry_p2_lname.configure(foreground="#000000")
        self.entry_p2_lname.configure(insertbackground="black")

        self.button_check = tk.Button(self.labelframe_partners)
        self.button_check.place(relx=0.806, rely=0.863, height=28, width=46
                , bordermode='ignore')
        self.button_check.configure(activebackground="#ececec")
        self.button_check.configure(activeforeground="#000000")
        self.button_check.configure(background="#d9d9d9")
        self.button_check.configure(command=form_register_a_marriage_support.button_check_click)
        self.button_check.configure(disabledforeground="#a3a3a3")
        self.button_check.configure(foreground="#000000")
        self.button_check.configure(highlightbackground="#d9d9d9")
        self.button_check.configure(highlightcolor="black")
        self.button_check.configure(pady="0")
        self.button_check.configure(text='''Check''')

        self.labelframe_info_p1 = tk.LabelFrame(top)
        self.labelframe_info_p1.place(relx=0.345, rely=0.032, relheight=0.804
                , relwidth=0.31)
        self.labelframe_info_p1.configure(relief='groove')
        self.labelframe_info_p1.configure(foreground="black")
        self.labelframe_info_p1.configure(text='''Partner1''')
        self.labelframe_info_p1.configure(background="#d9d9d9")

        self.label_p1_bdate = tk.Label(self.labelframe_info_p1)
        self.label_p1_bdate.place(relx=0.083, rely=0.157, height=23, width=66
                , bordermode='ignore')
        self.label_p1_bdate.configure(background="#d9d9d9")
        self.label_p1_bdate.configure(disabledforeground="#a3a3a3")
        self.label_p1_bdate.configure(foreground="#000000")
        self.label_p1_bdate.configure(text='''Birth date:''')

        self.label_p1_bplace = tk.Label(self.labelframe_info_p1)
        self.label_p1_bplace.place(relx=0.083, rely=0.353, height=23, width=71
                , bordermode='ignore')
        self.label_p1_bplace.configure(background="#d9d9d9")
        self.label_p1_bplace.configure(disabledforeground="#a3a3a3")
        self.label_p1_bplace.configure(foreground="#000000")
        self.label_p1_bplace.configure(text='''Birth place:''')

        self.label_p1_address = tk.Label(self.labelframe_info_p1)
        self.label_p1_address.place(relx=0.083, rely=0.549, height=23, width=57
                , bordermode='ignore')
        self.label_p1_address.configure(background="#d9d9d9")
        self.label_p1_address.configure(disabledforeground="#a3a3a3")
        self.label_p1_address.configure(foreground="#000000")
        self.label_p1_address.configure(text='''Address:''')

        self.label_p1_phone = tk.Label(self.labelframe_info_p1)
        self.label_p1_phone.place(relx=0.083, rely=0.745, height=23, width=45
                , bordermode='ignore')
        self.label_p1_phone.configure(background="#d9d9d9")
        self.label_p1_phone.configure(disabledforeground="#a3a3a3")
        self.label_p1_phone.configure(foreground="#000000")
        self.label_p1_phone.configure(text='''Phone:''')

        self.entry_p1_bdate = tk.Entry(self.labelframe_info_p1)
        self.entry_p1_bdate.place(relx=0.306, rely=0.157, height=17
                , relwidth=0.622, bordermode='ignore')
        self.entry_p1_bdate.configure(background="white")
        self.entry_p1_bdate.configure(disabledforeground="#a3a3a3")
        self.entry_p1_bdate.configure(font="TkFixedFont")
        self.entry_p1_bdate.configure(foreground="#000000")
        self.entry_p1_bdate.configure(insertbackground="black")
        self.entry_p1_bdate.configure(state='readonly')

        self.entry_p1_bplace = tk.Entry(self.labelframe_info_p1)
        self.entry_p1_bplace.place(relx=0.306, rely=0.353, height=17
                , relwidth=0.622, bordermode='ignore')
        self.entry_p1_bplace.configure(background="white")
        self.entry_p1_bplace.configure(disabledforeground="#a3a3a3")
        self.entry_p1_bplace.configure(font="TkFixedFont")
        self.entry_p1_bplace.configure(foreground="#000000")
        self.entry_p1_bplace.configure(highlightbackground="#d9d9d9")
        self.entry_p1_bplace.configure(highlightcolor="black")
        self.entry_p1_bplace.configure(insertbackground="black")
        self.entry_p1_bplace.configure(selectbackground="#c4c4c4")
        self.entry_p1_bplace.configure(selectforeground="black")
        self.entry_p1_bplace.configure(state='readonly')

        self.entry_p1_address = tk.Entry(self.labelframe_info_p1)
        self.entry_p1_address.place(relx=0.306, rely=0.549, height=17
                , relwidth=0.622, bordermode='ignore')
        self.entry_p1_address.configure(background="white")
        self.entry_p1_address.configure(disabledforeground="#a3a3a3")
        self.entry_p1_address.configure(font="TkFixedFont")
        self.entry_p1_address.configure(foreground="#000000")
        self.entry_p1_address.configure(highlightbackground="#d9d9d9")
        self.entry_p1_address.configure(highlightcolor="black")
        self.entry_p1_address.configure(insertbackground="black")
        self.entry_p1_address.configure(selectbackground="#c4c4c4")
        self.entry_p1_address.configure(selectforeground="black")
        self.entry_p1_address.configure(state='readonly')

        self.entry_p1_phone = tk.Entry(self.labelframe_info_p1)
        self.entry_p1_phone.place(relx=0.306, rely=0.745, height=17
                , relwidth=0.622, bordermode='ignore')
        self.entry_p1_phone.configure(background="white")
        self.entry_p1_phone.configure(disabledforeground="#a3a3a3")
        self.entry_p1_phone.configure(font="TkFixedFont")
        self.entry_p1_phone.configure(foreground="#000000")
        self.entry_p1_phone.configure(highlightbackground="#d9d9d9")
        self.entry_p1_phone.configure(highlightcolor="black")
        self.entry_p1_phone.configure(insertbackground="black")
        self.entry_p1_phone.configure(selectbackground="#c4c4c4")
        self.entry_p1_phone.configure(selectforeground="black")
        self.entry_p1_phone.configure(state='readonly')

        self.button_p1_apply = tk.Button(self.labelframe_info_p1)
        self.button_p1_apply.place(relx=0.806, rely=0.863, height=28, width=44
                , bordermode='ignore')
        self.button_p1_apply.configure(activebackground="#ececec")
        self.button_p1_apply.configure(activeforeground="#000000")
        self.button_p1_apply.configure(background="#d9d9d9")
        self.button_p1_apply.configure(command=form_register_a_marriage_support.button_p1_apply_click)
        self.button_p1_apply.configure(disabledforeground="#a3a3a3")
        self.button_p1_apply.configure(foreground="#000000")
        self.button_p1_apply.configure(highlightbackground="#d9d9d9")
        self.button_p1_apply.configure(highlightcolor="black")
        self.button_p1_apply.configure(pady="0")
        self.button_p1_apply.configure(state='disabled')
        self.button_p1_apply.configure(text='''Apply''')

        self.labelframe_info_p2 = tk.LabelFrame(top)
        self.labelframe_info_p2.place(relx=0.672, rely=0.032, relheight=0.804
                , relwidth=0.31)
        self.labelframe_info_p2.configure(relief='groove')
        self.labelframe_info_p2.configure(foreground="black")
        self.labelframe_info_p2.configure(text='''Partner2''')
        self.labelframe_info_p2.configure(background="#d9d9d9")
        self.labelframe_info_p2.configure(highlightbackground="#d9d9d9")
        self.labelframe_info_p2.configure(highlightcolor="black")

        self.label_p2_bdate = tk.Label(self.labelframe_info_p2)
        self.label_p2_bdate.place(relx=0.083, rely=0.157, height=23, width=66
                , bordermode='ignore')
        self.label_p2_bdate.configure(activebackground="#f9f9f9")
        self.label_p2_bdate.configure(activeforeground="black")
        self.label_p2_bdate.configure(background="#d9d9d9")
        self.label_p2_bdate.configure(disabledforeground="#a3a3a3")
        self.label_p2_bdate.configure(foreground="#000000")
        self.label_p2_bdate.configure(highlightbackground="#d9d9d9")
        self.label_p2_bdate.configure(highlightcolor="black")
        self.label_p2_bdate.configure(text='''Birth date:''')

        self.label_p2_bplace = tk.Label(self.labelframe_info_p2)
        self.label_p2_bplace.place(relx=0.083, rely=0.353, height=23, width=71
                , bordermode='ignore')
        self.label_p2_bplace.configure(activebackground="#f9f9f9")
        self.label_p2_bplace.configure(activeforeground="black")
        self.label_p2_bplace.configure(background="#d9d9d9")
        self.label_p2_bplace.configure(disabledforeground="#a3a3a3")
        self.label_p2_bplace.configure(foreground="#000000")
        self.label_p2_bplace.configure(highlightbackground="#d9d9d9")
        self.label_p2_bplace.configure(highlightcolor="black")
        self.label_p2_bplace.configure(text='''Birth place:''')

        self.label_p2_address = tk.Label(self.labelframe_info_p2)
        self.label_p2_address.place(relx=0.083, rely=0.549, height=23, width=57
                , bordermode='ignore')
        self.label_p2_address.configure(activebackground="#f9f9f9")
        self.label_p2_address.configure(activeforeground="black")
        self.label_p2_address.configure(background="#d9d9d9")
        self.label_p2_address.configure(disabledforeground="#a3a3a3")
        self.label_p2_address.configure(foreground="#000000")
        self.label_p2_address.configure(highlightbackground="#d9d9d9")
        self.label_p2_address.configure(highlightcolor="black")
        self.label_p2_address.configure(text='''Address:''')

        self.label_p2_phone = tk.Label(self.labelframe_info_p2)
        self.label_p2_phone.place(relx=0.083, rely=0.745, height=23, width=45
                , bordermode='ignore')
        self.label_p2_phone.configure(activebackground="#f9f9f9")
        self.label_p2_phone.configure(activeforeground="black")
        self.label_p2_phone.configure(background="#d9d9d9")
        self.label_p2_phone.configure(disabledforeground="#a3a3a3")
        self.label_p2_phone.configure(foreground="#000000")
        self.label_p2_phone.configure(highlightbackground="#d9d9d9")
        self.label_p2_phone.configure(highlightcolor="black")
        self.label_p2_phone.configure(text='''Phone:''')

        self.entry_p2_bdate = tk.Entry(self.labelframe_info_p2)
        self.entry_p2_bdate.place(relx=0.306, rely=0.157, height=17
                , relwidth=0.622, bordermode='ignore')
        self.entry_p2_bdate.configure(background="white")
        self.entry_p2_bdate.configure(disabledforeground="#a3a3a3")
        self.entry_p2_bdate.configure(font="TkFixedFont")
        self.entry_p2_bdate.configure(foreground="#000000")
        self.entry_p2_bdate.configure(highlightbackground="#d9d9d9")
        self.entry_p2_bdate.configure(highlightcolor="black")
        self.entry_p2_bdate.configure(insertbackground="black")
        self.entry_p2_bdate.configure(selectbackground="#c4c4c4")
        self.entry_p2_bdate.configure(selectforeground="black")
        self.entry_p2_bdate.configure(state='readonly')

        self.entry_p2_bplace = tk.Entry(self.labelframe_info_p2)
        self.entry_p2_bplace.place(relx=0.306, rely=0.353, height=17
                , relwidth=0.622, bordermode='ignore')
        self.entry_p2_bplace.configure(background="white")
        self.entry_p2_bplace.configure(disabledforeground="#a3a3a3")
        self.entry_p2_bplace.configure(font="TkFixedFont")
        self.entry_p2_bplace.configure(foreground="#000000")
        self.entry_p2_bplace.configure(highlightbackground="#d9d9d9")
        self.entry_p2_bplace.configure(highlightcolor="black")
        self.entry_p2_bplace.configure(insertbackground="black")
        self.entry_p2_bplace.configure(selectbackground="#c4c4c4")
        self.entry_p2_bplace.configure(selectforeground="black")
        self.entry_p2_bplace.configure(state='readonly')

        self.entry_p2_address = tk.Entry(self.labelframe_info_p2)
        self.entry_p2_address.place(relx=0.306, rely=0.549, height=17
                , relwidth=0.622, bordermode='ignore')
        self.entry_p2_address.configure(background="white")
        self.entry_p2_address.configure(disabledforeground="#a3a3a3")
        self.entry_p2_address.configure(font="TkFixedFont")
        self.entry_p2_address.configure(foreground="#000000")
        self.entry_p2_address.configure(highlightbackground="#d9d9d9")
        self.entry_p2_address.configure(highlightcolor="black")
        self.entry_p2_address.configure(insertbackground="black")
        self.entry_p2_address.configure(selectbackground="#c4c4c4")
        self.entry_p2_address.configure(selectforeground="black")
        self.entry_p2_address.configure(state='readonly')

        self.entry_p2_phone = tk.Entry(self.labelframe_info_p2)
        self.entry_p2_phone.place(relx=0.306, rely=0.745, height=17
                , relwidth=0.622, bordermode='ignore')
        self.entry_p2_phone.configure(background="white")
        self.entry_p2_phone.configure(disabledforeground="#a3a3a3")
        self.entry_p2_phone.configure(font="TkFixedFont")
        self.entry_p2_phone.configure(foreground="#000000")
        self.entry_p2_phone.configure(highlightbackground="#d9d9d9")
        self.entry_p2_phone.configure(highlightcolor="black")
        self.entry_p2_phone.configure(insertbackground="black")
        self.entry_p2_phone.configure(selectbackground="#c4c4c4")
        self.entry_p2_phone.configure(selectforeground="black")
        self.entry_p2_phone.configure(state='readonly')

        self.button_p2_apply = tk.Button(self.labelframe_info_p2)
        self.button_p2_apply.place(relx=0.806, rely=0.863, height=28, width=44
                , bordermode='ignore')
        self.button_p2_apply.configure(activebackground="#ececec")
        self.button_p2_apply.configure(activeforeground="#000000")
        self.button_p2_apply.configure(background="#d9d9d9")
        self.button_p2_apply.configure(command=form_register_a_marriage_support.button_p2_apply_click)
        self.button_p2_apply.configure(disabledforeground="#a3a3a3")
        self.button_p2_apply.configure(foreground="#000000")
        self.button_p2_apply.configure(highlightbackground="#d9d9d9")
        self.button_p2_apply.configure(highlightcolor="black")
        self.button_p2_apply.configure(pady="0")
        self.button_p2_apply.configure(state='disabled')
        self.button_p2_apply.configure(text='''Apply''')

        self.button_register = tk.Button(top)
        self.button_register.place(relx=0.913, rely=0.883, height=28, width=59)
        self.button_register.configure(activebackground="#ececec")
        self.button_register.configure(activeforeground="#000000")
        self.button_register.configure(background="#d9d9d9")
        self.button_register.configure(command=form_register_a_marriage_support.button_register_click)
        self.button_register.configure(disabledforeground="#a3a3a3")
        self.button_register.configure(foreground="#000000")
        self.button_register.configure(highlightbackground="#d9d9d9")
        self.button_register.configure(highlightcolor="black")
        self.button_register.configure(pady="0")
        self.button_register.configure(state='disabled')
        self.button_register.configure(text='''Register''')

if __name__ == '__main__':
    vp_start_gui()