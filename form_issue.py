import sys
import tkinter as tk
import form_issue_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = form_issue (root)
    form_issue_support.init(root, top)
    root.mainloop()

w = None
def create_form_issue(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = form_issue (w)
    form_issue_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_form_issue():
    global w
    w.destroy()
    w = None

class form_issue:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("470x352+500+500")
        top.title("Officer - Issue a ticket")
        top.configure(background="#d9d9d9")

        self.label_regno = tk.Label(top)
        self.label_regno.place(relx=0.043, rely=0.028, height=23, width=44)
        self.label_regno.configure(background="#d9d9d9")
        self.label_regno.configure(disabledforeground="#a3a3a3")
        self.label_regno.configure(foreground="#000000")
        self.label_regno.configure(text='''regno:''')

        self.label_fname = tk.Label(top)
        self.label_fname.place(relx=0.043, rely=0.114, height=23, width=45)
        self.label_fname.configure(background="#d9d9d9")
        self.label_fname.configure(disabledforeground="#a3a3a3")
        self.label_fname.configure(foreground="#000000")
        self.label_fname.configure(text='''fname:''')

        self.label_lname = tk.Label(top)
        self.label_lname.place(relx=0.043, rely=0.199, height=23, width=44)
        self.label_lname.configure(background="#d9d9d9")
        self.label_lname.configure(disabledforeground="#a3a3a3")
        self.label_lname.configure(foreground="#000000")
        self.label_lname.configure(text='''lname:''')

        self.label_make = tk.Label(top)
        self.label_make.place(relx=0.043, rely=0.284, height=23, width=41)
        self.label_make.configure(background="#d9d9d9")
        self.label_make.configure(disabledforeground="#a3a3a3")
        self.label_make.configure(foreground="#000000")
        self.label_make.configure(text='''make:''')

        self.label_model = tk.Label(top)
        self.label_model.place(relx=0.043, rely=0.369, height=23, width=46)
        self.label_model.configure(background="#d9d9d9")
        self.label_model.configure(disabledforeground="#a3a3a3")
        self.label_model.configure(foreground="#000000")
        self.label_model.configure(text='''model:''')

        self.label_year = tk.Label(top)
        self.label_year.place(relx=0.043, rely=0.455, height=23, width=34)
        self.label_year.configure(background="#d9d9d9")
        self.label_year.configure(disabledforeground="#a3a3a3")
        self.label_year.configure(foreground="#000000")
        self.label_year.configure(text='''year:''')

        self.label_color = tk.Label(top)
        self.label_color.place(relx=0.043, rely=0.54, height=23, width=39)
        self.label_color.configure(background="#d9d9d9")
        self.label_color.configure(disabledforeground="#a3a3a3")
        self.label_color.configure(foreground="#000000")
        self.label_color.configure(text='''color:''')

        self.entry_fname = tk.Entry(top)
        self.entry_fname.place(relx=0.138, rely=0.114, height=17, relwidth=0.796)

        self.entry_fname.configure(background="white")
        self.entry_fname.configure(disabledforeground="#a3a3a3")
        self.entry_fname.configure(font="TkFixedFont")
        self.entry_fname.configure(foreground="#000000")
        self.entry_fname.configure(insertbackground="black")
        self.entry_fname.configure(state='readonly')

        self.entry_lname = tk.Entry(top)
        self.entry_lname.place(relx=0.138, rely=0.199, height=17, relwidth=0.796)

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

        self.entry_make = tk.Entry(top)
        self.entry_make.place(relx=0.138, rely=0.284,height=17, relwidth=0.796)
        self.entry_make.configure(background="white")
        self.entry_make.configure(disabledforeground="#a3a3a3")
        self.entry_make.configure(font="TkFixedFont")
        self.entry_make.configure(foreground="#000000")
        self.entry_make.configure(highlightbackground="#d9d9d9")
        self.entry_make.configure(highlightcolor="black")
        self.entry_make.configure(insertbackground="black")
        self.entry_make.configure(selectbackground="#c4c4c4")
        self.entry_make.configure(selectforeground="black")
        self.entry_make.configure(state='readonly')

        self.entry_model = tk.Entry(top)
        self.entry_model.place(relx=0.138, rely=0.369, height=17, relwidth=0.796)

        self.entry_model.configure(background="white")
        self.entry_model.configure(disabledforeground="#a3a3a3")
        self.entry_model.configure(font="TkFixedFont")
        self.entry_model.configure(foreground="#000000")
        self.entry_model.configure(highlightbackground="#d9d9d9")
        self.entry_model.configure(highlightcolor="black")
        self.entry_model.configure(insertbackground="black")
        self.entry_model.configure(selectbackground="#c4c4c4")
        self.entry_model.configure(selectforeground="black")
        self.entry_model.configure(state='readonly')

        self.entry_year = tk.Entry(top)
        self.entry_year.place(relx=0.138, rely=0.455,height=17, relwidth=0.796)
        self.entry_year.configure(background="white")
        self.entry_year.configure(disabledforeground="#a3a3a3")
        self.entry_year.configure(font="TkFixedFont")
        self.entry_year.configure(foreground="#000000")
        self.entry_year.configure(highlightbackground="#d9d9d9")
        self.entry_year.configure(highlightcolor="black")
        self.entry_year.configure(insertbackground="black")
        self.entry_year.configure(selectbackground="#c4c4c4")
        self.entry_year.configure(selectforeground="black")
        self.entry_year.configure(state='readonly')

        self.entry_color = tk.Entry(top)
        self.entry_color.place(relx=0.138, rely=0.54,height=17, relwidth=0.796)
        self.entry_color.configure(background="white")
        self.entry_color.configure(disabledforeground="#a3a3a3")
        self.entry_color.configure(font="TkFixedFont")
        self.entry_color.configure(foreground="#000000")
        self.entry_color.configure(highlightbackground="#d9d9d9")
        self.entry_color.configure(highlightcolor="black")
        self.entry_color.configure(insertbackground="black")
        self.entry_color.configure(selectbackground="#c4c4c4")
        self.entry_color.configure(selectforeground="black")
        self.entry_color.configure(state='readonly')

        self.entry_regno = tk.Entry(top)
        self.entry_regno.place(relx=0.138, rely=0.028, height=17, relwidth=0.796)

        self.entry_regno.configure(background="white")
        self.entry_regno.configure(disabledforeground="#a3a3a3")
        self.entry_regno.configure(font="TkFixedFont")
        self.entry_regno.configure(foreground="#000000")
        self.entry_regno.configure(highlightbackground="#d9d9d9")
        self.entry_regno.configure(highlightcolor="black")
        self.entry_regno.configure(insertbackground="black")
        self.entry_regno.configure(selectbackground="#c4c4c4")
        self.entry_regno.configure(selectforeground="black")

        self.label_vdate = tk.Label(top)
        self.label_vdate.place(relx=0.043, rely=0.625, height=23, width=39)
        self.label_vdate.configure(activebackground="#f9f9f9")
        self.label_vdate.configure(activeforeground="black")
        self.label_vdate.configure(background="#d9d9d9")
        self.label_vdate.configure(disabledforeground="#a3a3a3")
        self.label_vdate.configure(foreground="#000000")
        self.label_vdate.configure(highlightbackground="#d9d9d9")
        self.label_vdate.configure(highlightcolor="black")
        self.label_vdate.configure(text='''vdate:''')

        self.label_violation = tk.Label(top)
        self.label_violation.place(relx=0.0, rely=0.71, height=23, width=60)
        self.label_violation.configure(activebackground="#f9f9f9")
        self.label_violation.configure(activeforeground="black")
        self.label_violation.configure(background="#d9d9d9")
        self.label_violation.configure(disabledforeground="#a3a3a3")
        self.label_violation.configure(foreground="#000000")
        self.label_violation.configure(highlightbackground="#d9d9d9")
        self.label_violation.configure(highlightcolor="black")
        self.label_violation.configure(text='''violation:''')

        self.label_fine = tk.Label(top)
        self.label_fine.place(relx=0.043, rely=0.795, height=23, width=39)
        self.label_fine.configure(activebackground="#f9f9f9")
        self.label_fine.configure(activeforeground="black")
        self.label_fine.configure(background="#d9d9d9")
        self.label_fine.configure(disabledforeground="#a3a3a3")
        self.label_fine.configure(foreground="#000000")
        self.label_fine.configure(highlightbackground="#d9d9d9")
        self.label_fine.configure(highlightcolor="black")
        self.label_fine.configure(text='''fine:''')

        self.entry_vdate = tk.Entry(top)
        self.entry_vdate.place(relx=0.138, rely=0.625, height=17, relwidth=0.796)

        self.entry_vdate.configure(background="white")
        self.entry_vdate.configure(disabledforeground="#a3a3a3")
        self.entry_vdate.configure(font="TkFixedFont")
        self.entry_vdate.configure(foreground="#000000")
        self.entry_vdate.configure(highlightbackground="#d9d9d9")
        self.entry_vdate.configure(highlightcolor="black")
        self.entry_vdate.configure(insertbackground="black")
        self.entry_vdate.configure(selectbackground="#c4c4c4")
        self.entry_vdate.configure(selectforeground="black")
        self.entry_vdate.configure(state='readonly')

        self.entry_violation = tk.Entry(top)
        self.entry_violation.place(relx=0.138, rely=0.71, height=17
                , relwidth=0.796)
        self.entry_violation.configure(background="white")
        self.entry_violation.configure(disabledforeground="#a3a3a3")
        self.entry_violation.configure(font="TkFixedFont")
        self.entry_violation.configure(foreground="#000000")
        self.entry_violation.configure(highlightbackground="#d9d9d9")
        self.entry_violation.configure(highlightcolor="black")
        self.entry_violation.configure(insertbackground="black")
        self.entry_violation.configure(selectbackground="#c4c4c4")
        self.entry_violation.configure(selectforeground="black")
        self.entry_violation.configure(state='readonly')

        self.entry_fine = tk.Entry(top)
        self.entry_fine.place(relx=0.138, rely=0.795,height=17, relwidth=0.796)
        self.entry_fine.configure(background="white")
        self.entry_fine.configure(disabledforeground="#a3a3a3")
        self.entry_fine.configure(font="TkFixedFont")
        self.entry_fine.configure(foreground="#000000")
        self.entry_fine.configure(highlightbackground="#d9d9d9")
        self.entry_fine.configure(highlightcolor="black")
        self.entry_fine.configure(insertbackground="black")
        self.entry_fine.configure(selectbackground="#c4c4c4")
        self.entry_fine.configure(selectforeground="black")
        self.entry_fine.configure(state='readonly')

        self.button_check = tk.Button(top)
        self.button_check.place(relx=0.702, rely=0.881, height=28, width=46)
        self.button_check.configure(activebackground="#ececec")
        self.button_check.configure(activeforeground="#000000")
        self.button_check.configure(background="#d9d9d9")
        self.button_check.configure(command=form_issue_support.button_check_click)
        self.button_check.configure(disabledforeground="#a3a3a3")
        self.button_check.configure(foreground="#000000")
        self.button_check.configure(highlightbackground="#d9d9d9")
        self.button_check.configure(highlightcolor="black")
        self.button_check.configure(pady="0")
        self.button_check.configure(text='''Check''')

        self.button_issue = tk.Button(top)
        self.button_issue.place(relx=0.83, rely=0.881, height=28, width=41)
        self.button_issue.configure(activebackground="#ececec")
        self.button_issue.configure(activeforeground="#000000")
        self.button_issue.configure(background="#d9d9d9")
        self.button_issue.configure(command=form_issue_support.button_issue_click)
        self.button_issue.configure(disabledforeground="#a3a3a3")
        self.button_issue.configure(foreground="#000000")
        self.button_issue.configure(highlightbackground="#d9d9d9")
        self.button_issue.configure(highlightcolor="black")
        self.button_issue.configure(pady="0")
        self.button_issue.configure(state='disabled')
        self.button_issue.configure(text='''Issue''')

if __name__ == '__main__':
    vp_start_gui()