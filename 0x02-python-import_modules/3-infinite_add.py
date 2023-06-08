#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the result of the addition of all arguments."""
    import sys

    args = sys.argv[1:]

    args_sum = sum(int(arg) for arg in args)
    print("{:d}\n".format(args_sum))
