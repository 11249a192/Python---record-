#Function to print Fibonacci sequence
def fibonacci(n):
   a, b = 0, 1
5 / 27
   print("Fibonacci sequence:")
   for _ in range(n):
       print(a, end=' ')
       a, b = b, a + b
# Get user input
N = input("Enter the number of terms (N > 0): ")
# Validate input
if N.isdigit():
   N = int(N)
   if N > 0:
       fibonacci(N)
   else:
       print("Invalid input. Please enter a number greater than 0.")
else:
   print("Invalid input. Please enter a positive integer.")
