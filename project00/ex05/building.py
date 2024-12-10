import sys

def main():
	try:
		lower = 0
		upper = 0
		numbers = 0
		spaces = 0
		symbols = 0
		if len(sys.argv) > 2:
			raise AssertionError("Wrong number of arguments")
		string = sys.argv[1] if len(sys.argv) == 2 else input("Insert your input: ")
		for c in string:
			if c.isalpha():
				if c.islower():
					lower += 1
				else:
					upper += 1
			elif c.isnumeric():
					numbers += 1
			elif c.isspace():
					spaces += 1
			elif c.isprintable():
					symbols += 1
		print(f"The text contains {len(string)} characters.")
		print(f"{upper} upper letters")
		print(f"{lower} lower letters")
		print(f"{symbols} punctuation marks")
		print(f"{spaces} spaces")
		print(f"{numbers} digits")
	except Exception as err:
		print(f"{err.__class__.__name__}: err")
     
if __name__ == "__main__":
	main()