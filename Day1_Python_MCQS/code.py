# Python script containing code for all 25 MCQs from the updated PDF ("Welcome to Python MCQS (1).pdf")
# Each question is numbered (1, 2, 3, ...) with the correct answer, explanation, and code
# Answers follow the updated answer key, which is now fully accurate

# 1. What will print(name[0:3]) output if name = "subhan"?
# Correct Answer: A) sub
# Explanation: String slicing [0:3] extracts characters from index 0 to 2 (end index 3 is exclusive).
# For name = "subhan", indices are: s(0), u(1), b(2), h(3), a(4), n(5). Thus, name[0:3] gives "sub".
name = "subhan"
print("Q1:", name[0:3])  # Output: sub

# 2. What does print(name[3:-1]) display for name = "subhan"?
# Correct Answer: A) ha
# Explanation: Slice [3:-1] starts at index 3 and goes to the second-to-last character.
# For name = "subhan", indices are: s(0), u(1), b(2), h(3), a(4), n(5). So, name[3:-1] is h(3), a(4), giving "ha".
name = "subhan"
print("Q2:", name[3:-1])  # Output: ha

# 3. What will print(str1.endswith("Id")) return if str1 = "hello World subhan"?
# Correct Answer: B) False
# Explanation: endswith("Id") checks if the string ends with "Id". For str1 = "hello World subhan",
# it ends with "an", not "Id", so it returns False.
str1 = "hello World subhan"
print("Q3:", str1.endswith("Id"))  # Output: False

# 4. What will print(str1.startswith("he")) return if str1 = "hello World subhan"?
# Correct Answer: A) True
# Explanation: startswith("he") checks if the string begins with "he". For str1 = "hello World subhan",
# it starts with "he", so it returns True.
str1 = "hello World subhan"
print("Q4:", str1.startswith("he"))  # Output: True

# 5. What does str1.lower() do if str1 = "hello World subhan"?
# Correct Answer: C) Converts string to lowercase
# Explanation: lower() converts all uppercase characters to lowercase.
# For str1 = "hello World subhan", it becomes "hello world subhan".
str1 = "hello World subhan"
print("Q5:", str1.lower())  # Output: hello world subhan

# 6. What does str1.upper() do if str1 = "hello World subhan"?
# Correct Answer: B) Converts string to uppercase
# Explanation: upper() converts all lowercase characters to uppercase.
# For str1 = "hello World subhan", it becomes "HELLO WORLD SUBHAN".
str1 = "hello World subhan"
print("Q6:", str1.upper())  # Output: HELLO WORLD SUBHAN

# 7. Output of str1.title() if str1 = "hello World subhan"?
# Correct Answer: C) Hello World Subhan
# Explanation: title() capitalizes the first letter of each word.
# For str1 = "hello World subhan", it becomes "Hello World Subhan".
str1 = "hello World subhan"
print("Q7:", str1.title())  # Output: Hello World Subhan

# 8. What does str1.capitalize() do if str1 = "hello World subhan"?
# Correct Answer: A) Capitalizes first letter only
# Explanation: capitalize() capitalizes only the first character and converts the rest to lowercase.
# For str1 = "hello World subhan", it becomes "Hello world subhan".
str1 = "hello World subhan"
print("Q8:", str1.capitalize())  # Output: Hello world subhan

# 9. What is output of str2.replace("subhan", "kaladi") if str2 = "hello world subhan"?
# Correct Answer: B) hello world kaladi
# Explanation: replace() replaces all occurrences of "subhan" with "kaladi".
# For str2 = "hello world subhan", it becomes "hello world kaladi".
str2 = "hello world subhan"
print("Q9:", str2.replace("subhan", "kaladi"))  # Output: hello world kaladi

# 10. What will print(str3.find("K")) return if str3 = "Subhan Kaladi"?
# Correct Answer: A) 7
# Explanation: find() returns the lowest index of "K". For str3 = "Subhan Kaladi",
# indices are: S(0), u(1), b(2), h(3), a(4), n(5),  (6), K(7), a(8), l(9), a(10), d(11), i(12).
# "K" is at index 7.
str3 = "Subhan Kaladi"
print("Q10:", str3.find("K"))  # Output: 7

# 11. What will print(str3.find("M")) return if str3 = "Subhan Kaladi"?
# Correct Answer: C) -1
# Explanation: find() returns -1 if the substring is not found.
# For str3 = "Subhan Kaladi", there is no "M", so it returns -1.
str3 = "Subhan Kaladi"
print("Q11:", str3.find("M"))  # Output: -1

# 12. What will print(str3.count("Kaladi")) return if str3 = "Subhan Kaladi"?
# Correct Answer: B) 1
# Explanation: count() counts occurrences of "Kaladi".
# For str3 = "Subhan Kaladi", "Kaladi" appears once, so it returns 1.
str3 = "Subhan Kaladi"
print("Q12:", str3.count("Kaladi"))  # Output: 1

# 13. What is the result of print(str4.split(" ")) if str4 = "Subhan Kaladi"?
# Correct Answer: B) ['Subhan', 'Kaladi']
# Explanation: split(" ") splits the string at each space into a list.
# For str4 = "Subhan Kaladi", it becomes ['Subhan', 'Kaladi'].
str4 = "Subhan Kaladi"
print("Q13:", str4.split(" "))  # Output: ['Subhan', 'Kaladi']

# 14. What does len(first_name) return if first_name = input("Enter your first name: ")?
# Correct Answer: B) Total characters in input
# Explanation: len() returns the number of characters in the input string.
# For example, if input is "Subhan", len(first_name) returns 6.
# Note: Using sample input since input() can't be simulated here.
first_name = "Subhan"  # Simulating input
print("Q14:", len(first_name))  # Output: 6

# 15. Output of find_later.count("a") where find_later = "subhan $ kaladi $"?
# Correct Answer: B) 3
# Explanation: count() counts occurrences of "a". For find_later = "subhan $ kaladi $",
# "a" appears at indices 4 (s-u-b-h-a), 10 (k-a), and 12 (l-a), totaling 3 times.
find_later = "subhan $ kaladi $"
print("Q15:", find_later.count("a"))  # Output: 3

# 16. Which of the following is a valid string data type in Python?
# Correct Answer: A) "123"
# Explanation: A string is enclosed in quotes (e.g., "123"). Option B) 123 is an integer,
# C) True is a boolean, D) None is NoneType.
print("Q16:", type("123"))  # Output: <class 'str'>

# 17. What will happen if you try to add an integer and a string without type casting?
# Correct Answer: C) It will throw an error
# Explanation: Adding an integer and a string raises a TypeError.
try:
    print("Q17:", 5 + "10")  # Raises TypeError
except TypeError as e:
    print("Q17:", str(e))  # Output: unsupported operand type(s) for +: 'int' and 'str'

# 18. What function is used to convert a string "2" into an integer?
# Correct Answer: C) int("2")
# Explanation: int() converts a string representing a number to an integer.
print("Q18:", int("2"))  # Output: 2
print("Q18 Type:", type(int("2")))  # Output: <class 'int'>

# 19. Which of the following is not part of Python's character set for strings?
# Correct Answer: D) Car engine codes
# Explanation: Python strings support Unicode, including letters, digits, and emojis.
# "Car engine codes" is not a standard character set for strings; it’s an invalid option.
s = "ABC123😊"
print("Q19:", s)  # Output: ABC123😊 (demonstrates letters, digits, emojis are valid)

# 20. Which of the following is a valid Python identifier?
# Correct Answer: B) my_variable
# Explanation: A valid identifier starts with a letter or underscore and contains letters, digits, or underscores.
# Only B) my_variable is valid.
my_variable = 10
print("Q20:", my_variable)  # Output: 10

# 21. What data type does input() return?
# Correct Answer: B) str
# Explanation: input() always returns a string.
# Note: Using sample input since input() can't be simulated.
result = "123"  # Simulating input
print("Q21:", type(result))  # Output: <class 'str'>

# 22. What is the index of "K" in "Subhan Kaladi"?
# Correct Answer: C) 7
# Explanation: "K" is at index 7 in "Subhan Kaladi".
s = "Subhan Kaladi"
print("Q22:", s.find("K"))  # Output: 7

# 23. Which method is used to find a character's index?
# Correct Answer: C) find()
# Explanation: find() returns the index of the first occurrence or -1 if not found.
s = "Subhan"
print("Q23:", s.find("h"))  # Output: 3

# 24. Which method counts how many times a substring appears?
# Correct Answer: B) count()
# Explanation: count() counts occurrences of a substring.
s = "Subhan Kaladi"
print("Q24:", s.count("a"))  # Output: 3

# 25. Which method converts all characters to capital letters?
# Correct Answer: D) upper()
# Explanation: upper() converts all characters to uppercase.
s = "Subhan Kaladi"
print("Q25:", s.upper())  # Output: SUBHAN KALADI