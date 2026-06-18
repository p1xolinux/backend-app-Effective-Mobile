from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!")

if __name__ == '__main__':
    # 0.0.0.0 — иначе nginx из другого контейнера не достучится
    server = HTTPServer(('0.0.0.0', 8080), RequestHandler)
    print("server up on 8080")
    server.serve_forever()