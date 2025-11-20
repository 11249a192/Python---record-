def main():
   # Step 1: Input file name
   filename = input("Enter the filename: ")
   # Step 2: Open file and display first N lines
   N = int(input("Enter number of lines to display: "))
   print(f"\nFirst {N} lines of the file:")
   with open(filename, 'r') as file:
       for i in range(N):
           line = file.readline()
           if line == '':
               print("End of file reached.")
               break
           print(line.strip())
 # Step 3: Count word frequency
   word = input("\nEnter the word to find its frequency: ").lower()
   with open(filename, 'r') as file:
       content = file.read().lower()
       frequency = content.count(word)
  print(f"\nThe word '{word}' occurred {frequency} times in the file.")
# Run the function
main()
