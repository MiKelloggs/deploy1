import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
import os
import psycopg2
import psycopg2.extras
import urllib.parse

fw = open('database.txt', 'w')
fw.write("testing 1i23")
fw.close()




class httpServerRequsetHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            if self.path == "/windshields":

                db = GlassDB()
                rows = db.getGlass()
                json_string = json.dumps(rows)

                print("JSON:", json_string)


                print(json.dumps(rows))

                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, HEAD, OPTIONS")
                self.send_header("Access-Control-Allow_Headers", "X-Requested-With")
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes(json_string, "utf-8"))
                return
            else:
                self.handle404()
                print("Oops, the page you are looking for is not here.")

        def do_OPTIONS(self):
            self.send_response(200, "ok")
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, DELETE, PUT, HEAD')
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.end_headers()
            return


        def do_DELETE(self):
                if self.path == "/windshields":
                    length = self.headers['Content-Length']
                    length = int(length)

                    body = self.rfile.read(length).decode("utf-8")
                    data = parse_qs(body)

                    message = data['message'][0]
                    print(message)

                    db = GlassDB()
                    db.deleteGlass(message)


                    self.send_response(200)
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, HEAD, OPTIONS")
                    self.send_header("Access-Control-Allow_Headers", "X-Requested-With")
                    self.send_header("Content-type", "application/x-www-form-urlencoded")
                    self.end_headers()
                    return
                else:
                    self.handle404()
                    print("Oops, the page you are looking for is not here.")

        def do_POST(self):
                if self.path == "/windshields":
                    length = self.headers['Content-Length']
                    length = int(length)

                    body = self.rfile.read(length).decode("utf-8")
                    data = parse_qs(body)

                    message = data['message'][0]
                    messages = message.split()
                    print(messages, message)

                    db = GlassDB()
                    create = db.createGlass(messages)


                    self.send_response(201)
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, HEAD, OPTIONS")
                    self.send_header("Access-Control-Allow_Headers", "X-Requested-With")
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                else:
                    self.handle404()


        def do_PUT(self):
                if self.path == "/windshields":
                    length = self.headers['Content-Length']
                    length = int(length)

                    body = self.rfile.read(length).decode("utf-8")
                    data = parse_qs(body)

                    message = data['message'][0]
                    messages = message.split()
                    print(messages, message)

                    db = GlassDB()
                    create = db.modifyGlass(messages)


                    self.send_response(201)
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, HEAD, OPTIONS")
                    self.send_header("Access-Control-Allow_Headers", "X-Requested-With")
                    self.send_header("Content-type", "application/x-www-form-urlencoded")
                    self.end_headers()
                else:
                    self.handle404();

        def handle404(self):
            self.send_response(404)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-type", "text/html")#name of header and value
            self.end_headers()
            self.wfile.write(bytes("<strong>Not Found</strong>", "utf-8")) #dont write just a string, http doesnt understand ordinary strings.



class GlassDB:

    def __init__(self):
        urllib.parse.uses_netloc.append("postgres")
        url = urllib.parse.urlparse(os.environ["DATABASE_URL"])


        self.connection.row_factory = dict_factory


        self.connection = psycopg2.connect(
            cursor_factory=psycopg2.extras.RealDictCursor,
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
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

    def createGlassTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS glassdb (id SERIAL PRIMARY KEY, yearstart INTEGER, yearend INTEGER, make VARCHAR(255), model VARCHAR(255), partnumber VARCHAR(255), location VARCHAR(255), cost INTEGER, stock INTEGER)")
        self.connection.commit()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def main():
    db = GlassDB()
    db.createGlassTable()
    rows = db.getGlass()
    print(json.dumps(rows))

    port = 8080
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    listen = ("0.0.0.0", port)
    server = HTTPServer(listen, httpServerRequsetHandler)

    print("Listening...")
    server.serve_forever()




if __name__ == "__main__":
    main()