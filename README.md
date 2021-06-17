# DB project (university project)

## Table of contents

* [Introduction](#introduction)
* [Technologies](#technologies)
* [Contents description](#contents-description)
* [Setup](#setup)

## Introduction

The aim of this project is to develop a database for the MotoGP. Moreover, it was realised a simple Python application that allows to visualize the rank of every single Gran Prix and the statistics of a driver during the entire championship. The GUI is created using tkinter, while the graphs are realisized with matplotlib.

## Technologies

The project is created using:

* OS: Windows 10
* MySQL server version: 8.0.25
* conda version: 4.8.5
* Python version: 3.7.4

For the specific versions of Python modules, check the section [Setup](#setup) 
## Contents description

A brief description of the directories and the files.

* **ERD** In this directory you may find two files: logic_d.vuerd.json, the .json file used to realise the logic diagram for the database using the VS Code extension **ERD Editor**, and the settings.json, the .json file for the settings of the VS Code extension **ERD Editor**.
*  **motogp_units.sql** In order to have some data and use the stored procedures (used in the python application), you may import this .sql file.
*  **conda_env.txt** You may use this file to generate the same conda virtual enviroment (with the right versions of the python modules) used to realize the python application.
* **src** In this directory you may find many python modules used to realized the simple application.

## Setup

You may follow these steps:

1. Import the SQL file motogp_units.sql in your MySQL server. You can use the following command (you have to create an empty database before)
```
mysql -u username -p database_name -R < motogp_units.sql
```
2. In order to create the conda virtual enviroment, use
```
conda create --name name_env --file conda_env.txt
```
3. Activate the virtual enviroment ```conda activate name_env```
4. In the python module main_module.py (at the end of the file) you may find the following lines of code
```Python
if __name__ == "__main__":

    con = MyConnection(db = "db_name", user = "user_name", passwd = "psw", host = "localhost")
    root = MainPage(con)
    
    root.mainloop()

    con.close()

```
Change ```"db_name"```, ```"user_name"``` and ```"psw"``` with the right parameters.

You can start the application (```python main_module.py```).
