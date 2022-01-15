#import modules
import os
from http.server import BaseHTTPRequestHandler
from routes.main import routes
from pathlib import Path #gets the path of files redirected to

from response.templateHandler import TemplateHandler
from response.badRequestHandler import BadRequestHandler

# holds the methods that handles the server request and responses
class Server(BaseHTTPRequestHandler):
	def do_HEAD(self):
		return
	def do_POST(self):
		return
	def do_GET(self):
		split_path = os.path.splitext(self.path)
		request_extension = split_path[1]

		if request_extension == "" or request_extension == ".html":
			if self.path in routes:
				handler = TemplateHandler()
				handler.find(routes[self.path])

			else:
				handler = BadRequestHandler()

		else:
			handler = BadRequestHandler()

		self.respond({'handler': handler})
	
	#sends http handlers and returns content
	def handle_http(self, handler):
		status_code = handler.getStatus()

		self.send_response(status_code)

		if status_code == 200:
			content = handler.getContents()
			self.send_header('Content-type', handler.getContentType())

		else:
			content = "404 not found"

		self.end_headers()

		return bytes(content, 'UTF-8')

	def respond(self, opts):
		response = self.handle_http(opts['handler'])
		self.wfile.write(response)

