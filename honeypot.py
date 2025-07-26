from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

hostName = "localhost"
serverPort = 8080

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"GET request from {self.client_address[0]} for {self.path}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("This is a honeypot server. Your request is logged.", "utf-8"))

    def do_POST(self):
        logging.info(f"POST request from {self.client_address[0]} for {self.path}")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info(f"POST data: {post_data.decode('utf-8')}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("POST received and logged.", "utf-8"))

if __name__ == "__main__":
    logging.basicConfig(filename="honeypot.log", level=logging.INFO)
    server = HTTPServer((hostName, serverPort), MyHandler)
    print(f"[*] Honeypot started at http://{hostName}:{serverPort}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print("[*] Honeypot stopped.")
