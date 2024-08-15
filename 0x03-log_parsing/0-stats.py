#!/usr/bin/python3
"""
Log Parser Module

This module parses log data from standard input and prints
the file size and occurrence count of each status code every 10 lines.

The module consists of two functions: `print_status` and `main`.
"""
import sys


def print_status(size, status):
    """
    Prints the size of a file and the occurrence count of each status code.
    """
    print(f'File size: {size}')

    for code, count in status.items():  # sorted
        if count > 0:
            print(f'{code}: {count}')


def main():
    """
    The main function of the program, responsible
    for parsing log data from standard input.
    """
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }
    size = 0
    count = 0
    try:
        for line in sys.stdin:
            split_line = line.split()
            if count % 10 == 0 and count != 0:
                print_status(size=size, status=status_codes)
            try:
                code = split_line[-2]
                if code in status_codes.keys():
                    status_codes[code] += 1
            except Exception:
                pass
            try:
                size += int(split_line[-1])
            except Exception:
                pass
            count += 1
        print_status(size=size, status=status_codes)
    except KeyboardInterrupt:
        print_status(size=size, status=status_codes)
        raise


if __name__ == "__main__":
    main()
