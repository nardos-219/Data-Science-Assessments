def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result

""" Calculate the factorial of a number.
    Example: 5! = 5 * 4 * 3 * 2 * 1 """

def main():
    num = int(input("Enter a number: "))
    print("Factorial:", factorial(num))


if __name__ == "__main__":
    main()
