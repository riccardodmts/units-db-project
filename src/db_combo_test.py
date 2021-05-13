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

    combo.remove_all()

    for item in lista:
        
        combo.add_option(item, command = lambda : change_second(combo, combo2, con))

def change_second(combo1, combo2, con):

    key = int(combo1.get_selected())

    result = con._execute_pstmt("SELECT productCode FROM orderDetails WHERE orderNumber = %s", (key, ))
    combo2.remove_all()

    for item in result:
        
        combo2.add_option(item[0], command = lambda : print(f"{item[0]}"))


if __name__ == "__main__":

    con = MyConnection()

    root = tk.Tk()
    result = con._execute_pstmt("SELECT orderNumber FROM orders", None)

    lista = []
    
    for item in result:

        lista.append(item[0])

   
    first = MyComboBox(root, ["prima", "prima 2"], root)
    second = MyComboBox(root, ["prima", "seoncda"], root)
 
    first.grid(row = 0, column = 0)
    second.grid(row = 0, column = 1)

    root.after(5000, lambda : change(lista, first, second, con))
    root.mainloop()

    

    
