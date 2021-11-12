def flatten(sequence):
    result_list = []
    for x in sequence:
        if isinstance(x, (list, tuple)):
            result_list = result_list + flatten(x)
        else:
            result_list.append(x)

    return result_list

