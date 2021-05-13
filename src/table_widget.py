import matplotlib as mpl
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import matplotlib.dates as mdates
import datetime

dark_grey = "#212121"
dark_blue="#102A43"
blue_1="#243B53"
grey_1="#424242"


class Table(tk.Frame):

    def __init__(self, parent, matrix, *args, **kwargs):

        self.rows = len(matrix)
        self.columns = None
        self.col_idx = None

        self.current_row = 0

        self.colors = {

            "bg_color"          : grey_1,
            "space_color"       : dark_grey,
            "text_color"        : "white"
        }

        if "labels" in kwargs:

            self.columns = len(kwargs["labels"])
            self.col_idx = kwargs.pop("labels")
        
        else:

            self.columns = len(matrix[0])
            
        for key in self.colors:

            if key in kwargs:
                self.colors[key] = kwargs.pop(key)
        
        

        tk.Frame.__init__(self, parent, *args, **kwargs)

        self._widgets_matrix = []

        self.master_frame = tk.Frame(self, bg = self.colors["bg_color"])

        if self.col_idx is not None:

            self._create_idx()

        self._create_table(matrix)
        
        self.master_frame.pack(fill = tk.BOTH, expand = True)

        
    def _create_idx(self):

        first_row = []
        second_row = []
        column = 0

        for item in self.col_idx:

            frame = tk.Frame(self.master_frame, bg = self.colors["space_color"], pady = 5)

            #frame2 = tk.Frame(self.master_frame, bg = self.colors["bg_color"], height = 10)
            #frame2.grid(row = 1, column = column, sticky = "ew")

            label = tk.Label(frame, bg = self.colors["bg_color"], fg = self.colors["text_color"], text = item, anchor = "w")

            label.pack(fill = tk.BOTH, expand = True)

            frame.grid(row = 0, column = column, sticky = "nswe")
            tupla = (frame, label)

            self.master_frame.grid_columnconfigure(column, weight = 1)

            first_row.append(tupla)
            #second_row.append(frame2)

            column+=1

        self._widgets_matrix.append(first_row)
        #self._widgets_matrix.append(second_row)

        self.current_row = 1


    def _create_table(self, matrix):

        for item in matrix:

            col = 0

            row = []

            for el in item:

                frame = tk.Frame(self.master_frame, bg = self.colors["space_color"], pady = 1)

                label = tk.Label(frame, bg = self.colors["bg_color"], fg = self.colors["text_color"], text = f"{el}", anchor = "w")

                label.pack(fill = tk.BOTH, expand = True)

                frame.grid(row = self.current_row, column = col, sticky = "nswe")
                tupla = (frame, label)

                if self.current_row == 0:

                    self.master_frame.grid_columnconfigure(col, weight = 1)

                row.append(tupla)
                col+=1

            self._widgets_matrix.append(row)
            self.current_row +=1




if __name__ == "__main__":

    lista = ["prima", "seconda", "terza"]

    root = tk.Tk()

    frame = Table(root, [[1,2,3], [4, 5, datetime.date(1999,10,26)], [7, "ciao", 25]], labels = lista)

    frame.pack(fill = tk.BOTH, expand = True)

    root.mainloop()





