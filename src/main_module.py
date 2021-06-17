from os import close
from table_widget import Table
import tkinter as tk
import matplotlib as mpl
import mysql.connector as mysql
import datetime as dt
from graph_widget import SwitchingFrame, MyPlot
from combo_widget import MyComboBox
from db_module import MyConnection
from vertical_bar_widget import VerticalBar



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
        self.stat_driver = False

        for item in result:

            self.rank_combo.add_option(f"{item[0]}", command = lambda : self.create_rank_popup())
            self.rank_costr_combo1.add_option(f"{item[0]}", command = lambda : self.create_rank_cost_popup())
            self.rank_race_combo1.add_option(f"{item[0]}", command = lambda : self.fill_race_combo2())
            self.stat_driver_combo1.add_option(f"{item[0]}", command = lambda : self.fill_stat_combo2())

    def fill_stat_combo2(self):

        key1, key2 = (self.stat_driver_combo1.get_selected()).split()

        res = self.conn.get_drivers_list(key2, key1)

        self.stat_driver_combo2.remove_all()

        for item in res:

            self.stat_driver_combo2.add_option(f"{item[0]}", command = lambda : self.create_stat_driver_popup())


    def close_stat_driver_popup(self, popup):

        self.stat_driver = False
        popup.destroy()

    def order_stat_results_1(self, input):

        result = []

        for item in input:

            temp = []
            temp.append(item[0])
            temp.append(item[1])
            temp.append(item[2])
            temp.append(item[3])

            result.append(temp)

        return result

    def order_stat_results_2(self, input):

        result = []

        for item in input:

            temp = []
            temp.append(str(item[0]))
            temp.append(item[1])

            if item[2] is None:
                temp.append("NA")
            else:
                temp.append(item[2])
                    
            temp.append(item[3])

            result.append(temp)

        return result

    def check_data(self, x_leader, y_leader, x_other, y_other):

        new_y_other = None
        new_y_leader = None

        if len(x_leader) == len(x_other):
            x = x_leader
            return x, y_leader, y_other
        
        else:

            if len(x_leader) > len(x_other):

                new_y_other = []
                c = 0
                for item in x_leader:

                    if item == x_other[c]:

                        new_y_other.append(y_other[c])
                        c+=1
                    else:

                        new_y_other.append(0)

                return x_leader, y_leader, new_y_other







    def data_for_graph(self, input):

        x = []
        y = []

        for item in input:

            x.append(item[0])
            y.append(item[3])

        return [x, y]


    def create_stat_driver_popup(self):

        if not self.stat_driver:

            self.stat_driver = True

            #data pilota
            key1, key2 = (self.stat_driver_combo1.get_selected()).split()
            num, nome, cognome = (self.stat_driver_combo2.get_selected()).split()
            #------------------------------------------------


            res = self.conn.get_driver_results(key2, key1, nome, cognome)
            res_1 = self.order_stat_results_1(res)
            res_2 = self.order_stat_results_2(res)

            #data leader
            leader = self.conn.get_leader(key2, key1)
            nome_leader, cogn_leader = leader[0]
            #----------------------------------
            

            res_leader = self.conn.get_driver_results(key2, key1, nome_leader, cogn_leader)
            res_leader = self.order_stat_results_1(res_leader)

            #print(res_leader)

            x, y_leader = self.data_for_graph(res_leader)

            self.stat_popup = tk.Toplevel(bg = dark_grey)
            self.stat_popup.title(f"Statistiche pilota: {self.stat_driver_combo2.get_selected()}")
            self.stat_popup.protocol("WM_DELETE_WINDOW", lambda : self.close_stat_driver_popup(self.stat_popup))
            tabs = SwitchingFrame(self.stat_popup, bg_color = dark_grey, unselected_color = grey_1)
            frame = tabs.get_master()

            data_graph_x, data_graph_y = self.data_for_graph(res_1)
            #print(data_graph_x, data_graph_y)

            tab1 = tk.Frame(frame, bg = dark_grey)
            tab1.grid_columnconfigure(0, weight = 3)
            tab1.grid_columnconfigure(1, weight = 1)
            tab1.grid_rowconfigure(0, weight = 0)

            table = Table(tab1, res_2, labels = ["Data", "Nome GP", "Posizione", "Punti"])
            table.grid(row = 0, column = 1, sticky = "nswe")

            data_graph_x, y_leader, data_graph_y = self.check_data(x, y_leader, data_graph_x, data_graph_y)

            graph = MyPlot(tab1, data_graph_x, [data_graph_y, y_leader], [f"{self.stat_driver_combo2.get_selected()}", f"{nome_leader} {cogn_leader}"], date = "date", bg_color = dark_blue)
            tabs.add_tab("Grafico", tab1)
            graph.grid(row = 0, column = 0, sticky = "nswe")


            num_podi = ((self.conn.get_number_podiums(key2, key1, nome, cognome))[0])[0]
            num_podi_leader = ((self.conn.get_number_podiums(key2, key1, nome_leader, cogn_leader))[0])[0]

            
            num_v = ((self.conn.get_number_victories(key2, key1, nome, cognome))[0])[0]
            num_v_leader = ((self.conn.get_number_victories(key2, key1, nome_leader, cogn_leader))[0])[0]

            num_na = ((self.conn.get_number_na(key2, key1, nome, cognome))[0])[0]
            num_na_leader = ((self.conn.get_number_na(key2, key1, nome_leader, cogn_leader))[0])[0]

            max_podi = max([num_podi, num_podi_leader])
            if max_podi == 0:
                max_podi = 1
            max_v = max([num_v, num_v_leader])
            if max_v == 0:
                max_v = 1
            max_na = max([num_na, num_na_leader])

            if max_na == 0:
                max_na =1


            bar_frame = tk.Frame(frame, bg = dark_grey)

            bar_frame.grid_columnconfigure(0, weight = 1)
            bar_frame.grid_columnconfigure(1, weight = 1)
            bar_frame.grid_columnconfigure(2, weight = 1)
            bar_frame.grid_rowconfigure(0, weight = 0)
            bar_frame.grid_rowconfigure(1, weight = 1)

            label1 = tk.Label(bar_frame, text = "Podi", foreground = "white", bg = dark_grey)
            label1.grid(row = 0, column = 0)

            frame_bar_1 = tk.Frame(bar_frame, bg = dark_grey)
            frame_bar_1.grid_columnconfigure(0, weight = 1)
            frame_bar_1.grid_columnconfigure(1, weight = 1)
            frame_bar_1.grid_rowconfigure(0, weight = 1)

            bar1_1 = VerticalBar(frame_bar_1, 0, max_podi, width = 30, height = 150)
            bar1_1.update_bar(num_podi)
            bar1_1.grid(row = 0, column = 0)


            bar1_2 = VerticalBar(frame_bar_1, 0, max_podi, width = 30, height = 150, bar_color = "#ff6600")
            bar1_2.update_bar(num_podi_leader)
            bar1_2.grid(row = 0, column = 1)

            frame_bar_1.grid(row = 1, column = 0)

            label2 = tk.Label(bar_frame, text = "Vittorie", foreground = "white", bg = dark_grey)
            label2.grid(row = 0, column = 1)

            frame_bar_2 = tk.Frame(bar_frame, bg = dark_grey)
            frame_bar_2.grid_columnconfigure(0, weight = 1)
            frame_bar_2.grid_columnconfigure(1, weight = 1)
            frame_bar_2.grid_rowconfigure(0, weight = 1)

            bar2_1 = VerticalBar(frame_bar_2, 0, max_v, width = 30, height = 150)
            bar2_1.update_bar(num_v)
            bar2_1.grid(row = 0, column = 0)

            

            bar2_2 = VerticalBar(frame_bar_2, 0, max_v, width = 30, height = 150, bar_color = "#ff6600")
            bar2_2.update_bar(num_v_leader)
            bar2_2.grid(row = 0, column = 1)

            frame_bar_2.grid(row = 1, column = 1)

            label3 = tk.Label(bar_frame, text = "NA", foreground = "white", bg = dark_grey)
            label3.grid(row = 0, column = 2)

            frame_bar_3 = tk.Frame(bar_frame, bg = dark_grey)
            frame_bar_3.grid_columnconfigure(0, weight = 1)
            frame_bar_3.grid_columnconfigure(1, weight = 1)
            frame_bar_3.grid_rowconfigure(0, weight = 1)

            bar3_1 = VerticalBar(frame_bar_3, 0, max_na, width = 30, height = 150)
            bar3_1.update_bar(num_na)
            bar3_1.grid(row = 0, column = 0)


            bar3_2 = VerticalBar(frame_bar_3, 0, max_na, width = 30, height = 150, bar_color = "#ff6600")
            bar3_2.update_bar(num_na_leader)
            bar3_2.grid(row = 0, column = 1)

            frame_bar_3.grid(row = 1, column = 2)
            tabs.add_tab("Altre stat", bar_frame)

            
            tabs.pack(fill = tk.BOTH, expand = True)



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
                temp.append("NA")
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
            
            self.ch_popup.title(f"Classifica campionato: {input}")

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

            self.ch_cost_popup.title(f"Classifica costruttori. Campionato: {self.rank_costr_combo1.get_selected()}")
            self.ch_cost_popup.protocol("WM_DELETE_WINDOW", lambda : self.close_ch_cost_popup(self.ch_cost_popup))


            frame = Table(self.ch_cost_popup, res, labels = ["Posizione", "Casa costruttrice", "Punti"])
            frame.pack(fill = tk.BOTH, expand = True)




if __name__ == "__main__":

    con = MyConnection(db = "motogp_units", user =  "root", passwd = "psw", host = "localhost")
    root = MainPage(con)
    
    root.mainloop()

    con.close()


    



    

    

