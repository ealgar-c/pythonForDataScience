from time import sleep

def yielding_test(lst: range) -> None:
    for i in lst:
        yield i
        print()

def main():
    for elem in yielding_test(range(10)):
        sleep(0.5)

if __name__ == "__main__":
    main()