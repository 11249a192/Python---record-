Base class
class PalindromeChecker:
   def is_palindrome(self, value):
       raise NotImplementedError("Subclasses should implement this!")
# Derived class for string palindrome
class StringPalindromeChecker(PalindromeChecker):
   def is_palindrome(self, value):
       value = value.lower().replace(" ", "")  # Normalize string
       return value == value[::-1]
# Derived class for integer palindrome
class IntegerPalindromeChecker(PalindromeChecker):
   def is_palindrome(self, value):
       str_value = str(value)
       return str_value == str_value[::-1]
# Main logic
input_value = input("Enter a value (string or integer): ")
if input_value.isdigit():
   checker = IntegerPalindromeChecker()
   is_pal = checker.is_palindrome(int(input_value))
else:
   checker = StringPalindromeChecker()
   is_pal = checker.is_palindrome(input_value)
# Display the result
if is_pal:
   print("The input is a palindrome.")
else:
   print("The input is not a palindrome.")
