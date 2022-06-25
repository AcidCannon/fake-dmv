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

import form_get_a_driver_abstract_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = form_get_a_driver_abstract (root)
    form_get_a_driver_abstract_support.init(root, top)
    root.mainloop()

w = None
def create_form_get_a_driver_abstract(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = form_get_a_driver_abstract (w)
    form_get_a_driver_abstract_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_form_get_a_driver_abstract():
    global w
    w.destroy()
    w = None

class form_get_a_driver_abstract:
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

        top.geometry("764x450+500+500")
        top.title("Agent - Get a driver abstract")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.labelframe_driver = tk.LabelFrame(top)
        self.labelframe_driver.place(relx=0.026, rely=0.022, relheight=0.367
                , relwidth=0.353)
        self.labelframe_driver.configure(relief='groove')
        self.labelframe_driver.configure(foreground="black")
        self.labelframe_driver.configure(text='''Driver''')
        self.labelframe_driver.configure(background="#d9d9d9")
        self.labelframe_driver.configure(highlightbackground="#d9d9d9")
        self.labelframe_driver.configure(highlightcolor="black")

        self.label_fname = tk.Label(self.labelframe_driver)
        self.label_fname.place(relx=0.074, rely=0.242, height=23, width=45
                , bordermode='ignore')
        self.label_fname.configure(activebackground="#f9f9f9")
        self.label_fname.configure(activeforeground="black")
        self.label_fname.configure(background="#d9d9d9")
        self.label_fname.configure(disabledforeground="#a3a3a3")
        self.label_fname.configure(foreground="#000000")
        self.label_fname.configure(highlightbackground="#d9d9d9")
        self.label_fname.configure(highlightcolor="black")
        self.label_fname.configure(text='''fname:''')

        self.label_lname = tk.Label(self.labelframe_driver)
        self.label_lname.place(relx=0.074, rely=0.545, height=23, width=44
                , bordermode='ignore')
        self.label_lname.configure(activebackground="#f9f9f9")
        self.label_lname.configure(activeforeground="black")
        self.label_lname.configure(background="#d9d9d9")
        self.label_lname.configure(disabledforeground="#a3a3a3")
        self.label_lname.configure(foreground="#000000")
        self.label_lname.configure(highlightbackground="#d9d9d9")
        self.label_lname.configure(highlightcolor="black")
        self.label_lname.configure(text='''lname:''')

        self.entry_fname = tk.Entry(self.labelframe_driver)
        self.entry_fname.place(relx=0.259, rely=0.242, height=17, relwidth=0.681
                , bordermode='ignore')
        self.entry_fname.configure(background="white")
        self.entry_fname.configure(disabledforeground="#a3a3a3")
        self.entry_fname.configure(font="TkFixedFont")
        self.entry_fname.configure(foreground="#000000")
        self.entry_fname.configure(highlightbackground="#d9d9d9")
        self.entry_fname.configure(highlightcolor="black")
        self.entry_fname.configure(insertbackground="black")
        self.entry_fname.configure(selectbackground="#c4c4c4")
        self.entry_fname.configure(selectforeground="black")

        self.entry_lname = tk.Entry(self.labelframe_driver)
        self.entry_lname.place(relx=0.259, rely=0.545, height=17, relwidth=0.681
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

        self.button_check = tk.Button(self.labelframe_driver)
        self.button_check.place(relx=0.759, rely=0.727, height=28, width=46
                , bordermode='ignore')
        self.button_check.configure(activebackground="#ececec")
        self.button_check.configure(activeforeground="#000000")
        self.button_check.configure(background="#d9d9d9")
        self.button_check.configure(command=form_get_a_driver_abstract_support.button_check_click)
        self.button_check.configure(disabledforeground="#a3a3a3")
        self.button_check.configure(foreground="#000000")
        self.button_check.configure(highlightbackground="#d9d9d9")
        self.button_check.configure(highlightcolor="black")
        self.button_check.configure(pady="0")
        self.button_check.configure(text='''Check''')

        self.labelframe_abstract = tk.LabelFrame(top)
        self.labelframe_abstract.place(relx=0.406, rely=0.022, relheight=0.367
                , relwidth=0.563)
        self.labelframe_abstract.configure(relief='groove')
        self.labelframe_abstract.configure(foreground="black")
        self.labelframe_abstract.configure(text='''Abstract''')
        self.labelframe_abstract.configure(background="#d9d9d9")
        self.labelframe_abstract.configure(highlightbackground="#d9d9d9")
        self.labelframe_abstract.configure(highlightcolor="black")

        self.label_tickets_2year = tk.Label(self.labelframe_abstract)
        self.label_tickets_2year.place(relx=0.047, rely=0.182, height=23
                , width=135, bordermode='ignore')
        self.label_tickets_2year.configure(activebackground="#f9f9f9")
        self.label_tickets_2year.configure(activeforeground="black")
        self.label_tickets_2year.configure(background="#d9d9d9")
        self.label_tickets_2year.configure(disabledforeground="#a3a3a3")
        self.label_tickets_2year.configure(foreground="#000000")
        self.label_tickets_2year.configure(highlightbackground="#d9d9d9")
        self.label_tickets_2year.configure(highlightcolor="black")
        self.label_tickets_2year.configure(text='''#Tickets (last 2 years):''')

        self.label_demerit_notices_lifetime = tk.Label(self.labelframe_abstract)
        self.label_demerit_notices_lifetime.place(relx=0.047, rely=0.545
                , height=23, width=162, bordermode='ignore')
        self.label_demerit_notices_lifetime.configure(activebackground="#f9f9f9")
        self.label_demerit_notices_lifetime.configure(activeforeground="black")
        self.label_demerit_notices_lifetime.configure(background="#d9d9d9")
        self.label_demerit_notices_lifetime.configure(disabledforeground="#a3a3a3")
        self.label_demerit_notices_lifetime.configure(foreground="#000000")
        self.label_demerit_notices_lifetime.configure(highlightbackground="#d9d9d9")
        self.label_demerit_notices_lifetime.configure(highlightcolor="black")
        self.label_demerit_notices_lifetime.configure(text='''#Demerit notices (lifetime):''')

        self.entry_tickets_lifetime = tk.Entry(self.labelframe_abstract)
        self.entry_tickets_lifetime.place(relx=0.488, rely=0.303, height=17
                , relwidth=0.474, bordermode='ignore')
        self.entry_tickets_lifetime.configure(background="white")
        self.entry_tickets_lifetime.configure(disabledforeground="#a3a3a3")
        self.entry_tickets_lifetime.configure(font="TkFixedFont")
        self.entry_tickets_lifetime.configure(foreground="#000000")
        self.entry_tickets_lifetime.configure(highlightbackground="#d9d9d9")
        self.entry_tickets_lifetime.configure(highlightcolor="black")
        self.entry_tickets_lifetime.configure(insertbackground="black")
        self.entry_tickets_lifetime.configure(selectbackground="#c4c4c4")
        self.entry_tickets_lifetime.configure(selectforeground="black")
        self.entry_tickets_lifetime.configure(state='readonly')

        self.entry_demerit_notices_lifetime = tk.Entry(self.labelframe_abstract)
        self.entry_demerit_notices_lifetime.place(relx=0.488, rely=0.545
                ,height=17, relwidth=0.474, bordermode='ignore')
        self.entry_demerit_notices_lifetime.configure(background="white")
        self.entry_demerit_notices_lifetime.configure(disabledforeground="#a3a3a3")
        self.entry_demerit_notices_lifetime.configure(font="TkFixedFont")
        self.entry_demerit_notices_lifetime.configure(foreground="#000000")
        self.entry_demerit_notices_lifetime.configure(highlightbackground="#d9d9d9")
        self.entry_demerit_notices_lifetime.configure(highlightcolor="black")
        self.entry_demerit_notices_lifetime.configure(insertbackground="black")
        self.entry_demerit_notices_lifetime.configure(selectbackground="#c4c4c4")
        self.entry_demerit_notices_lifetime.configure(selectforeground="black")
        self.entry_demerit_notices_lifetime.configure(state='readonly')

        self.label_demerit_points_2year = tk.Label(self.labelframe_abstract)
        self.label_demerit_points_2year.place(relx=0.047, rely=0.667, height=23
                , width=181, bordermode='ignore')
        self.label_demerit_points_2year.configure(activebackground="#f9f9f9")
        self.label_demerit_points_2year.configure(activeforeground="black")
        self.label_demerit_points_2year.configure(background="#d9d9d9")
        self.label_demerit_points_2year.configure(disabledforeground="#a3a3a3")
        self.label_demerit_points_2year.configure(foreground="#000000")
        self.label_demerit_points_2year.configure(highlightbackground="#d9d9d9")
        self.label_demerit_points_2year.configure(highlightcolor="black")
        self.label_demerit_points_2year.configure(text='''#Demerit points (last 2 years):''')

        self.label_demerit_points_lifetime = tk.Label(self.labelframe_abstract)
        self.label_demerit_points_lifetime.place(relx=0.047, rely=0.788
                , height=23, width=157, bordermode='ignore')
        self.label_demerit_points_lifetime.configure(activebackground="#f9f9f9")
        self.label_demerit_points_lifetime.configure(activeforeground="black")
        self.label_demerit_points_lifetime.configure(background="#d9d9d9")
        self.label_demerit_points_lifetime.configure(disabledforeground="#a3a3a3")
        self.label_demerit_points_lifetime.configure(foreground="#000000")
        self.label_demerit_points_lifetime.configure(highlightbackground="#d9d9d9")
        self.label_demerit_points_lifetime.configure(highlightcolor="black")
        self.label_demerit_points_lifetime.configure(text='''#Demerit points (lifetime):''')

        self.entry_demerit_points_2_year = tk.Entry(self.labelframe_abstract)
        self.entry_demerit_points_2_year.place(relx=0.488, rely=0.667, height=17
                , relwidth=0.474, bordermode='ignore')
        self.entry_demerit_points_2_year.configure(background="white")
        self.entry_demerit_points_2_year.configure(disabledforeground="#a3a3a3")
        self.entry_demerit_points_2_year.configure(font="TkFixedFont")
        self.entry_demerit_points_2_year.configure(foreground="#000000")
        self.entry_demerit_points_2_year.configure(highlightbackground="#d9d9d9")
        self.entry_demerit_points_2_year.configure(highlightcolor="black")
        self.entry_demerit_points_2_year.configure(insertbackground="black")
        self.entry_demerit_points_2_year.configure(selectbackground="#c4c4c4")
        self.entry_demerit_points_2_year.configure(selectforeground="black")
        self.entry_demerit_points_2_year.configure(state='readonly')

        self.entry_demerit_points_lifetime = tk.Entry(self.labelframe_abstract)
        self.entry_demerit_points_lifetime.place(relx=0.488, rely=0.788, height=17
                , relwidth=0.474, bordermode='ignore')
        self.entry_demerit_points_lifetime.configure(background="white")
        self.entry_demerit_points_lifetime.configure(disabledforeground="#a3a3a3")
        self.entry_demerit_points_lifetime.configure(font="TkFixedFont")
        self.entry_demerit_points_lifetime.configure(foreground="#000000")
        self.entry_demerit_points_lifetime.configure(highlightbackground="#d9d9d9")
        self.entry_demerit_points_lifetime.configure(highlightcolor="black")
        self.entry_demerit_points_lifetime.configure(insertbackground="black")
        self.entry_demerit_points_lifetime.configure(selectbackground="#c4c4c4")
        self.entry_demerit_points_lifetime.configure(selectforeground="black")
        self.entry_demerit_points_lifetime.configure(state='readonly')

        self.label_demerit_notices_2_year = tk.Label(self.labelframe_abstract)
        self.label_demerit_notices_2_year.place(relx=0.047, rely=0.424, height=23
                , width=182, bordermode='ignore')
        self.label_demerit_notices_2_year.configure(activebackground="#f9f9f9")
        self.label_demerit_notices_2_year.configure(activeforeground="black")
        self.label_demerit_notices_2_year.configure(background="#d9d9d9")
        self.label_demerit_notices_2_year.configure(disabledforeground="#a3a3a3")
        self.label_demerit_notices_2_year.configure(foreground="#000000")
        self.label_demerit_notices_2_year.configure(highlightbackground="#d9d9d9")
        self.label_demerit_notices_2_year.configure(highlightcolor="black")
        self.label_demerit_notices_2_year.configure(text='''#Demerit notices (last 2 years):''')

        self.entry_demerit_notices_2year = tk.Entry(self.labelframe_abstract)
        self.entry_demerit_notices_2year.place(relx=0.488, rely=0.424, height=17
                , relwidth=0.474, bordermode='ignore')
        self.entry_demerit_notices_2year.configure(background="white")
        self.entry_demerit_notices_2year.configure(disabledforeground="#a3a3a3")
        self.entry_demerit_notices_2year.configure(font="TkFixedFont")
        self.entry_demerit_notices_2year.configure(foreground="#000000")
        self.entry_demerit_notices_2year.configure(insertbackground="black")
        self.entry_demerit_notices_2year.configure(state='readonly')

        self.label_tickets_lifetime = tk.Label(self.labelframe_abstract)
        self.label_tickets_lifetime.place(relx=0.047, rely=0.303, height=23
                , width=111, bordermode='ignore')
        self.label_tickets_lifetime.configure(background="#d9d9d9")
        self.label_tickets_lifetime.configure(disabledforeground="#a3a3a3")
        self.label_tickets_lifetime.configure(foreground="#000000")
        self.label_tickets_lifetime.configure(text='''#Tickets (lifetime):''')

        self.entry_tickets_2year = tk.Entry(self.labelframe_abstract)
        self.entry_tickets_2year.place(relx=0.488, rely=0.182, height=17
                , relwidth=0.474, bordermode='ignore')
        self.entry_tickets_2year.configure(background="white")
        self.entry_tickets_2year.configure(disabledforeground="#a3a3a3")
        self.entry_tickets_2year.configure(font="TkFixedFont")
        self.entry_tickets_2year.configure(foreground="#000000")
        self.entry_tickets_2year.configure(insertbackground="black")
        self.entry_tickets_2year.configure(state='readonly')

        self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        self.scrolledtreeview_tickets = ScrolledTreeView(top)
        self.scrolledtreeview_tickets.place(relx=0.026, rely=0.422
                , relheight=0.482, relwidth=0.97)
        self.scrolledtreeview_tickets.configure(columns="Col1 Col2 Col3 Col4 Col5 Col6 Col7")
        # build_treeview_support starting.
        self.scrolledtreeview_tickets.heading("#0",text=" ")
        self.scrolledtreeview_tickets.heading("#0",anchor="center")
        self.scrolledtreeview_tickets.column("#0",width="24")
        self.scrolledtreeview_tickets.column("#0",minwidth="20")
        self.scrolledtreeview_tickets.column("#0",stretch="1")
        self.scrolledtreeview_tickets.column("#0",anchor="w")
        self.scrolledtreeview_tickets.heading("Col1",text="tno")
        self.scrolledtreeview_tickets.heading("Col1",anchor="center")
        self.scrolledtreeview_tickets.column("Col1",width="39")
        self.scrolledtreeview_tickets.column("Col1",minwidth="20")
        self.scrolledtreeview_tickets.column("Col1",stretch="1")
        self.scrolledtreeview_tickets.column("Col1",anchor="w")
        self.scrolledtreeview_tickets.heading("Col2",text="vdate")
        self.scrolledtreeview_tickets.heading("Col2",anchor="center")
        self.scrolledtreeview_tickets.column("Col2",width="81")
        self.scrolledtreeview_tickets.column("Col2",minwidth="20")
        self.scrolledtreeview_tickets.column("Col2",stretch="1")
        self.scrolledtreeview_tickets.column("Col2",anchor="w")
        self.scrolledtreeview_tickets.heading("Col3",text="description")
        self.scrolledtreeview_tickets.heading("Col3",anchor="center")
        self.scrolledtreeview_tickets.column("Col3",width="200")
        self.scrolledtreeview_tickets.column("Col3",minwidth="20")
        self.scrolledtreeview_tickets.column("Col3",stretch="1")
        self.scrolledtreeview_tickets.column("Col3",anchor="w")
        self.scrolledtreeview_tickets.heading("Col4",text="fine")
        self.scrolledtreeview_tickets.heading("Col4",anchor="center")
        self.scrolledtreeview_tickets.column("Col4",width="39")
        self.scrolledtreeview_tickets.column("Col4",minwidth="20")
        self.scrolledtreeview_tickets.column("Col4",stretch="1")
        self.scrolledtreeview_tickets.column("Col4",anchor="w")
        self.scrolledtreeview_tickets.heading("Col5",text="rno")
        self.scrolledtreeview_tickets.heading("Col5",anchor="center")
        self.scrolledtreeview_tickets.column("Col5",width="38")
        self.scrolledtreeview_tickets.column("Col5",minwidth="20")
        self.scrolledtreeview_tickets.column("Col5",stretch="1")
        self.scrolledtreeview_tickets.column("Col5",anchor="w")
        self.scrolledtreeview_tickets.heading("Col6",text="make")
        self.scrolledtreeview_tickets.heading("Col6",anchor="center")
        self.scrolledtreeview_tickets.column("Col6",width="151")
        self.scrolledtreeview_tickets.column("Col6",minwidth="20")
        self.scrolledtreeview_tickets.column("Col6",stretch="1")
        self.scrolledtreeview_tickets.column("Col6",anchor="w")
        self.scrolledtreeview_tickets.heading("Col7",text="model")
        self.scrolledtreeview_tickets.heading("Col7",anchor="center")
        self.scrolledtreeview_tickets.column("Col7",width="150")
        self.scrolledtreeview_tickets.column("Col7",minwidth="20")
        self.scrolledtreeview_tickets.column("Col7",stretch="1")
        self.scrolledtreeview_tickets.column("Col7",anchor="w")

        self.button_more = tk.Button(top)
        self.button_more.place(relx=0.897, rely=0.922, height=28, width=49)
        self.button_more.configure(activebackground="#ececec")
        self.button_more.configure(activeforeground="#000000")
        self.button_more.configure(background="#d9d9d9")
        self.button_more.configure(command=form_get_a_driver_abstract_support.button_more_click)
        self.button_more.configure(disabledforeground="#a3a3a3")
        self.button_more.configure(foreground="#000000")
        self.button_more.configure(highlightbackground="#d9d9d9")
        self.button_more.configure(highlightcolor="black")
        self.button_more.configure(pady="0")
        self.button_more.configure(state='disabled')
        self.button_more.configure(text='''More''')

        self.button_show = tk.Button(top)
        self.button_show.place(relx=0.798, rely=0.922, height=28, width=49)
        self.button_show.configure(activebackground="#ececec")
        self.button_show.configure(activeforeground="#000000")
        self.button_show.configure(background="#d9d9d9")
        self.button_show.configure(command=form_get_a_driver_abstract_support.button_show_click)
        self.button_show.configure(disabledforeground="#a3a3a3")
        self.button_show.configure(foreground="#000000")
        self.button_show.configure(highlightbackground="#d9d9d9")
        self.button_show.configure(highlightcolor="black")
        self.button_show.configure(pady="0")
        self.button_show.configure(state='disabled')
        self.button_show.configure(text='''Show''')

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