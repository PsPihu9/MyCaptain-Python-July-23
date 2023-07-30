'''
@author: Prashansa Shah 
@description: Functions in Python
'''

import sqlite3

def connect(dbname):

    connect = sqlite3.connect(dbname)
    connect.execute("CREATE TABLE IF NOT EXISTS HOTELS_MUMBAI(NAME, ADDRESS, PRICE, RATINGS, AMENITIES)")
    print("table created!")

    connect.close()

def insert_into_table(dbname, values):

    connect = sqlite3.connect(dbname)
    connect.execute("INSERT INTO TABLE HOTELS_MUMBAI VALUES(?,?,?,?,?)", values)
    
    connect.commit()
    connect.close()

def get_table_data(dbname):

    connect = sqlite3.connect(dbname)    
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM HOTELS_MUMBAI")
    table_records = cursor.fetchall()

    for record in table_records:
        print(record)
    
    connect.close()

