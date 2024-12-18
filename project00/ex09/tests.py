from ft_package import count_in_list

def main():
    print(count_in_list(["hola", "que", "tal"], "hola"))
    print(count_in_list(["hola", "que", "hola"], "hola"))
    print(count_in_list(["buenas", "que", "tal"], "hola"))

if __name__ == "__main__":
    main()