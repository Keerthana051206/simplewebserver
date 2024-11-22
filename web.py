6-50542-AAOEM</li>

<li><b>System type</b>	64-bit operating system, x64-based processor</li>

<li><b><u>Pen and touch</b></u>	No pen or touch input is available for this display</li>
</ol>
</body>
</html>



"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<h1> Laptop Cofiguration(KEERTHANA-24002514) </h1>
<body>
<ol>
<li><b>Device name</b>	Keerthana

<li><b>Processor	11th Gen Intel(R) Core(TM) i5-1155G7 @ 2.50GHz   2.50 GHz

<li><b>Installed RAM</b>	16.0 GB (15.8 GB usable)</li>

<li><b>Device ID	79E946DE-3B2E-490D-B9E6-F53A013D9FB1</li>

<li><b>Product ID</b>	00342-4259