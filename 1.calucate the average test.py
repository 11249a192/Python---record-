#Accept three test marks from the user
test1 = float(input("Enter marks for Test 1: "))
test2 = float(input("Enter marks for Test 2: "))
test3 = float(input("Enter marks for Test 3: "))
# Store the marks in a list
marks = [test1, test2, test3]
2 / 27
# Sort the list in descending order
marks.sort(reverse=True)
# Calculate the average of the best two marks
best_two_avg = (marks[0] + marks[1]) / 2
cl# Display the result
print("The best two test marks are:", marks[0], "and", marks[1])
print("The average of the best two test marks is:", best_two_avg)
Palindrome Check & Digit Occurrence Count
