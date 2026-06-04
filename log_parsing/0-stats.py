#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """

""" un enfer ce code """


import sys


if __name__ == "__main__":
    """ main function """
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    total_size = 0
    line_count = 0
    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()
                if len(parts) < 9:
                    continue
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except Exception:
                continue
            if line_count % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(status_codes.keys()):
                    if status_codes[code] > 0:
                        print("{}: {}".format(code, status_codes[code]))
    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {}".format(total_size))
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print("{}: {}".format(code, status_codes[code]))
