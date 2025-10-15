def reverse_sort_dictionary(data):
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary")

    for key, value in data.items():
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("Each value must be a tuple with two elements")

    sorted_keys = sorted(data.keys(), reverse=True)

    result = [(key, data[key][0]) for key in sorted_keys]

    return result
