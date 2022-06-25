import sys
import tkinter as tk
import form_officer_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = form_officer (root)
    form_officer_support.init(root, top)
    root.mainloop()

w = None
def create_form_officer(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = form_officer (w)
    form_officer_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_form_officer():
    global w
    w.destroy()
    w = None

class form_officer:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font12 = "-family {Microsoft YaHei UI} -size 20 -weight normal"  \
            " -slant roman -underline 0 -overstrike 0"

        top.geometry("300x80+500+500")
        top.title("Traffic officer")
        top.configure(background="#d9d9d9")

        self.label_officer = tk.Label(top)
        self.label_officer.place(relx=0.01, rely=0.01, height=41, width=229)
        self.label_officer.configure(background="#d9d9d9")
        self.label_officer.configure(disabledforeground="#a3a3a3")
        self.label_officer.configure(font=font12)
        self.label_officer.configure(foreground="#000000")
        self.label_officer.configure(text='''Welcome, officer.''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                foreground="#000000",
                label="Start")
        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=form_officer_support.logout,
                foreground="#000000",
                label="Logout")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=form_officer_support.issue_a_ticket,
                foreground="#000000",
                label="Issue a ticket")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=form_officer_support.find_a_car_owner,
                foreground="#000000",
                label="Find a car owner")

if __name__ == '__main__':
    vp_start_gui()