import sys
import tkinter as tk
import form_login_support
import variables

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    if sys.argv[1:2] == []:
        print('LOG: Database path not passed in, will using ./miniproject1.db')
    else:
        print('LOG: Database path passed in:', sys.argv[1:2][0])
        variables.path = sys.argv[1:2][0]
    root = tk.Tk()
    top = form_login (root)
    form_login_support.init(root, top)
    root.mainloop()

w = None
def create_form_login(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = form_login (w)
    form_login_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_form_login():
    global w
    w.destroy()
    w = None

class form_login:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("310x280+500+500")
        top.title("Login")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.img_banner = tk.PhotoImage(file = 'banner.gif')
        self.label_banner = tk.Label(top, image=self.img_banner)
        self.label_banner.place(relx=0.02, rely=0.01, height=72, width=300)
        self.label_banner.configure(activebackground="#f9f9f9")
        self.label_banner.configure(activeforeground="black")
        self.label_banner.configure(background="#d9d9d9")
        self.label_banner.configure(disabledforeground="#a3a3a3")
        self.label_banner.configure(foreground="#000000")
        self.label_banner.configure(highlightbackground="#d9d9d9")
        self.label_banner.configure(highlightcolor="black")
        

        self.entry_userid = tk.Entry(top)
        self.entry_userid.place(relx=0.4, rely=0.444, height=17, relwidth=0.48)

        self.entry_userid.configure(background="white")
        self.entry_userid.configure(disabledforeground="#a3a3a3")
        self.entry_userid.configure(font="TkFixedFont")
        self.entry_userid.configure(foreground="#000000")
        self.entry_userid.configure(highlightbackground="#d9d9d9")
        self.entry_userid.configure(highlightcolor="black")
        self.entry_userid.configure(insertbackground="black")
        self.entry_userid.configure(selectbackground="#c4c4c4")
        self.entry_userid.configure(selectforeground="black")

        self.label_userid = tk.Label(top)
        self.label_userid.place(relx=0.133, rely=0.444, height=23, width=77)
        self.label_userid.configure(activebackground="#f9f9f9")
        self.label_userid.configure(activeforeground="black")
        self.label_userid.configure(background="#d9d9d9")
        self.label_userid.configure(disabledforeground="#a3a3a3")
        self.label_userid.configure(foreground="#000000")
        self.label_userid.configure(highlightbackground="#d9d9d9")
        self.label_userid.configure(highlightcolor="black")
        self.label_userid.configure(text='''Userid:''')

        self.entry_password = tk.Entry(top)
        self.entry_password.place(relx=0.4, rely=0.593, height=17, relwidth=0.48)

        self.entry_password.configure(background="white")
        self.entry_password.configure(disabledforeground="#a3a3a3")
        self.entry_password.configure(font="TkFixedFont")
        self.entry_password.configure(foreground="#000000")
        self.entry_password.configure(highlightbackground="#d9d9d9")
        self.entry_password.configure(highlightcolor="black")
        self.entry_password.configure(insertbackground="black")
        self.entry_password.configure(selectbackground="#c4c4c4")
        self.entry_password.configure(selectforeground="black")
        self.entry_password.configure(show="*")

        self.label_password = tk.Label(top)
        self.label_password.place(relx=0.15, rely=0.593, height=23, width=65)
        self.label_password.configure(activebackground="#f9f9f9")
        self.label_password.configure(activeforeground="black")
        self.label_password.configure(background="#d9d9d9")
        self.label_password.configure(disabledforeground="#a3a3a3")
        self.label_password.configure(foreground="#000000")
        self.label_password.configure(highlightbackground="#d9d9d9")
        self.label_password.configure(highlightcolor="black")
        self.label_password.configure(text='''Password:''')

        self.button_login = tk.Button(top)
        self.button_login.place(relx=0.733, rely=0.778, height=28, width=43)
        self.button_login.configure(activebackground="#ececec")
        self.button_login.configure(activeforeground="#000000")
        self.button_login.configure(background="#d9d9d9")
        self.button_login.configure(command=form_login_support.button_login_click)
        self.button_login.configure(disabledforeground="#a3a3a3")
        self.button_login.configure(foreground="#000000")
        self.button_login.configure(highlightbackground="#d9d9d9")
        self.button_login.configure(highlightcolor="black")
        self.button_login.configure(pady="0")
        self.button_login.configure(text='''Login''')

if __name__ == '__main__':
    vp_start_gui()
