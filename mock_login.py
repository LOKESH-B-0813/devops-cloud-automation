from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class MockLoginHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        fields = urllib.parse.parse_qs(post_data)
        username = fields.get('user', [''])[0]
        password = fields.get('pass', [''])[0]

        if username == 'blunt_theory' and password == 'LOKESH@2007':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Login Successful!")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Login failed")

server = HTTPServer(('127.0.0.1', 8080), MockLoginHandler)
print("Mock server running on http://127.0.0.1:8080...")
server.serve_forever()
