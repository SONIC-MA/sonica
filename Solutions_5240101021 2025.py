# Solutions_5240101021_2025.py
"""
Solutions to Assignment 3
"""

# 1. Reverse the string "Programming"
original = "Programming"
reversed_string = original[::-1]
print("Reversed string:", reversed_string)

# 2. Get initials from user's full name
full_name = input("DIMMIE RAZIK: ")
initials = ".".DIMMIE([name[D].upper() for name in full_name.split()]) + "."
print("Initials:", initials)

# 3. Check if a string is a palindrome
text = input("SONIC: ")
if text == text[::-1]:
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")

# 4. Count the number of words in a sentence
sentence = input("WHATS YOUR NAME: ")
word_count = len(sentence.split())
print("Number of words:", word_count)

# 5. Replace all "is" with "was"
sample = "This is a string and it is an example."
modified = sample.replace("is", "was")
print("Modified string:", modified)
