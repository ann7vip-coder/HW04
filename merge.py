def merge_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists")

    merged = list1 + list2

    for item in merged:
        if not isinstance(item, int):
            raise TypeError("All elements in the lists must be integers")

    for i in range(len(merged)):
        for j in range(i + 1, len(merged)):
            if merged[i] > merged[j]:
                merged[i], merged[j] = merged[j], merged[i]

    return merged
