class MyMath:
    def calculate(self, operation, n):

        if operation == "sum":
            result = n * (n + 1) // 2
            print("Sum of first", n, "natural numbers:", result)

        elif operation == "prime":
            num = 2           # Start checking numbers from 2
            count = 0         # How many primes we have found

            print("First", n, "prime numbers:", end=" ")
            while count < n:
                is_prime = True
                for i in range(2, num):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(num, end=" ")  # Print the prime number directly
                    count += 1
                num += 1
            print()  # Move to new line after printing primes

        elif operation == "fibonacci":
            a, b = 0, 1
            print("Fibonacci series:")
            for i in range(n):
                print(a, end=" ")
                a, b = b, a + b
            print()

        elif operation == "factorial":
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            print("Factorial of", n, "is:", fact)

        else:
            print("Invalid operation")


# Main Program
math_tool = MyMath()

print("1. Sum of first n natural numbers")
print("2. First n prime numbers")
print("3. Fibonacci series")
print("4. Factorial")

choice = int(input("Enter your choice (1-4): "))
n = int(input("Enter the value of n: "))

if choice == 1:
    math_tool.calculate("sum", n)
elif choice == 2:
    math_tool.calculate("prime", n)
elif choice == 3:
    math_tool.calculate("fibonacci", n)
elif choice == 4:
    math_tool.calculate("factorial", n)
else:
    print("Invalid choice")
