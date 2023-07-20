#!/usr/bin/python3

import sys
import signal

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

def print_statistics():
    print("Total file size: File size:", total_file_size)
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")

total_file_size = 0
status_codes = {}

try:
    signal.signal(signal.SIGINT, signal_handler)

    for line_number, line in enumerate(sys.stdin, start=1):
        if line_number % 10 == 0:
            print_statistics()

        parts = line.strip().split(" ")
        if len(parts) != 7:
            continue

        ip, _, _, status_code, file_size = parts
        if not (status_code.isdigit() and file_size.isdigit()):
            continue

        status_code = int(status_code)
        file_size = int(file_size)
        total_file_size += file_size

        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

except KeyboardInterrupt:
    print("\nKeyboard interruption detected. Printing current statistics:")
    print_statistics()

