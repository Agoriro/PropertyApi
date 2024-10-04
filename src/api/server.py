from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, property_handler=None, **kwargs):
        self.property_handler = property_handler
        super().__init__(*args, **kwargs)

    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/properties':
            query_params = parse_qs(parsed_path.query)
            response_data, status_code = self.property_handler.handle_get_properties(query_params)
            
            self.send_response(status_code)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

def create_server(host: str, port: int, property_handler) -> HTTPServer:
    def handler(*args):
        RequestHandler(*args, property_handler=property_handler)
    
    server = HTTPServer((host, port), handler)
    return server