from http.server import SimpleHTTPRequestHandler, HTTPServer
import random

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/change_color':
            # Generate a random color
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(color.encode())
        else:
            super().do_GET()

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()