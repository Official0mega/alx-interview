#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_log_line(line, total_size, status_codes):
    # Implement parsing logic
    try:
        parts = line.split()
        size = int(parts[-1])
        code = int(parts[-2])
        total_size += size
        status_codes[code] = status_codes.get(code, 0) + 1
        return total_size
    except (ValueError, IndexError):
        # Skip invalid lines
        return total_size

def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            total_size = parse_log_line(line.strip(), total_size, status_codes)

            # Print stats after every 10 lines
            if i % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        pass
    finally:
        # Print final stats
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
