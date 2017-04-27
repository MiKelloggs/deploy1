import os
import psycopg2
import psycopg2.extras
import urllib.parse

class GlassDB:

    def __init__(self):
        urllib.parse.uses_netloc.append("postgres")
        url = urllib.parse.urlparse(os.environ["http://mkorologos.com/3200/Deploy/glass.db"])


        self.connection = psycopg2.connect("http://mkorologos.com/3200/Deploy/glass.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        return

    def __del__(self):
        self.connection.close()
        return

    def getGlass(self):
        self.cursor.execute("SELECT * FROM glassdb")
        return self.cursor.fetchall()

    def createGlass(self, messages):
        self.cursor.execute("INSERT INTO glassdb (yearstart, yearend, make, model, partnumber, location, cost, stock) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (messages[0], messages[1], messages[2], messages[3], messages[4], messages[5], messages[6], messages[7]))
        self.connection.commit()
        return

    def modifyGlass(self, messages):
        self.cursor.execute("DELETE FROM glassdb WHERE partnumber = ?",  (messages[4],))
        self.cursor.execute("INSERT INTO glassdb (yearstart, yearend, make, model, partnumber, location, cost, stock) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (messages[0], messages[1], messages[2], messages[3], messages[4], messages[5], messages[6], messages[7]))
        self.connection.commit()
        return

    def deleteGlass(self, data):
        self.cursor.execute("DELETE FROM glassdb WHERE partnumber = ?",  (data,))
        self.connection.commit()
        return

    def createGlassTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS glassdb (id SERIAL PRIMARY KEY, yearstart INTEGER, yearend INTEGER, make VARCHAR(255), model VARCHAR(255), partnumber VARCHAR(255), location VARCHAR(255), cost INTEGER, stock INTEGER)")
        self.connection.commit()

        
