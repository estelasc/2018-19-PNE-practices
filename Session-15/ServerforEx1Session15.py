import http.server
import socketserver
import termcolor

PORT = 2000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # -- Printing the request line
        reqpath = self.path
        termcolor.cprint(reqpath, 'blue')

        if reqpath.startswith('/echo?msg='):
            resp = reqpath[10:]
            f = open('responseforex1form.html', 'r')
            contents = f.read()
            contents = contents.replace('##', resp).replace('+', ' ')
        elif reqpath == '/' or reqpath == '/echo':
            f = open("formforex1.html", 'r')
            contents = f.read()
        else:
            f = open('error.html', 'r')
            contents = f.read()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))

        return


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT:  {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")
