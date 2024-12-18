def count_in_list(l: list, w: str) -> int:
    counter = 0
    for item in l:
        if item == w:
            counter += 1
    return counter