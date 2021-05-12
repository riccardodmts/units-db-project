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

class MyComboBox(tk.Frame):


    def __init__(self, parent, values, root, *args, **kwargs):

        self._selected = None

        self.root_p = root


        self.colors = {

            "text_color"    : "white",
            "bg_color"      : dark_blue,
            "over_color"    : blue_1
        }


        for key in self.colors:

            if key in kwargs:

                self.colors[key] = kwargs.pop(key)

        kwargs["bg"] = self.colors["bg_color"]

        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.frame = tk.Frame(self, bg = self.colors["bg_color"])

        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_columnconfigure(1, weight = 0)
        self.frame.grid_rowconfigure(0, weight = 1)

        initial_width = self._find_width(values)

        self.label_sel = tk.Label(
            self.frame,
            fg = self.colors["text_color"],
            bg = self.colors["bg_color"],
            width = initial_width,
            text = values[0]
        )

        self.label_sel.grid(row = 0, column = 0)

        self.button = tk.Menubutton(
            self.frame,
            text = "˅",
            bg = self.colors["bg_color"],
            fg = self.colors["text_color"],
            activebackground = self.colors["over_color"],
            activeforeground = self.colors["text_color"]
        )

        self.button.bind("<Button-1>", lambda e : self._show_popup(e))

        self.button.grid(row = 0, column = 1)

        self.frame.pack(side = tk.LEFT)

        self._popup_on = False
        self.popup = None


        self.labels = dict()
        
        for item in values:

            self.labels[item] = dict()
        
        
    def remove_all(self):

        del self.labels
        self.labels = dict()
        self.label_sel.config(text = " ")

    def _show_popup(self, event):

        if self._popup_on is not True:

            self._popup_on = True

            x, y, height = self.frame.winfo_rootx(), self.frame.winfo_rooty(), self.frame.winfo_height()

            self.popup = tk.Toplevel(self.frame, bg = self.colors["bg_color"])
            self.popup.overrideredirect(True)

            self.popup.geometry('+{}+{}'.format(x, y + height))


            for item in self.labels:

                self._add_option(item, **self.labels[item])
            
            self.button.bind("<Button-1>", lambda e : self._destroy_popup())

            self.root_p.bind("<Configure>", lambda e : self._destroy_popup())

      
    def add_option(self, text, **kwargs):

        self.labels[text] = kwargs

        length = self._find_width(self.labels)

        self.label_sel.config(width = length) 
   
    def _add_option(self, text, **kwargs):

        func = kwargs.pop("command", None)

        mb = tk.Menubutton(
            self.popup,
            text = f"{text}",
            bg = self.colors["bg_color"],
            fg = self.colors["text_color"],
            activebackground = self.colors["over_color"],
            activeforeground = self.colors["text_color"]

        )

        mb._command = func
        mb.bind("<Button-1>", lambda e : self._on_select(e, text))
        mb.grid(sticky = "ew")

    

    def _on_select(self, event, text):

        self._select(text)

        w = event.widget

        if w._command is not None:

            w._command()
        
        self._change_option_selected(text)


    def _change_option_selected(self, key):

        self.label_sel.config(text = key)
        self._destroy_popup()



    def _destroy_popup(self):

        if self._popup_on :

            self.popup.destroy()
            self.button.bind("<Button-1>", lambda e : self._show_popup(e))
            self._popup_on = False


    def _find_width(self, lista):
            length = 0

            for item in lista:

                if len(f"{item}") > length:

                    length = len(f"{item}")
            
            return length

    def _select(self, text):

        self._selected = text
    
    def get_selected(self):

        return self._selected

if __name__ == "__main__":

    root = tk.Tk()

    prova = MyComboBox(root, ["prima", "pr"], root)
    prova.add_option("terza", command = lambda : print(prova.get_selected()))
    prova.add_option("quarta molto lunga lunga", command = lambda : print(prova.get_selected()))

    prova.pack()

    root.mainloop()