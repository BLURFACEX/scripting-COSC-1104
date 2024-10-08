def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_before(number):
    for num in range(number - 1, 1, -1):
        if is_prime(num):
            return num
    return None  # No prime before 2

def prime_after(number):
    num = number + 1
    while True:
        if is_prime(num):
            return num
        num += 1

def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def get_valid_input():
    while True:
        try:
            user_input = int(input("Enter a positive whole number: "))
            if user_input > 0:
                return user_input
            else:
                print("Input must be a positive whole number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def main():
    while True:
        # Get a valid positive integer from the user
        number = get_valid_input()

        # Find the largest prime before the number
        prime_before_number = prime_before(number)
        if prime_before_number:
            print(f"The largest prime number before {number} is {prime_before_number}.")
        else:
            print(f"There is no prime number before {number}.")

        # Check if the number is prime
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
            divisors = find_divisors(number)
            print(f"The divisors of {number} are: {divisors}")

        # Find the smallest prime after the number
        prime_after_number = prime_after(number)
        print(f"The next prime number after {number} is {prime_after_number}.")

        # Option to exit or try another number
        again = input("Do you want to try another number? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Exiting the program.")
            break

# Run the program
main()
