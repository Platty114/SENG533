from http.server import BaseHTTPRequestHandler, HTTPServer
import random

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def factorial(self):
        
        #generate a random number between 1 and 100
        factor = random.randint(1,100)
        factor_temp = factor
        factorial = 1
        #now calculate factorial
        while(factor > 0):
            factorial = factorial * factor
            factor -= 1

        return factor_temp, factorial

    def do_GET(self):
        # Set response status code
        self.send_response(200)
        
        # Set headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        factor, factorial = self.factorial()

        # Response body
        message = f"<html><body><h1>The factorial for {factor} is {factorial} </h1></body></html>"
        self.wfile.write(message.encode('utf-8'))

def run():
    print("Starting factorial server!")
    server_port = 8080
    handler = SimpleHTTPRequestHandler 
    address = ('', server_port)
    http_server = HTTPServer(address, handler)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        http_server.server_close()

if __name__ == '__main__':
    run()

