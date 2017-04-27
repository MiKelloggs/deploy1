from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
import sys
from glass_db import GlassDB

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
                    self.handle404()

        def handle404(self):
            self.send_response(404)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-type", "text/html")#name of header and value
            self.end_headers()
            self.wfile.write(bytes("<strong>Not Found</strong>", "utf-8")) #dont write just a string, http doesnt understand ordinary strings.
		
def main():
	db = GlassDB()
	db.createGlassTable()
	db = None # disconnect
	
	port = 8080
	if len(sys.argv) > 1:
		port = int(sys.argv[1])
	
	listen = ("0.0.0.0", port)
	server = HTTPServer(listen, httpServerRequsetHandler)
		
	print("Server listening on", "{}:{}".format(*listen))
	server.serve_forever()
	
if __name__ == "__main__":
	main()