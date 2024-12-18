def count_in_list(l: list, w: str) -> int:
    '''
		Function that counts all the matches of a str in a list
    '''
    counter = 0
    for item in l:
        if item == w:
            counter += 1
    return counter