#Input
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
# Find length of shorter and longer string
min_len = min(len(string1), len(string2))
max_len = max(len(string1), len(string2))
# Initialize match counter
match_count = 0
# Compare characters
for i in range(min_len):
   if string1[i] == string2[i]:
       match_count += 1
# Calculate similarity percentage
similarity = (match_count / max_len) * 100
