#!/usr/bin/env python


import http.server
import sys
import os
from beartype import beartype


class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    A SimpleHTTPRequestHandler that adds headers to disable caching.
    """

    def end_headers(self):
        # Add headers to disable caching
        self.send_header(
            "Cache-Control", "no-store, no-cache, must-revalidate, max-age=0"
        )
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


@beartype
def run(
    directory_to_serve: str = os.getcwd(),
    port: int = 8008,
):
    """
    Run the HTTP server.
    """

    os.chdir(directory_to_serve)

    httpd = http.server.HTTPServer(("", port), NoCacheHTTPRequestHandler)

    print(f"Serving from port {port}...")

    httpd.serve_forever()


def main():
    if len(sys.argv) > 1:
        directory_to_serve = sys.argv[1]
        port = int(sys.argv[2]) if len(sys.argv) > 2 else 8008
        print(f"Serving from directory: {directory_to_serve}")

    else:
        directory_to_serve = os.getcwd()
        port = 8008

    run(directory_to_serve=directory_to_serve, port=port)


if __name__ == "__main__":
    main()
