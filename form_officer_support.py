import sys
import tkinter as tk
import variables

def find_a_car_owner():
    import form_find_a_car_owner
    form_find_a_car_owner.vp_start_gui()

def issue_a_ticket():
    import form_issue
    form_issue.vp_start_gui()

def logout():
    destroy_window()
    import form_login
    form_login.vp_start_gui()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    variables.connection.close()
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import form_officer
    form_officer.vp_start_gui()