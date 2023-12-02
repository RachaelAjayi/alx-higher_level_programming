#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print arguments addition."""

    all_arg = 0
    for i in range(len(sys.argv) - 1):
        all_arg += int(sys.argv[i + 1])
    print("{}".format(all_arg))
