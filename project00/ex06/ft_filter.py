def ft_filter(s: str, s_len: int) -> list:
	"""Return an iterator yielding those items of iterable for which function\
(item)
is true. If function is None, return the items that are true."""
	def is_longer(word):
		return len(word) > s_len
	return [word for word in s.split() if is_longer(word)]
