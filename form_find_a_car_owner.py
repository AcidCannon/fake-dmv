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

import form_find_a_car_owner_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = form_find_a_car_owner (root)
    form_find_a_car_owner_support.init(root, top)
    root.mainloop()

w = None
def create_form_find_a_car_owner(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = form_find_a_car_owner (w)
    form_find_a_car_owner_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_form_find_a_car_owner():
    global w
    w.destroy()
    w = None

class form_find_a_car_owner:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("947x708+500+500")
        top.title("Officer - Find a car owner")
        top.configure(background="#d9d9d9")

        self.labelframe_information = tk.LabelFrame(top)
        self.labelframe_information.place(relx=0.021, rely=0.014, relheight=0.374
                , relwidth=0.306)
        self.labelframe_information.configure(relief='groove')
        self.labelframe_information.configure(foreground="black")
        self.labelframe_information.configure(text='''Information''')
        self.labelframe_information.configure(background="#d9d9d9")

        self.label_make = tk.Label(self.labelframe_information)
        self.label_make.place(relx=0.069, rely=0.113, height=20, width=40
                , bordermode='ignore')
        self.label_make.configure(activebackground="#f9f9f9")
        self.label_make.configure(activeforeground="black")
        self.label_make.configure(background="#d9d9d9")
        self.label_make.configure(disabledforeground="#a3a3a3")
        self.label_make.configure(foreground="#000000")
        self.label_make.configure(highlightbackground="#d9d9d9")
        self.label_make.configure(highlightcolor="black")
        self.label_make.configure(text='''Make:''')

        self.label_model = tk.Label(self.labelframe_information)
        self.label_model.place(relx=0.069, rely=0.264, height=20, width=40
                , bordermode='ignore')
        self.label_model.configure(activebackground="#f9f9f9")
        self.label_model.configure(activeforeground="black")
        self.label_model.configure(background="#d9d9d9")
        self.label_model.configure(disabledforeground="#a3a3a3")
        self.label_model.configure(foreground="#000000")
        self.label_model.configure(highlightbackground="#d9d9d9")
        self.label_model.configure(highlightcolor="black")
        self.label_model.configure(text='''Model:''')

        self.label_year = tk.Label(self.labelframe_information)
        self.label_year.place(relx=0.069, rely=0.415, height=20, width=40
                , bordermode='ignore')
        self.label_year.configure(activebackground="#f9f9f9")
        self.label_year.configure(activeforeground="black")
        self.label_year.configure(background="#d9d9d9")
        self.label_year.configure(disabledforeground="#a3a3a3")
        self.label_year.configure(foreground="#000000")
        self.label_year.configure(highlightbackground="#d9d9d9")
        self.label_year.configure(highlightcolor="black")
        self.label_year.configure(text='''Year:''')

        self.label_color = tk.Label(self.labelframe_information)
        self.label_color.place(relx=0.069, rely=0.566, height=20, width=40
                , bordermode='ignore')
        self.label_color.configure(activebackground="#f9f9f9")
        self.label_color.configure(activeforeground="black")
        self.label_color.configure(background="#d9d9d9")
        self.label_color.configure(disabledforeground="#a3a3a3")
        self.label_color.configure(foreground="#000000")
        self.label_color.configure(highlightbackground="#d9d9d9")
        self.label_color.configure(highlightcolor="black")
        self.label_color.configure(text='''Color:''')

        self.label_plate = tk.Label(self.labelframe_information)
        self.label_plate.place(relx=0.069, rely=0.717, height=20, width=40
                , bordermode='ignore')
        self.label_plate.configure(activebackground="#f9f9f9")
        self.label_plate.configure(activeforeground="black")
        self.label_plate.configure(background="#d9d9d9")
        self.label_plate.configure(disabledforeground="#a3a3a3")
        self.label_plate.configure(foreground="#000000")
        self.label_plate.configure(highlightbackground="#d9d9d9")
        self.label_plate.configure(highlightcolor="black")
        self.label_plate.configure(text='''Plate:''')

        self.entry_make = tk.Entry(self.labelframe_information)
        self.entry_make.place(relx=0.241, rely=0.113, height=17, relwidth=0.669
                , bordermode='ignore')
        self.entry_make.configure(background="white")
        self.entry_make.configure(disabledforeground="#a3a3a3")
        self.entry_make.configure(font="TkFixedFont")
        self.entry_make.configure(foreground="#000000")
        self.entry_make.configure(highlightbackground="#d9d9d9")
        self.entry_make.configure(highlightcolor="black")
        self.entry_make.configure(insertbackground="black")
        self.entry_make.configure(selectbackground="#c4c4c4")
        self.entry_make.configure(selectforeground="black")

        self.entry_model = tk.Entry(self.labelframe_information)
        self.entry_model.place(relx=0.241, rely=0.264, height=17, relwidth=0.669
                , bordermode='ignore')
        self.entry_model.configure(background="white")
        self.entry_model.configure(disabledforeground="#a3a3a3")
        self.entry_model.configure(font="TkFixedFont")
        self.entry_model.configure(foreground="#000000")
        self.entry_model.configure(highlightbackground="#d9d9d9")
        self.entry_model.configure(highlightcolor="black")
        self.entry_model.configure(insertbackground="black")
        self.entry_model.configure(selectbackground="#c4c4c4")
        self.entry_model.configure(selectforeground="black")

        self.entry_year = tk.Entry(self.labelframe_information)
        self.entry_year.place(relx=0.241, rely=0.415, height=17, relwidth=0.669
                , bordermode='ignore')
        self.entry_year.configure(background="white")
        self.entry_year.configure(disabledforeground="#a3a3a3")
        self.entry_year.configure(font="TkFixedFont")
        self.entry_year.configure(foreground="#000000")
        self.entry_year.configure(highlightbackground="#d9d9d9")
        self.entry_year.configure(highlightcolor="black")
        self.entry_year.configure(insertbackground="black")
        self.entry_year.configure(selectbackground="#c4c4c4")
        self.entry_year.configure(selectforeground="black")

        self.entry_color = tk.Entry(self.labelframe_information)
        self.entry_color.place(relx=0.241, rely=0.566, height=17, relwidth=0.669
                , bordermode='ignore')
        self.entry_color.configure(background="white")
        self.entry_color.configure(disabledforeground="#a3a3a3")
        self.entry_color.configure(font="TkFixedFont")
        self.entry_color.configure(foreground="#000000")
        self.entry_color.configure(highlightbackground="#d9d9d9")
        self.entry_color.configure(highlightcolor="black")
        self.entry_color.configure(insertbackground="black")
        self.entry_color.configure(selectbackground="#c4c4c4")
        self.entry_color.configure(selectforeground="black")

        self.entry_plate = tk.Entry(self.labelframe_information)
        self.entry_plate.place(relx=0.241, rely=0.717, height=17, relwidth=0.669
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

        self.button_check = tk.Button(self.labelframe_information)
        self.button_check.place(relx=0.759, rely=0.83, height=28, width=49
                , bordermode='ignore')
        self.button_check.configure(activebackground="#ececec")
        self.button_check.configure(activeforeground="#000000")
        self.button_check.configure(background="#d9d9d9")
        self.button_check.configure(command=form_find_a_car_owner_support.button_check_click)
        self.button_check.configure(disabledforeground="#a3a3a3")
        self.button_check.configure(foreground="#000000")
        self.button_check.configure(highlightbackground="#d9d9d9")
        self.button_check.configure(highlightcolor="black")
        self.button_check.configure(pady="0")
        self.button_check.configure(text='''Check''')

        self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        self.scrolledtreeview_result = ScrolledTreeView(top)
        self.scrolledtreeview_result.place(relx=0.021, rely=0.41, relheight=0.561
                , relwidth=0.961)
        self.scrolledtreeview_result.configure(columns="Col1 Col2 Col3 Col4 Col5")
        # build_treeview_support starting.
        self.scrolledtreeview_result.heading("#0",text="Index")
        self.scrolledtreeview_result.heading("#0",anchor="center")
        self.scrolledtreeview_result.column("#0",width="49")
        self.scrolledtreeview_result.column("#0",minwidth="20")
        self.scrolledtreeview_result.column("#0",stretch="1")
        self.scrolledtreeview_result.column("#0",anchor="w")
        self.scrolledtreeview_result.heading("Col1",text="Make")
        self.scrolledtreeview_result.heading("Col1",anchor="center")
        self.scrolledtreeview_result.column("Col1",width="199")
        self.scrolledtreeview_result.column("Col1",minwidth="20")
        self.scrolledtreeview_result.column("Col1",stretch="1")
        self.scrolledtreeview_result.column("Col1",anchor="w")
        self.scrolledtreeview_result.heading("Col2",text="Model")
        self.scrolledtreeview_result.heading("Col2",anchor="center")
        self.scrolledtreeview_result.column("Col2",width="198")
        self.scrolledtreeview_result.column("Col2",minwidth="20")
        self.scrolledtreeview_result.column("Col2",stretch="1")
        self.scrolledtreeview_result.column("Col2",anchor="w")
        self.scrolledtreeview_result.heading("Col3",text="Year")
        self.scrolledtreeview_result.heading("Col3",anchor="center")
        self.scrolledtreeview_result.column("Col3",width="48")
        self.scrolledtreeview_result.column("Col3",minwidth="20")
        self.scrolledtreeview_result.column("Col3",stretch="1")
        self.scrolledtreeview_result.column("Col3",anchor="w")
        self.scrolledtreeview_result.heading("Col4",text="Color")
        self.scrolledtreeview_result.heading("Col4",anchor="center")
        self.scrolledtreeview_result.column("Col4",width="198")
        self.scrolledtreeview_result.column("Col4",minwidth="20")
        self.scrolledtreeview_result.column("Col4",stretch="1")
        self.scrolledtreeview_result.column("Col4",anchor="w")
        self.scrolledtreeview_result.heading("Col5",text="Plate")
        self.scrolledtreeview_result.heading("Col5",anchor="center")
        self.scrolledtreeview_result.column("Col5",width="199")
        self.scrolledtreeview_result.column("Col5",minwidth="20")
        self.scrolledtreeview_result.column("Col5",stretch="1")
        self.scrolledtreeview_result.column("Col5",anchor="w")
        self.scrolledtreeview_result.bind("<Double-Button-1>", form_find_a_car_owner_support.scrolledtreeview_result_double_click)

        self.labelframe_details = tk.LabelFrame(top)
        self.labelframe_details.place(relx=0.348, rely=0.014, relheight=0.374
                , relwidth=0.634)
        self.labelframe_details.configure(relief='groove')
        self.labelframe_details.configure(foreground="black")
        self.labelframe_details.configure(text='''Details''')
        self.labelframe_details.configure(background="#d9d9d9")

        self.label_fname = tk.Label(self.labelframe_details)
        self.label_fname.place(relx=0.083, rely=0.113, height=15, width=69
                , bordermode='ignore')
        self.label_fname.configure(background="#d9d9d9")
        self.label_fname.configure(disabledforeground="#a3a3a3")
        self.label_fname.configure(foreground="#000000")
        self.label_fname.configure(text='''First name:''')

        self.label_lname = tk.Label(self.labelframe_details)
        self.label_lname.place(relx=0.083, rely=0.208, height=15, width=68
                , bordermode='ignore')
        self.label_lname.configure(background="#d9d9d9")
        self.label_lname.configure(disabledforeground="#a3a3a3")
        self.label_lname.configure(foreground="#000000")
        self.label_lname.configure(text='''Last name:''')

        self.label_regdate = tk.Label(self.labelframe_details)
        self.label_regdate.place(relx=0.017, rely=0.302, height=15, width=109
                , bordermode='ignore')
        self.label_regdate.configure(background="#d9d9d9")
        self.label_regdate.configure(disabledforeground="#a3a3a3")
        self.label_regdate.configure(foreground="#000000")
        self.label_regdate.configure(text='''Registration date:''')

        self.label_expiry = tk.Label(self.labelframe_details)
        self.label_expiry.place(relx=0.075, rely=0.396, height=15, width=74
                , bordermode='ignore')
        self.label_expiry.configure(background="#d9d9d9")
        self.label_expiry.configure(disabledforeground="#a3a3a3")
        self.label_expiry.configure(foreground="#000000")
        self.label_expiry.configure(text='''Expiry date:''')

        self.label_details_make = tk.Label(self.labelframe_details)
        self.label_details_make.place(relx=0.125, rely=0.491, height=15, width=42
                , bordermode='ignore')
        self.label_details_make.configure(background="#d9d9d9")
        self.label_details_make.configure(disabledforeground="#a3a3a3")
        self.label_details_make.configure(foreground="#000000")
        self.label_details_make.configure(text='''Make:''')

        self.label_details_model = tk.Label(self.labelframe_details)
        self.label_details_model.place(relx=0.117, rely=0.585, height=15
                , width=47, bordermode='ignore')
        self.label_details_model.configure(background="#d9d9d9")
        self.label_details_model.configure(disabledforeground="#a3a3a3")
        self.label_details_model.configure(foreground="#000000")
        self.label_details_model.configure(text='''Model:''')

        self.label_details_year = tk.Label(self.labelframe_details)
        self.label_details_year.place(relx=0.133, rely=0.679, height=15, width=35
                , bordermode='ignore')
        self.label_details_year.configure(background="#d9d9d9")
        self.label_details_year.configure(disabledforeground="#a3a3a3")
        self.label_details_year.configure(foreground="#000000")
        self.label_details_year.configure(text='''Year:''')

        self.label_details_color = tk.Label(self.labelframe_details)
        self.label_details_color.place(relx=0.125, rely=0.774, height=15
                , width=41, bordermode='ignore')
        self.label_details_color.configure(background="#d9d9d9")
        self.label_details_color.configure(disabledforeground="#a3a3a3")
        self.label_details_color.configure(foreground="#000000")
        self.label_details_color.configure(text='''Color:''')

        self.label_details_plate = tk.Label(self.labelframe_details)
        self.label_details_plate.place(relx=0.125, rely=0.868, height=15
                , width=37, bordermode='ignore')
        self.label_details_plate.configure(background="#d9d9d9")
        self.label_details_plate.configure(disabledforeground="#a3a3a3")
        self.label_details_plate.configure(foreground="#000000")
        self.label_details_plate.configure(text='''Plate:''')

        self.entry_fname = tk.Entry(self.labelframe_details)
        self.entry_fname.place(relx=0.2, rely=0.113, height=17, relwidth=0.757
                , bordermode='ignore')
        self.entry_fname.configure(background="white")
        self.entry_fname.configure(disabledforeground="#a3a3a3")
        self.entry_fname.configure(font="TkFixedFont")
        self.entry_fname.configure(foreground="#000000")
        self.entry_fname.configure(insertbackground="black")
        self.entry_fname.configure(state='readonly')

        self.entry_lname = tk.Entry(self.labelframe_details)
        self.entry_lname.place(relx=0.2, rely=0.208, height=17, relwidth=0.757
                , bordermode='ignore')
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

        self.entry_regdate = tk.Entry(self.labelframe_details)
        self.entry_regdate.place(relx=0.2, rely=0.302, height=17, relwidth=0.757
                , bordermode='ignore')
        self.entry_regdate.configure(background="white")
        self.entry_regdate.configure(disabledforeground="#a3a3a3")
        self.entry_regdate.configure(font="TkFixedFont")
        self.entry_regdate.configure(foreground="#000000")
        self.entry_regdate.configure(highlightbackground="#d9d9d9")
        self.entry_regdate.configure(highlightcolor="black")
        self.entry_regdate.configure(insertbackground="black")
        self.entry_regdate.configure(selectbackground="#c4c4c4")
        self.entry_regdate.configure(selectforeground="black")
        self.entry_regdate.configure(state='readonly')

        self.entry_expiry = tk.Entry(self.labelframe_details)
        self.entry_expiry.place(relx=0.2, rely=0.396, height=17, relwidth=0.757
                , bordermode='ignore')
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

        self.entry_details_make = tk.Entry(self.labelframe_details)
        self.entry_details_make.place(relx=0.2, rely=0.491, height=17
                , relwidth=0.757, bordermode='ignore')
        self.entry_details_make.configure(background="white")
        self.entry_details_make.configure(disabledforeground="#a3a3a3")
        self.entry_details_make.configure(font="TkFixedFont")
        self.entry_details_make.configure(foreground="#000000")
        self.entry_details_make.configure(highlightbackground="#d9d9d9")
        self.entry_details_make.configure(highlightcolor="black")
        self.entry_details_make.configure(insertbackground="black")
        self.entry_details_make.configure(selectbackground="#c4c4c4")
        self.entry_details_make.configure(selectforeground="black")
        self.entry_details_make.configure(state='readonly')

        self.entry_details_model = tk.Entry(self.labelframe_details)
        self.entry_details_model.place(relx=0.2, rely=0.585, height=17
                , relwidth=0.757, bordermode='ignore')
        self.entry_details_model.configure(background="white")
        self.entry_details_model.configure(disabledforeground="#a3a3a3")
        self.entry_details_model.configure(font="TkFixedFont")
        self.entry_details_model.configure(foreground="#000000")
        self.entry_details_model.configure(highlightbackground="#d9d9d9")
        self.entry_details_model.configure(highlightcolor="black")
        self.entry_details_model.configure(insertbackground="black")
        self.entry_details_model.configure(selectbackground="#c4c4c4")
        self.entry_details_model.configure(selectforeground="black")
        self.entry_details_model.configure(state='readonly')

        self.entry_details_year = tk.Entry(self.labelframe_details)
        self.entry_details_year.place(relx=0.2, rely=0.679, height=17
                , relwidth=0.757, bordermode='ignore')
        self.entry_details_year.configure(background="white")
        self.entry_details_year.configure(disabledforeground="#a3a3a3")
        self.entry_details_year.configure(font="TkFixedFont")
        self.entry_details_year.configure(foreground="#000000")
        self.entry_details_year.configure(highlightbackground="#d9d9d9")
        self.entry_details_year.configure(highlightcolor="black")
        self.entry_details_year.configure(insertbackground="black")
        self.entry_details_year.configure(selectbackground="#c4c4c4")
        self.entry_details_year.configure(selectforeground="black")
        self.entry_details_year.configure(state='readonly')

        self.entry_details_color = tk.Entry(self.labelframe_details)
        self.entry_details_color.place(relx=0.2, rely=0.774, height=17
                , relwidth=0.757, bordermode='ignore')
        self.entry_details_color.configure(background="white")
        self.entry_details_color.configure(disabledforeground="#a3a3a3")
        self.entry_details_color.configure(font="TkFixedFont")
        self.entry_details_color.configure(foreground="#000000")
        self.entry_details_color.configure(highlightbackground="#d9d9d9")
        self.entry_details_color.configure(highlightcolor="black")
        self.entry_details_color.configure(insertbackground="black")
        self.entry_details_color.configure(selectbackground="#c4c4c4")
        self.entry_details_color.configure(selectforeground="black")
        self.entry_details_color.configure(state='readonly')

        self.entry_details_plate = tk.Entry(self.labelframe_details)
        self.entry_details_plate.place(relx=0.2, rely=0.868, height=17
                , relwidth=0.757, bordermode='ignore')
        self.entry_details_plate.configure(background="white")
        self.entry_details_plate.configure(disabledforeground="#a3a3a3")
        self.entry_details_plate.configure(font="TkFixedFont")
        self.entry_details_plate.configure(foreground="#000000")
        self.entry_details_plate.configure(highlightbackground="#d9d9d9")
        self.entry_details_plate.configure(highlightcolor="black")
        self.entry_details_plate.configure(insertbackground="black")
        self.entry_details_plate.configure(selectbackground="#c4c4c4")
        self.entry_details_plate.configure(selectforeground="black")
        self.entry_details_plate.configure(state='readonly')

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





