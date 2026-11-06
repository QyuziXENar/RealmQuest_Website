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
    # Render automatically provides the PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    
    # 0.0.0.0 is required for Render/cloud hosting
    host = "0.0.0.0"
    
    handler = partial(CustomHandler, directory=str(ROOT))
    HTTPServer.allow_reuse_address = True
    server = HTTPServer((host, port), handler)
    
    print(f"\n=======================================================")
    print(f" RealmQuest site running on port {port}")
    print(f" Local URL: http://localhost:{port}/")
    print(f" Press Ctrl+C to stop.")
    print(f"=======================================================\n")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.server_close()

if __name__ == "__main__":
    run()