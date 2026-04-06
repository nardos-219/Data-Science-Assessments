def reverse_string(text):
    return text[::-1]
    """ Reverse a given string."""

def main():
    user_input = input("Enter a string: ")
    print("Reversed:", reverse_string(user_input))

main()
