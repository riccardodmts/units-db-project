import tkinter as tk
import matplotlib as mpl
import mysql.connector as mysql
import datetime as dt
from combo_widget import MyComboBox

dark_grey = "#212121"
dark_blue="#102A43"
blue_1="#243B53"
grey_1="#424242"
fill = "#057FA4"
title_font = ("Helvetica", 12, "bold")


if __name__ == "__main__":

    root = tk.Tk()
    root.grid_columnconfigure(0, weight = 1)

    root.grid_rowconfigure(0, weight = 0)
    root.grid_rowconfigure(1, weight = 1)
    root.grid_rowconfigure(2, weight = 0)
    root.grid_rowconfigure(3, weight = 1)
    root.grid_rowconfigure(4, weight = 0)
    root.grid_rowconfigure(5, weight = 1)
    root.grid_rowconfigure(6, weight = 0)
    root.grid_rowconfigure(7, weight = 1)

    frame_label_1 = tk.Frame(root, bg = dark_grey)
    label1 = tk.Label(frame_label_1, bg = dark_grey, fg = "white", text = "Classifica campionato:", font = title_font)

    label1.pack(side = tk.LEFT)
    frame_label_1.grid(row = 0, column = 0, sticky = "we")

    frame1 = tk.Frame(root, bg = dark_blue)
    frame1.grid_columnconfigure(0, weight = 1, uniform= "g1")
    frame1.grid_columnconfigure(1, weight = 1, uniform = "g1")
    frame1.grid_rowconfigure(0, weight = 1)

    frame_left1 = tk.Frame(frame1, bg = dark_grey)
    frame_right1 = tk.Frame(frame1, bg = dark_grey)

    frame_left1.grid(row = 0, column = 0, sticky = "nswe")
    frame_right1.grid(row = 0, column = 1, sticky = "nsew")


    rank_combo = MyComboBox(frame_left1, ["prova", "prova2"], root)
    rank_combo.pack(anchor = tk.CENTER, expand = True)

    frame1.grid(row = 1, column = 0, sticky = "nswe")

    frame_label_2 = tk.Frame(root, bg = dark_grey)
    label2 = tk.Label(frame_label_2, bg = dark_grey, fg = "white", text = "Classifica gara:", font = title_font)

    label2.pack(side = tk.LEFT)
    frame_label_2.grid(row = 2, column = 0, sticky = "we")

    frame2 = tk.Frame(root, bg = dark_blue)
    frame2.grid_columnconfigure(0, weight = 1, uniform= "g1")
    frame2.grid_columnconfigure(1, weight = 1, uniform = "g1")
    frame2.grid_rowconfigure(0, weight = 1)

    frame_left2 = tk.Frame(frame2, bg = dark_grey)
    frame_right2 = tk.Frame(frame2, bg = dark_grey)

    frame_left2.grid(row = 0, column = 0, sticky = "nswe")
    frame_right2.grid(row = 0, column = 1, sticky = "nsew")


    rank_race_combo1 = MyComboBox(frame_left2, ["prova", "prova2"], root)
    rank_race_combo1.pack(anchor = tk.CENTER, expand = True)

    rank_race_combo2 = MyComboBox(frame_right2, ["prova3", "prova4"], root)
    rank_race_combo2.pack(anchor = tk.CENTER, expand = True)

    frame2.grid(row = 3, column = 0, sticky = "nswe")

    frame_label_3 = tk.Frame(root, bg = dark_grey)
    label3 = tk.Label(frame_label_3, bg = dark_grey, fg = "white", text = "Classifica costruttori:", font = title_font)

    label3.pack(side = tk.LEFT)
    frame_label_3.grid(row = 4, column = 0, sticky = "we")

    frame3 = tk.Frame(root, bg = dark_blue)
    frame3.grid_columnconfigure(0, weight = 1, uniform= "g1")
    frame3.grid_columnconfigure(1, weight = 1, uniform = "g1")
    frame3.grid_rowconfigure(0, weight = 1)

    frame_left3 = tk.Frame(frame3, bg = dark_grey)
    frame_right3 = tk.Frame(frame3, bg = dark_grey)

    frame_left3.grid(row = 0, column = 0, sticky = "nswe")
    frame_right3.grid(row = 0, column = 1, sticky = "nsew")


    rank_costr_combo1 = MyComboBox(frame_left3, ["prova", "prova2"], root)
    rank_costr_combo1.pack(anchor = tk.CENTER, expand = True)

    rank_costr_combo2 = MyComboBox(frame_right3, ["prova3", "prova4"], root)
    rank_costr_combo2.pack(anchor = tk.CENTER, expand = True)

    frame3.grid(row = 5, column = 0, sticky = "nswe")

    frame_label_4 = tk.Frame(root, bg = dark_grey)
    label4 = tk.Label(frame_label_4, bg = dark_grey, fg = "white", text = "Classifica costruttori:", font = title_font)

    label4.pack(side = tk.LEFT)
    frame_label_4.grid(row = 6, column = 0, sticky = "we")

    frame4 = tk.Frame(root, bg = dark_blue)
    frame4.grid_columnconfigure(0, weight = 1, uniform= "g1")
    frame4.grid_columnconfigure(1, weight = 1, uniform = "g1")
    frame4.grid_rowconfigure(0, weight = 1)

    frame_left4 = tk.Frame(frame4, bg = dark_grey)
    frame_right4 = tk.Frame(frame4, bg = dark_grey)

    frame_left4.grid(row = 0, column = 0, sticky = "nswe")
    frame_right4.grid(row = 0, column = 1, sticky = "nsew")


    stat_driver_combo1 = MyComboBox(frame_left4, ["prova", "prova2"], root)
    stat_driver_combo1.pack(anchor = tk.CENTER, expand = True)

    stat_driver_combo2 = MyComboBox(frame_right4, ["prova3", "prova4"], root)
    stat_driver_combo2.pack(anchor = tk.CENTER, expand = True)

    frame4.grid(row = 7, column = 0, sticky = "nswe")



    root.geometry("350x350")
    root.mainloop()


    



    

    

