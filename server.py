#import modules
from http.server import BaseHTTPRequestHandler
from routes.main import routes
from pathlib import Path #gets the path of files redirected to

# holds the methods that handles the server request and responses
class Server(BaseHTTPRequestHandler):
	def do_HEAD(self):
		return
	def do_POST(self):
		return
	def do_GET(self):
		self.respond()
	
	#sends http handlers and returns content
	def handle_http(self):
		status = 200
		content_type = "text/plain"
		response_content = ""

		if self.path in routes:
			print(routes[self.path])
			route_content = routes[self.path]['template']
			filepath = Path("templates/{}".format(route_content))
			
			if filepath.is_file():
				content_type = "text/html"
				response_content = open("templates/{}".format(route_content))
				response_content = response_content.read()
			
			else:
				content_type = "text/plain"
				response_content = "404 Not found"
		
		else:
			content_type = "text/plain"
			response_content = "404 Not found"

		self.send_response(status)
		self.send_header('Content-type', content_type)
		self.end_headers()
		return bytes(response_content, "UTF-8")
	
	#sends out response
	def respond(self):
		content = self.handle_http()
		self.wfile.write(content)
