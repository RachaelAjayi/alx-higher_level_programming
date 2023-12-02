#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    """Print all the names defined by the module hidden_4."""

    for i in range(len(dir(hidden_4))):
        if dir(hidden_4)[i].startswith("__"):
            continue
        else:
            print(dir(hidden_4)[i])
