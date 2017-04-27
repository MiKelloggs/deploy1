import os
import psycopg2
import psycopg2.extras
import urllib.parse

class GlassDB:
		
	def __init__(self):
		urllib.parse.uses_netloc.append("postgres")
		url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
		
		self.connection = psycopg2.connect(
			cursor_factory = psycopg2.extras.RealDictCursor,
			database = url.path[1:],
			user = url.username,
			password = url.password,
			host = url.hostname,
			port = url.port
        )
		self.cursor = self.connection.cursor()
		
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