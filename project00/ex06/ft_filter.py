def ft_filter(s: str, l: int) -> list:
    is_longer = lambda s, l: True if len(s) > l else False
    return [word for word in s if is_longer(word, l)]