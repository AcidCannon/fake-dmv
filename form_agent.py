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

import form_agent_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = form_agent (root)
    form_agent_support.init(root, top)
    root.mainloop()

w = None
def create_form_agent(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = form_agent (w)
    form_agent_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_form_agent():
    global w
    w.destroy()
    w = None

class form_agent:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("300x80+500+500")
        top.title("Registry agent")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.label_agent = tk.Label(top)
        self.label_agent.place(relx=0.033, rely=0.125, height=41, width=222)
        self.label_agent.configure(activebackground="#f9f9f9")
        self.label_agent.configure(activeforeground="black")
        self.label_agent.configure(background="#d9d9d9")
        self.label_agent.configure(disabledforeground="#a3a3a3")
        self.label_agent.configure(font="-family {Microsoft YaHei UI} -size 20")
        self.label_agent.configure(foreground="#000000")
        self.label_agent.configure(highlightbackground="#d9d9d9")
        self.label_agent.configure(highlightcolor="black")
        self.label_agent.configure(text='''Welcome, agent.''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Start")
        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=form_agent_support.logout,
                foreground="#000000",
                label="Logout")
        self.sub_menu1 = tk.Menu(top,tearoff=0)
        self.sub_menu.add_cascade(menu=self.sub_menu1,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                foreground="#000000",
                label="Register")
        self.sub_menu1.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=form_agent_support.register_a_birth,
                foreground="#000000",
                label="Birth")
        self.sub_menu1.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=form_agent_support.register_a_marriage,
                foreground="#000000",
                label="Marriage")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=form_agent_support.renew_a_vehicle_registration,
                foreground="#000000",
                label="Renew a vehicle registration")
        self.sub_menu12 = tk.Menu(top,tearoff=0)
        self.sub_menu.add_cascade(menu=self.sub_menu12,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                foreground="#000000",
                label="Process")
        self.sub_menu12.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=form_agent_support.process_a_bill_of_sale,
                foreground="#000000",
                label="Bill of sale")
        self.sub_menu12.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=form_agent_support.process_a_payment,
                foreground="#000000",
                label="Payment")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=form_agent_support.get_a_driver_abstract,
                foreground="#000000",
                label="Get a driver abstract")

if __name__ == '__main__':
    vp_start_gui()