def fibonacci(n):
    sequence = []
    a, b = 0, 1
  """Generate Fibonacci sequence up to n terms."""

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence

def main():
    terms = int(input("Enter number of terms: "))
    
    if terms <= 0:
        print("Please enter a positive number.")
    else:
        result = fibonacci(terms)
        print("Fibonacci Sequence:", result)
      
  main()
