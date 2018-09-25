import time
import BaseHTTPServer, cgi
from os import curdir, sep

HOST_NAME = ''
PORT_NUMBER = 8000

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def make_testing(slef):
                f= open("testing.html","w+")
                f.write("<!DOCTYPE html>")
                f.write("<html>")
                f.write("<body>")
                f.write("<h1>This is a test creation page</h1>")
                f.write("</body>")
                f.write("</html>")
                f.close()
                return
        
	# handler for GET requests
	def do_GET(self):
		if self.path == "/" or self.path == "/send" or self.path == "/mainmenu.html?":
			self.path = "/mainmenu.html"

		if self.path == "/pupload.html?":
			self.path = "/pupload.html"	
		if self.path == "/demo4.html?":
			self.path = "/demo4.html"
                if self.path == "/htmltext.html?":
			self.path = "/htmltext.html"
                if self.path == "/inputform.html?":
			self.path = "/inputform.html"
		if self.path == "/createPermissions.html?":
			self.path = "/createPermissions.html"
                if self.path == "/testing.html?":
                        self.make_testing()
			self.path = "/testing.html"
		
		try:
			sendReply = False
			if self.path.endswith(".html"):
				mimetype = "text/html"
				sendReply = True

			if sendReply:
				f = open(curdir + sep + self.path)
				self.send_response(200)
				self.send_header("Content-type", mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
				self.wfile.write("</body></html>")
			return

		except IOError:
			self.send_error(404, "File not found: %s" % self.path)

	# handler for POST requests
	def do_POST(self):
		global led_state, LEDPIN
		print "In do_POST()"
		if self.path == "/send":
			self.path = "/"
			form = cgi.FieldStorage(
				fp = self.rfile,
				headers = self.headers,
				environ = {"REQUEST_METHOD":"POST",
					"CONTENT_TYPE":self.headers["Content-Type"],
			})

			if form["command"].value == "LED":
                                print "LED was pushed"
                                self.path = "/pupload.html"
                                self.do_GET()
			elif form["command"].value == "Blink":
                                print "Blink was pushed"
                                self.path = "/mainmenu.html"
                                self.do_GET()
			
			return


def  main():
	
	try:
		server = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
		print "Started httpserver on port ", PORT_NUMBER

		server.serve_forever()

	except KeyboardInterrupt:
		print "^C received, shutting down web server"
		server.socket.close()

if __name__ == "__main__":
	main()
