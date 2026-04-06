def is_prime(number):
    if number <= 1:
        return False
  """ Check if a number is prime.
    A prime number is only divisible by 1 and itself."""
    
for i in range(2, int(number ** 0.5) + 1):
  if number % i == 0:
    return False
return True

def main():
    num = int(input("Enter a number: "))
    
    if is_prime(num):
        print(f"{num} is a Prime number.")
    else:
        print(f"{num} is NOT a Prime number.")

main()
