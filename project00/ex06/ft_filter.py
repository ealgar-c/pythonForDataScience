def ft_filter(s: str, l: int) -> list:
    is_longer = lambda word: len(word) > l
    return [word for word in s.split() if is_longer(word)]
