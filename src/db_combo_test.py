import matplotlib as mpl
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import matplotlib.dates as mdates
import datetime
from db_module import MyConnection
from combo_widget import MyComboBox

def change(lista, combo, combo2, con):
    call_sp_get_leader(con)
    combo.remove_all()

    for item in lista:
        
        combo.add_option(f"{item[0]} {item[1]}", command = lambda : change_second(combo, combo2, con))

def change_second(combo1, combo2, con):

    str = combo1.get_selected()
    key1, key2 = str.split()
    
    result = con._execute_pstmt("SELECT nome FROM granpremio WHERE anno = %s AND categoria = %s", (key2, key1))
    combo2.remove_all()

    for item in result:
        
        combo2.add_option(item[0], command = lambda d = f"{item[0]}" : print(d))

def call_sp_get_leader(conn):

        '''

        conn.cursor.callproc('sp_get_driver_results', args =  ('2020', 'motogp', 'Valentino', 'Rossi'))

        for result in conn.cursor.stored_results():
            
            res = result.fetchall()
        
        for record in res:
            print(record)
        '''

        for res in conn.get_championship_ranking('2020', 'motogp'):
            
            print(res)

        


if __name__ == "__main__":

    con = MyConnection(db = "motogp_units")

    root = tk.Tk()
    result = con._execute_pstmt("SELECT categoria,anno FROM campionato", None)

    lista = []
    
    for item in result:

        lista.append(item)

   
    first = MyComboBox(root, ["prima", "prima 2"], root)
    second = MyComboBox(root, ["prima", "seoncda"], root)
 
    first.grid(row = 0, column = 0)
    second.grid(row = 0, column = 1)

    root.after(5000, lambda : change(lista, first, second, con))
    root.mainloop()

    

    
