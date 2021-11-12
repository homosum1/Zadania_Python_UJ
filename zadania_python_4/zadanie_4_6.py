def sum_seq(sequence):
    result = 0
    for x in sequence:
        if isinstance(x, (list, tuple)):
            result += sum_seq(x)
        else:
            result += x

    return result
