#!/usr/bin/python3


import http.server
import json

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """ sfds f df """


    def do_GET(self):
        if self.path == "/":
            self.handle_root()
        elif self.path == "/data":
            self.handle_data()
        elif self.path == "/status":
            self.handle_status()
        else:
            self.handle_not_found()

    def handle_root(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def handle_data(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        self.wfile.write(json.dumps(data).encode())

    def handle_status(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"OK")

    def handle_not_found(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Endpoint not found")

def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
