from http.server import BaseHTTPRequestHandler, HTTPServer, CGIHTTPRequestHandler

import os

server = HTTPServer(("", 8888), CGIHTTPRequestHandler)

print ("Der Server horcht unter http://localhost:8888")
print("TEST")
server.serve_forever()
