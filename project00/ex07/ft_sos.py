import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

def check_string(s: str) -> bool:
    if any(not (c.isalnum() or c == ' ') for c in s):
        return False
    return True


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("arguments are bad")
        s = sys.argv[1]
        if check_string(s) == False:
            raise AssertionError("arguments are bad")
        le = 0
        for c in s:
            le += 1
            print(NESTED_MORSE[c.upper()], end="")
            if le is not len(s):
                print(' ', end="")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")

if __name__ == "__main__":
    main()