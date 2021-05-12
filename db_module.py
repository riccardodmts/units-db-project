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
            "passwd" : "...",
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


#test di connessione
if __name__ == "__main__":

    conn = MyConnection()

    results = conn._execute_pstmt("SELECT paymentDate FROM payments", None)

    for date in results:

        #print(date[0], '\n')
        d = np.datetime64(date[0])
        print(d," ", date[0].year)

    conn.close()