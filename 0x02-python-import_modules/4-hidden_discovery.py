#!/usr/bin/python3
if __name__ == "__main__":
    """Prints all names defined by a given module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if not name.startswith("__"):
            print(name)
