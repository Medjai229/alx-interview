#!/usr/bin/python3
import sys


def print_status(size, status):
    
    print(f'File size: {size}')

    for code, count in status.items(): # sorted
        if count > 0:
            print (f'{code}: {count}')









def main():
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    size = 0
    count = 0
    try:
        for line in sys.stdin:
            split_line = line.split()
            if count % 10 == 0 and count != 0:
                print_status(size=size, status= status_codes)
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
        print_status(size=size, status= status_codes)
    except KeyboardInterrupt:
        print_status(size=size, status= status_codes)
        raise

if __name__ == "__main__":
    main()