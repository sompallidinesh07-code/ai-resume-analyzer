#!/usr/bin/env python3
"""
AI Resume Analyzer 3D - HTTP Server
Serves the 3D dark theme resume analyzer
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path

# Configuration
PORT = 8000
HOST = '127.0.0.1'
PROJECT_DIR = Path(__file__).parent.absolute()

class ResumeAnalyzerHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP handler for resume analyzer"""
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self.path = '/ai_resume_analyzer_3d_dark.html'
        return super().do_GET()
    
    def end_headers(self):
        """Add custom headers"""
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Custom logging"""
        if '404' not in str(args):
            super().log_message(format, *args)

def start_server():
    """Start the HTTP server"""
    os.chdir(PROJECT_DIR)
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer((HOST, PORT), ResumeAnalyzerHandler)
    
    print("\n" + "="*70)
    print("🚀 AI RESUME ANALYZER 3D - NEURAL CORE INITIALIZED".center(70))
    print("="*70)
    print("\n📍 Server Configuration:")
    print(f"   Host: {HOST}")
    print(f"   Port: {PORT}")
    print(f"   Directory: {PROJECT_DIR}")
    print("\n🌐 Access Application:")
    print(f"   → http://{HOST}:{PORT}")
    print(f"   → http://localhost:{PORT}")
    print("\n✨ Features:")
    print("   ✓ 3D Interactive Neural Core (Three.js)")
    print("   ✓ Drag & Drop Resume Upload")
    print("   ✓ Real-time Skill Analysis")
    print("   ✓ ATS Score Calculation")
    print("   ✓ Career Matching (Top 5 Roles)")
    print("   ✓ Learning Roadmap Generation")
    print("\n⌨️  Controls:")
    print("   Mouse: Drag to rotate 3D model")
    print("   Upload: Drag and drop resume PDF")
    print("\n⏹️  To stop: Press Ctrl+C")
    print("="*70 + "\n")
    
    try:
        webbrowser.open(f'http://{HOST}:{PORT}')
        print("✓ Browser opened automatically\n")
    except:
        print("⚠ Browser not available, open manually\n")
    
    try:
        print("🔄 Server is running... Listening for requests...\n")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\n⏹️ Shutdown signal received...")
        server.shutdown()
        print("✓ Server stopped gracefully")
        sys.exit(0)

if __name__ == '__main__':
    try:
        start_server()
    except OSError as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
