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
fill = "#057FA4"


class VerticalBar(tk.Frame):

    def __init__(self, parent, min_value, max_value, *args, **kwargs):


        self.settings = {

            "width"     :   30,
            "height"    :  100,
            "unit"      :   ""

        }

        self.colors = {
            "bg_color"      : dark_grey,
            "bar_color"     : fill,
            "vbar_color"    : grey_1,
            "text_color"    : "white"
        }


        self.value = min_value

        self.min = min_value
        self.max = max_value

        for key in self.settings:

            if key in kwargs:

                self.settings[key] = kwargs.pop(key)
        
        for key in self.colors:

            if key in kwargs:

                self.colors[key] = kwargs.pop(key)


        
        self.width = self.settings["width"]
        self.height = self.settings["height"] 



        kwargs["bg"] = self.colors["bg_color"]

        tk.Frame.__init__(self, parent, *args, **kwargs)



        self.canvas = tk.Canvas(self, bg = self.colors["bg_color"],
                                height = self.height, width = self.width,
                                bd=0,
                                highlightthickness=0
                                )

        self.label = tk.Label(
            self, bg = self.colors["bg_color"],
            fg = self.colors["text_color"],
            text = "{}{}".format(self.min, self.settings["unit"])
            )

        self.vbar = self.canvas.create_rectangle  (0, 0, self.width, self.height,
                                                     fill = self.colors["vbar_color"])

        self.bar = self.canvas.create_rectangle(
            0, self.height - 1,
            self.width, self.height,
            fill = self.colors["bar_color"]
        )

        self.canvas.grid(row = 0, column = 0, sticky = "nswe")
        self.label.grid(row = 1, column = 0, sticky = "we")
    
    def _calculate_bar_height(self, value):

        diff = self.max - self.min

        result = self.height - (((value - self.min)* self.height)/diff)

        return result
    
    def update_bar(self, value):

        x0, y0, x1, y1 = self.canvas.coords(self.bar)

        y0 = self._calculate_bar_height(value)

        self.canvas.coords(self.bar, x0, y0, x1, y1)

        text = f"{value}"

        self.label.configure(text = text)



def example_update(bar):

    bar.update_bar(10)

if __name__ == "__main__":

    root = tk.Tk()

    bar = VerticalBar(root, 0, 20, width = 50, height = 200)

    bar.pack(fill = tk.Y)

    root.after(2000, lambda : example_update(bar))

    root.mainloop()