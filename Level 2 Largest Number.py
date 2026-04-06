def find_largest(numbers):
    """ Find the largest number in a list."""
    if not numbers:
        return "List is empty."
    
    largest = numbers[0]
    
    for num in numbers:
        if num > largest:
            largest = num
    
    return largest


def main():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Largest number:", find_largest(nums))

main()
