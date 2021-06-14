from os import close
from table_widget import Table
import tkinter as tk
import matplotlib as mpl
import mysql.connector as mysql
import datetime as dt
from combo_widget import MyComboBox
from db_module import MyConnection

dark_grey = "#212121"
dark_blue="#102A43"
blue_1="#243B53"
grey_1="#424242"
fill = "#057FA4"
title_font = ("Helvetica", 12, "bold")


class MainPage(tk.Tk):

    def __init__(self, conn, *args, **kwargs):

        self.conn = conn

        tk.Tk.__init__(self, *args, **kwargs)

        self.grid_columnconfigure(0, weight = 1)

        self.grid_rowconfigure(0, weight = 0)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 0)
        self.grid_rowconfigure(3, weight = 1)
        self.grid_rowconfigure(4, weight = 0)
        self.grid_rowconfigure(5, weight = 1)
        self.grid_rowconfigure(6, weight = 0)
        self.grid_rowconfigure(7, weight = 1)

        self.frame_label_1 = tk.Frame(self, bg = dark_grey)
        self.label1 = tk.Label(self.frame_label_1, bg = dark_grey, fg = "white", text = "Classifica campionato:", font = title_font)

        self.label1.pack(side = tk.LEFT)
        self.frame_label_1.grid(row = 0, column = 0, sticky = "we")

        self.frame1 = tk.Frame(self, bg = dark_blue)
        self.frame1.grid_columnconfigure(0, weight = 1, uniform= "g1")
        self.frame1.grid_columnconfigure(1, weight = 1, uniform = "g1")
        self.frame1.grid_rowconfigure(0, weight = 1)

        self.frame_left1 = tk.Frame(self.frame1, bg = dark_grey)
        self.frame_right1 = tk.Frame(self.frame1, bg = dark_grey)

        self.frame_left1.grid(row = 0, column = 0, sticky = "nswe")
        self.frame_right1.grid(row = 0, column = 1, sticky = "nsew")


        self.rank_combo = MyComboBox(self.frame_left1, ["prova", "prova2"], self)
        self.rank_combo.pack(anchor = tk.CENTER, expand = True)

        self.frame1.grid(row = 1, column = 0, sticky = "nswe")

        self.frame_label_2 = tk.Frame(self, bg = dark_grey)
        self.label2 = tk.Label(self.frame_label_2, bg = dark_grey, fg = "white", text = "Classifica gara:", font = title_font)

        self.label2.pack(side = tk.LEFT)
        self.frame_label_2.grid(row = 2, column = 0, sticky = "we")

        self.frame2 = tk.Frame(self, bg = dark_blue)
        self.frame2.grid_columnconfigure(0, weight = 1, uniform= "g1")
        self.frame2.grid_columnconfigure(1, weight = 1, uniform = "g1")
        self.frame2.grid_rowconfigure(0, weight = 1)

        self.frame_left2 = tk.Frame(self.frame2, bg = dark_grey)
        self.frame_right2 = tk.Frame(self.frame2, bg = dark_grey)

        self.frame_left2.grid(row = 0, column = 0, sticky = "nswe")
        self.frame_right2.grid(row = 0, column = 1, sticky = "nsew")


        self.rank_race_combo1 = MyComboBox(self.frame_left2, ["prova", "prova2"], self)
        self.rank_race_combo1.pack(anchor = tk.CENTER, expand = True)

        self.rank_race_combo2 = MyComboBox(self.frame_right2, ["prova3", "prova4"], self)
        self.rank_race_combo2.pack(anchor = tk.CENTER, expand = True)

        self.frame2.grid(row = 3, column = 0, sticky = "nswe")

        self.frame_label_3 = tk.Frame(self, bg = dark_grey)
        label3 = tk.Label(self.frame_label_3, bg = dark_grey, fg = "white", text = "Classifica costruttori:", font = title_font)

        label3.pack(side = tk.LEFT)
        self.frame_label_3.grid(row = 4, column = 0, sticky = "we")

        self.frame3 = tk.Frame(self, bg = dark_blue)
        self.frame3.grid_columnconfigure(0, weight = 1, uniform= "g1")
        self.frame3.grid_columnconfigure(1, weight = 1, uniform = "g1")
        self.frame3.grid_rowconfigure(0, weight = 1)

        self.frame_left3 = tk.Frame(self.frame3, bg = dark_grey)
        self.frame_right3 = tk.Frame(self.frame3, bg = dark_grey)

        self.frame_left3.grid(row = 0, column = 0, sticky = "nswe")
        self.frame_right3.grid(row = 0, column = 1, sticky = "nsew")


        self.rank_costr_combo1 = MyComboBox(self.frame_left3, ["prova", "prova2"], self)
        self.rank_costr_combo1.pack(anchor = tk.CENTER, expand = True)

        #self.rank_costr_combo2 = MyComboBox(self.frame_right3, ["prova3", "prova4"], self)
        #self.rank_costr_combo2.pack(anchor = tk.CENTER, expand = True)

        self.frame3.grid(row = 5, column = 0, sticky = "nswe")

        self.frame_label_4 = tk.Frame(self, bg = dark_grey)
        self.label4 = tk.Label(self.frame_label_4, bg = dark_grey, fg = "white", text = "Statistiche pilota:", font = title_font)

        self.label4.pack(side = tk.LEFT)
        self.frame_label_4.grid(row = 6, column = 0, sticky = "we")

        self.frame4 = tk.Frame(self, bg = dark_blue)
        self.frame4.grid_columnconfigure(0, weight = 1, uniform= "g1")
        self.frame4.grid_columnconfigure(1, weight = 1, uniform = "g1")
        self.frame4.grid_rowconfigure(0, weight = 1)

        self.frame_left4 = tk.Frame(self.frame4, bg = dark_grey)
        self.frame_right4 = tk.Frame(self.frame4, bg = dark_grey)

        self.frame_left4.grid(row = 0, column = 0, sticky = "nswe")
        self.frame_right4.grid(row = 0, column = 1, sticky = "nsew")


        self.stat_driver_combo1 = MyComboBox(self.frame_left4, ["prova", "prova2"], self)
        self.stat_driver_combo1.pack(anchor = tk.CENTER, expand = True)

        self.stat_driver_combo2 = MyComboBox(self.frame_right4, ["prova3", "prova4"], self)
        self.stat_driver_combo2.pack(anchor = tk.CENTER, expand = True)

        self.frame4.grid(row = 7, column = 0, sticky = "nswe")



        self.geometry("350x350")

        self.set_initial_value()

    def set_initial_value(self):

        result = self.conn._execute_pstmt("SELECT CONCAT(categoria, ' ', anno) FROM campionato", None)
        self.rank_combo.remove_all()
        self.rank_costr_combo1.remove_all()
        self.rank_race_combo1.remove_all()
        self.stat_driver_combo1.remove_all()

        self.rank_popup = False
        self.rank_cost_popup = False
        self.rank_race_popup = False

        for item in result:

            self.rank_combo.add_option(f"{item[0]}", command = lambda : self.create_rank_popup())
            self.rank_costr_combo1.add_option(f"{item[0]}", command = lambda : self.create_rank_cost_popup())
            self.rank_race_combo1.add_option(f"{item[0]}", command = lambda : self.fill_race_combo2())
            self.stat_driver_combo1.add_option(f"{item[0]}")


    def fill_race_combo2(self):

        key1, key2 = (self.rank_race_combo1.get_selected()).split()

        res = self.conn._execute_pstmt("SELECT nome FROM granPremio WHERE anno = %s AND categoria = %s", (key2, key1))
        self.rank_race_combo2.remove_all()

        for item in res:

            self.rank_race_combo2.add_option(f"{item[0]}", command = lambda : self.create_rank_race_popup())

        
        #print(res)
    def close_race_popup(self, popup):

        self.rank_race_popup = False
        popup.destroy()
    

    def create_rank_race_popup(self):

        if not self.rank_race_popup:

            self.rank_race_popup = True

            key3 = self.rank_race_combo2.get_selected()

            key1, key2 = (self.rank_race_combo1.get_selected()).split()

            res = self.conn.get_gran_prix_ranking(key2, key1, key3)
        
            res = self.order_race_rank(res)

            self.r_r_popup = tk.Toplevel(bg = dark_grey)

            self.r_r_popup.title(f"Classifica: {key3} campionato {key1} {key2}")
            self.r_r_popup.protocol("WM_DELETE_WINDOW", lambda : self.close_race_popup(self.r_r_popup))

            frame = Table(self.r_r_popup, res, labels = ["Posizione", "Num", "Pilota", "Punti", "Tempo", "Team", "Moto"])
            frame.pack(fill = tk.BOTH, expand = True)

    def order_race_rank(self, input):

        result = []

        for item in input:

            temp = []
            if item[0] is None:
                temp.append("-")
            else:
                temp.append(item[0])


            temp.append(item[1]) 
            temp.append(item[2]) 
            temp.append(item[3])
            if item[4] is None:
                temp.append("-")
            else:
                temp.append(str(item[4]))
            temp.append(item[5])
            temp.append(item[6])

            result.append(temp)

        return result

    def order_rank(self, input):

        result = []

        for item in input:

            temp = []

            temp.append(int(item[0]))
            temp.append(item[1])
            temp.append(item[2])
            temp.append(int(item[3]))
            temp.append(item[4])
            temp.append(item[5])

            result.append(temp)

        return result


    def close_ch_popup(self, popup):

        self.rank_popup = False
        popup.destroy()

    def create_rank_popup(self):

        input = self.rank_combo.get_selected()
        
        if not self.rank_popup:

            self.rank_popup = True
            key1, key2 = input.split()
            
            res = self.conn.get_championship_ranking(key2, key1)

            res = self.order_rank(res)

            self.ch_popup = tk.Toplevel(bg = dark_grey)
            
            self.ch_popup.title("Classifica campionato")

            self.ch_popup.protocol("WM_DELETE_WINDOW", lambda : self.close_ch_popup(self.ch_popup))
            #print(res)
            frame = Table(self.ch_popup, res, labels = ["Posizione", "Num", "Pilota", "Punti", "Team", "Moto"])
            frame.pack(fill = tk.BOTH, expand = True)

    def close_ch_cost_popup(self, popup):

        
        self.rank_cost_popup = False
        popup.destroy()

    def order_rank_cost(self, input):

        result = []

        for item in input:

            temp = []

            temp.append(int(item[0]))
            temp.append(item[1])
            temp.append(int(item[2]))

            result.append(temp)

        return result


    def create_rank_cost_popup(self):

        if not self.rank_cost_popup:

            self.rank_cost_popup = True

            key1, key2 = (self.rank_costr_combo1.get_selected()).split()
            
            res = self.conn.get_championship_manufacturer_ranking(key2, key1)
            res = self.order_rank_cost(res)

            self.ch_cost_popup = tk.Toplevel(bg = dark_grey)

            self.ch_cost_popup.title("Classifica costruttori")
            self.ch_cost_popup.protocol("WM_DELETE_WINDOW", lambda : self.close_ch_cost_popup(self.ch_cost_popup))


            frame = Table(self.ch_cost_popup, res, labels = ["Posizione", "Casa costruttrice", "Punti"])
            frame.pack(fill = tk.BOTH, expand = True)




if __name__ == "__main__":

    con = MyConnection(db = "motogp_units")
    root = MainPage(con)
    
    root.mainloop()

    con.close()


    



    

    

