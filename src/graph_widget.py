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

#CLASSE SwitchingFrame

#parametri obbligatori:
#   -parent: master tkinter

#parametri non obbligatori (passati con kwargs):
#   -bg_color: il colore per lo sfondo. c'è un valore di deafult
#   -text_color: il colore dei testi. c'è un valore di deafult
#   -unselected_color: il colore usato per le voci non selezionate

#due metodi pubblici, per permettere di aggiungere dei tab
#con get_master() si ottiene il master per il tab da aggiungere
#con add_tab(text, tab) si aggiunge il tab. text deve essere una stringa univoca e 
#comparirà come voce nel menu. tab è il widget/frame/... che si vuole aggiungere

class SwitchingFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        
        self.small_frames = dict()
        self.n = 0

        self.colors = {

            "bg_color"          : dark_blue,
            "unselected_color"  : blue_1,
            "text_color"        : "white"
        }

        self.tabs = dict()

        for key in self.colors:

            if key in kwargs:
                
                self.colors[key] = kwargs.pop(key)

    
        tk.Frame.__init__(self, parent, *args, **kwargs)


        self.menu_frame = tk.Frame(self, bg = self.colors["unselected_color"])

        self.menu_buttons = dict()


        self.main_frame = tk.Frame(self, bg = self.colors["bg_color"])

        self.main_frame.grid_columnconfigure(0, weight = 1)
        self.main_frame.grid_rowconfigure(0, weight = 1)

        

        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 0)
        self.grid_rowconfigure(1, weight = 1)

        self.menu_frame.grid(row = 0, column = 0, sticky = "we")
        self.main_frame.grid(row = 1, column = 0, sticky = "wens")

    def add_tab(self, text, tab):
        self.n+=2

        self.small_frames[text] = tk.Frame(self.menu_frame, width = 2, bg = self.colors["text_color"]) 

        self.menu_buttons[text] = tk.Menubutton(self.menu_frame, text = text, 
                                                 bg = self.colors["bg_color"],
                                                 fg = self.colors["text_color"],
                                                 activeforeground = self.colors["text_color"],
                                                 activebackground = self.colors["bg_color"],
                                                 borderwidth = 0
                                                 )
        self.small_frames[text].grid(row = 0, column = self.n-2, sticky = "ns")
        self.menu_buttons[text].grid( row = 0, column = self.n-1)
        self.tabs[text] = tab
        self.tabs[text].grid(row = 0, column = 0, sticky = "nsew", padx = 20, pady = 20)

        self._select_tab(text)

        self.menu_buttons[text].bind("<Button-1>", lambda e : self._select_tab(text))

        

        
                                            
    def _show_frame(self, page_selected):

        self.tabs[page_selected].tkraise() 

    def get_master(self):

        return self.main_frame

    def _select_tab(self, text):

        
        for key in self.menu_buttons:
            self.small_frames[key].config(bg = self.colors["unselected_color"])
            self.menu_buttons[key].config(bg = self.colors["unselected_color"], activebackground = self.colors["unselected_color"])
        
        self.menu_buttons[text].config(bg = self.colors["bg_color"], activebackground = self.colors["bg_color"])
        self.small_frames[text].config(bg = self.colors["text_color"])

        self._show_frame(text)

#---------------------------------------------------------------------------------------------------------------------------------

#CLASSE MyPlot 

#parametri obbligatori:
#   -parent: master tkinter
#   -x: lista elementi su asse x
#   -y: lista con liste. ongi lista associata al dato da mostrare
#   -labels: lista di stringhe. Queste stringhe vengono usate nella legenda

#parametri non obbligatori (passati con kwargs):
#   -bg_color: il colore per lo sfondo. c'è un valore di deafult
#   -text_color: il colore dei testi e degli assi. c'è un valore di deafult
#   -lines_colors: lista con i colori per ogni linea. c'è un valore di deafult
#   -date: se si passa date = "date" si formatteranno le 
#          label sull'asse x in modo adeguato per mostrare un intera data (y-m-d).
#          se si passa date = "Y", per mostare solo l'anno
# 
# OSS: i metodi sono tutti privati (segnati con _) 

class MyPlot(tk.Frame):

    def __init__(self, parent, x, y, labels, *args, **kwargs):

        self.x = x
        self.y = y
        self.labels = labels

        self.fig = Figure()
        self.ax  = self.fig.add_subplot(1,1,1)

        self.settings = {

            "y_ticks" : None,

            "interactive" : False

        }

        self.colors = {

            "bg_color"      : dark_grey,
            "text_color"    : "white",
            "lines_colors"  : ["#E42217", "#4CC552",  "#57FEFF", "#FFE87C", "#153E7E", "#348781"]
        }

        for key in self.colors:

            if key in kwargs:

                self.colors[key] = kwargs.pop(key)


        if "date" in kwargs:

            if kwargs["date"] == "date":
                self._draw_with_entire_dates()
            
            if kwargs["date"] == "Y":

                self._draw_with_years()

            del kwargs["date"]

        else:

            self._draw()

        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.ax.patch.set_facecolor(self.colors["bg_color"])
        self.fig.patch.set_facecolor(self.colors["bg_color"])

        for label in self.ax.xaxis.get_ticklabels():

            label.set_color(self.colors["text_color"])
            

        for label in self.ax.yaxis.get_ticklabels():

            label.set_color(self.colors["text_color"])

        for tick in self.ax.xaxis.get_ticklines():

            tick.set_color(self.colors["text_color"])
            

        for tick in self.ax.yaxis.get_ticklines():

            tick.set_color(self.colors["text_color"])

        self.ax.spines['bottom'].set_color(self.colors["text_color"])
        self.ax.spines['left'].set_color(self.colors["text_color"])

        self.legend = self.ax.legend(
                            bbox_to_anchor = ( 0., 1.0, 1, 0.1 ) , mode = " expand ", loc = 2,
                            borderaxespad = 0., ncol = self.counter
                         )


        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()

        #widget con il canvas
        self.w = self.canvas.get_tk_widget()
        self.w.pack(fill = tk.BOTH, expand = True)

    def _draw(self):

        self.ax.set_xticks(self.x)
        self.ax.set_xlim(min(self.x), max(self.x))

        self.counter = 0

        for data in self.y:
            
            self.ax.plot(self.x, data, self.colors["lines_colors"][self.counter], label = f"{self.labels[self.counter]}")
            self.counter+=1


    def _draw_date(self,x):

        self.ax.set_xticks(x)
        self.ax.set_xlim(min(x), max(x))

        self.counter = 0

        for data in self.y:
            
            self.ax.plot(x, data, self.colors["lines_colors"][self.counter], label = f"{self.labels[self.counter]}")
            self.counter+=1

        self.fig.autofmt_xdate()

    def _draw_with_entire_dates(self):
        
        
        myFmt = mdates.DateFormatter('%Y-%m-%d')
        self.ax.xaxis.set_major_formatter(myFmt)
        
        self._draw_date(self.x)
    
    def _draw_with_years(self):

        myFmt = mdates.DateFormatter('%Y')
        self.ax.xaxis.set_major_formatter(myFmt)
        
        self._draw_date(self.x)
        
        

        

if __name__ == "__main__":

    lista = list()

    lista.append(datetime.date(1999,10,26))
    lista.append(datetime.date(2000, 1, 10))
    lista.append(datetime.date(2001, 1, 10))
    lista.append(datetime.date(2002, 1, 10))
    lista.append(datetime.date(2003, 1, 10))
    lista.append(datetime.date(2004, 1, 10))

    y = list()

    y_first = [1, 2, 1 , 1,1, 1]
    y_second = [4, 1, 2, 1,1, 3]

    y.append(y_first)
    y.append(y_second)

    root = tk.Tk()
    tabs = SwitchingFrame(root, bg_color = dark_grey, unselected_color = grey_1)

    #esempio: 3 grafici (stessi dati) aggiunti ad un tab menu
    frame = tabs.get_master()
    graph = MyPlot(frame, lista, y, ["prova","sec"], date = "Y", bg_color = "black")
    graph2 = MyPlot(frame, lista, y, ["prova","sec"], date = "date", bg_color = "black")
    graph3 = MyPlot(frame, lista, y, ["prova","sec"], date = "date", bg_color = dark_blue)


    tabs.add_tab("Graph", graph)
    tabs.add_tab("Graph_2", graph2)
    tabs.add_tab("Graph_3", graph3)
    tabs.pack(fill = tk.BOTH, expand = True)


    #graph.pack(fill = tk.BOTH, expand = True)

    root.mainloop()