#!/usr/bin/env python3
"""Serve the RealmQuest: Beyond the Veil promotional website."""

import os
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

def run():
    port = int(os.environ.get("PORT", 8080))
    host = "127.0.0.1"
    
    # Explicitly serve from the script's root directory
    handler = partial(CustomHandler, directory=str(ROOT))
    
    # Allow immediate reuse of the port
    HTTPServer.allow_reuse_address = True
    
    server = HTTPServer((host, port), handler)
    print(f"\n=======================================================")
    print(f" RealmQuest site running at: http://{host}:{port}/")
    print(f" Press Ctrl+C to stop.")
    print(f"=======================================================\n")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.server_close()

if __name__ == "__main__":
    run()