import tkinter as tk
import matplotlib as mpl
import mysql.connector as mysql
import datetime
import numpy as np

class MyConnection():

    def __init__(self, * args, **kwargs):

        self.settings = {

            "user" : "root",
            "host" : "localhost",
            "passwd" : "Aprilia21units",
            "db" : "classicmodels"

        }

        for key in self.settings:

            if key in kwargs:

                self.settings[key] = kwargs.pop(key)

        self.cnx = mysql.connect(
            
            host = self.settings["host"],
            user = self.settings["user"],
            passwd = self.settings["passwd"],
            database = self.settings["db"]
        )

        self.cursor = self.cnx.cursor()


    def _execute_pstmt(self, stmt, params):

        if params is not None:
            self.cursor.execute(stmt, params)

        else:

            self.cursor.execute(stmt)

        return self.cursor.fetchall()


    def close(self):

        self.cnx.close()



    def get_gran_prix_ranking(self, anno, cat, nome):

        self.cursor.callproc('sp_get_gran_prix_ranking', args =  (anno, cat, nome))

        for result in self.cursor.stored_results():

            res = result.fetchall()

        return res

    def get_championship_ranking(self, anno, cat):

        self.cursor.callproc('sp_get_championship_ranking', args =  (anno, cat))

        for result in self.cursor.stored_results():

            res = result.fetchall()

        return res


    def get_championship_manufacturer_ranking(self, anno, cat):

        self.cursor.callproc('sp_get_championship_manufacturer_ranking', args =  (anno, cat))

        for result in self.cursor.stored_results():

            res = result.fetchall()

        return res
    
    def get_drivers_list(self, anno, cat):

        self.cursor.callproc('sp_get_drivers_list_from_championship', args =  (anno, cat))

        for result in self.cursor.stored_results():

            res = result.fetchall()

        return res


    def get_driver_results(self, anno, cat, nome, cognome):


        self.cursor.callproc('sp_get_driver_results', args =  (anno, cat, nome, cognome))

        for result in self.cursor.stored_results():

            res = result.fetchall()

        return res

    def get_number_podiums(self, anno, cat, nome, cognome):

        self.cursor.callproc('sp_get_number_podiums', args =  (anno, cat, nome, cognome))

        for result in self.cursor.stored_results():

            res = result.fetchall()

        return res

    def get_number_victories(self, anno, cat, nome, cognome):

        self.cursor.callproc('sp_get_number_victories', args =  (anno, cat, nome, cognome))

        for result in self.cursor.stored_results():

            res = result.fetchall()

        return res
    
    def get_number_na(self, anno, cat, nome, cognome):

        self.cursor.callproc('sp_get_number_na', args =  (anno, cat, nome, cognome))

        for result in self.cursor.stored_results():

            res = result.fetchall()

        return res


    def get_leader(self, anno, cat):


        self.cursor.callproc('sp_get_leader', args =  (anno, cat))

        for result in self.cursor.stored_results():

            res = result.fetchall()

        return res


        


#test di connessione
if __name__ == "__main__":

    conn = MyConnection()

    results = conn._execute_pstmt("SELECT paymentDate FROM payments", None)

    for date in results:

        #print(date[0], '\n')
        d = np.datetime64(date[0])
        print(d," ", date[0].year)

    conn.close()