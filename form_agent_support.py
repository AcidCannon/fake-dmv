import sys
import sqlite3
import variables

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

def get_a_driver_abstract():
    import form_get_a_driver_abstract
    form_get_a_driver_abstract.vp_start_gui()
    
def process_a_bill_of_sale():
    import form_process_a_bill_of_sale
    form_process_a_bill_of_sale.vp_start_gui()

def process_a_payment():
    import form_process_a_payment
    form_process_a_payment.vp_start_gui()

def register_a_birth():
    import form_register_a_birth
    form_register_a_birth.vp_start_gui()

def register_a_marriage():
    import form_register_a_marriage
    form_register_a_marriage.vp_start_gui()

def renew_a_vehicle_registration():
    import form_renew_a_vehicle_registration
    form_renew_a_vehicle_registration.vp_start_gui()

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
    import form_agent
    form_agent.vp_start_gui()