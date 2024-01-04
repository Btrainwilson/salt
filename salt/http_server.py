#!/usr/bin/env python

import http.server
import sys
import os


class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to disable caching
        self.send_header(
            "Cache-Control", "no-store, no-cache, must-revalidate, max-age=0"
        )
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


def run(port:int server_class=http.server.HTTPServer, handler_class=NoCacheHTTPRequestHandler):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving from port {server_address[1]}...")
    httpd.serve_forever()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory_to_serve = sys.argv[1]
        port = sys.argv[2] if len(sys.argv) > 2 else 8008
        print(f"Serving from directory: {directory_to_serve}")
        os.chdir(
            directory_to_serve
        )  # change the working directory to serve files from the specified directory
    run(port=int(port))
