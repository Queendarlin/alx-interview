#!/usr/bin/python3
"""Module for log parsing"""
import sys
import signal
import re

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = re.match(r"(\d+\.\d+\.\d+\.\d+) - \[.*]"
                         r"\"GET /projects/260 HTTP/1\.1\" (\d+) (\d+)", line)
        if match:
            status_code = int(match.group(2))
            file_size = int(match.group(3))
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        line_count += 1
        if line_count == 10:
            print_stats()
            line_count = 0
except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
