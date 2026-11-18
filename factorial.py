def calculate_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    number = 5
    print(f"The factorial of {number} is {calculate_factorial(number)}")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
