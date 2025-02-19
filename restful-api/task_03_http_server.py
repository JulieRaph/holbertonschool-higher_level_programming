#!/usr/bin/python3
"""Develop a simple API using Python with the `http.server` module"""


from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))
        elif self.path == '/status':
            status = ("OK")
            json_status = json.dumps(status)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(json_status.encode("utf-8"))
        elif self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            json_info = json.dumps(info)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(json.info.encode("utf-8"))
        elif self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    host = "localhost"
    port = 8000
    httpd = HTTPServer((host, port), MyRequestHandler)
    print("Starting server on http://localhost:8000")
    httpd.serve_forever()
