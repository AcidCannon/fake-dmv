import sys
import tkinter as tk
import tkinter.messagebox as msgBox
import variables
import functions

def button_login_click():
    # establish connection and get cursor
    variables.connection, variables.cursor = functions.connect(variables.path)
    # remove starting and trailing space
    userid = w.entry_userid.get().strip()
    password = w.entry_password.get().strip()
    # using extra regular expression to dectect password validity to prevent SQL injection
    if(functions.login_check(userid, password)):
        variables.cursor.execute('SELECT * FROM users WHERE uid = ? collate nocase AND pwd = ?;', (userid, password))
        try:
            # if no result, which means wrong userid or password
            fetched = variables.cursor.fetchall()[0]
            utype = fetched[2]
            variables.user_city = fetched[-1]
            print('LOG:', 'operator city:', variables.user_city)
        except:
            # do not give correct utype
            utype = ''
    else:
        # reject SQL injection
        utype = ''
    if utype == 'o' or utype == 'O':
        # officer interface
        destroy_window()
        import form_officer
        form_officer.vp_start_gui()
    elif utype == 'a' or utype == 'A':
        # agent interface
        destroy_window()
        import form_agent
        form_agent.vp_start_gui()
    else:
        # login failed
        msgBox.showerror("Access Denied","You userid/password is not valid! Please try again!")

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import form_login
    form_login.vp_start_gui()