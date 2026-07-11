import os
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", 8080))
NAME = os.getenv("NAME", "David Shlomo Zim")

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(f"Hello from Docker! {NAME}s app is running!!!!!!!.\n".encode())

if __name__ == "__main__":
    print("Server starting on " + HOST + ":" + str(PORT))
    HTTPServer((HOST, PORT), SimpleHandler).serve_forever()
    