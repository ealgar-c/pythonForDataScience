from shutil import get_terminal_size as gts

def ft_tqdm(lst: range) -> None:
    term_size = gts()
    term_width = term_size.columns
    bar_width = max(10, term_width - (10 + (len(str(lst.stop) * 2))))
    
    for i in lst:
        actual_prog_ratio = (i + 1) / (lst.stop)
        eqs = int(actual_prog_ratio * bar_width)
        bar = '=' * eqs + '>' + ' ' * (bar_width - eqs)
        percent = int(actual_prog_ratio * 100)

        print(f"\r{percent}%|{bar}| {i + 1}/{lst.stop}", end="", flush=True)
        yield i