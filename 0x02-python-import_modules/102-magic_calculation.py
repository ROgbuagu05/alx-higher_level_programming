def magic_calculation(a, b):
    """Does the same thing as the Python bytecode."""

    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c += i
        return (c)
    else:
        return (sub(a, b))
