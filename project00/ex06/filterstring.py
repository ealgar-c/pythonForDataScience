from ft_filter import ft_filter
import sys

def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        s = str(sys.argv[1])
        l = int(sys.argv[2])
        print(ft_filter(s, l))
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")

if __name__ == "__main__":
    main()