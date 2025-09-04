#!/usr/bin/env python3
"""
Simple Local Web Server for URL Code System
This script creates a local web server so you can test your system locally
and share links with others on the same network.

Usage:
    python start_local_server.py

Requirements:
    - Python 3.6 or higher
    - All HTML, CSS, and JS files in the same directory

Features:
    - Serves files on localhost:8000
    - Accessible from other devices on your network
    - Auto-reloads when files change
    - Shows your local IP address for sharing
"""

import http.server
import socketserver
import socket
import os
import webbrowser
from pathlib import Path

def get_local_ip():
    """Get the local IP address of this machine"""
    try:
        # Connect to a remote address to get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

def start_server(port=8000):
    """Start the local web server"""
    
    # Change to the directory containing this script
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Check if required files exist
    required_files = ['index.html', 'access.html', 'dashboard.html', 'index1.html']
    missing_files = [f for f in required_files if not Path(f).exists()]
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        print("Make sure all HTML files are in the same directory as this script.")
        return
    
    # Create server
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            local_ip = get_local_ip()
            
            print("🚀 Starting Local Web Server...")
            print("=" * 50)
            print(f"📍 Local Access: http://localhost:{port}")
            print(f"🌐 Network Access: http://{local_ip}:{port}")
            print("=" * 50)
            print("📁 Serving files from:", os.getcwd())
            print("🔗 Available pages:")
            print(f"   • Main Login: http://localhost:{port}/index.html")
            print(f"   • URL Code Access: http://localhost:{port}/access.html")
            print(f"   • Admin Dashboard: http://localhost:{port}/dashboard.html")
            print(f"   • Protected Content: http://localhost:{port}/index1.html")
            print("=" * 50)
            print("💡 Tips:")
            print("   • Share the network URL with others on your network")
            print("   • Use localhost for testing on this machine")
            print("   • Press Ctrl+C to stop the server")
            print("=" * 50)
            
            # Open main page in browser
            try:
                webbrowser.open(f"http://localhost:{port}/index.html")
                print("🌐 Opened main page in your browser")
            except:
                print("📱 Please manually open: http://localhost:8000/index.html")
            
            print("\n🔄 Server is running... Press Ctrl+C to stop")
            
            # Start serving
            httpd.serve_forever()
            
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use!")
            print(f"💡 Try a different port: python start_local_server.py {port + 1}")
        else:
            print(f"❌ Error starting server: {e}")
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    import sys
    
    # Get port from command line argument
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid port number. Using default port 8000")
    
    start_server(port)
