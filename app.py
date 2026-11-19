"""
Application: app.py
Máy chủ Web & API Trung tâm Điều hành AI Agent Đánh giá Yêu cầu Chào giá - Nguyễn Việt Insight
Sử dụng thư viện chuẩn của Python (http.server), chạy cục bộ tại http://localhost:8080.
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from backend.handler import run_server, NguyenVietRequestHandler, handler, app

if __name__ == '__main__':
    run_server()
