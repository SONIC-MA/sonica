# Solutions_5211040111_2025.py
"""
Solutions to Assignment 3
"""

# 1. Reverse the string "Programming"
original = "Programming"
reversed_string = original[::-1]
print("Reversed string:", reversed_string)

# 2. Get initials from user's full name
full_name = input("Enter your full name: ")
initials = ".".join([name[0].upper() for name in full_name.split()]) + "."
print("Initials:", initials)

# 3. Check if a string is a palindrome
text = input("Enter a word to check for palindrome: ")
if text == text[::-1]:
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")

# 4. Count the number of words in a sentence
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words:", word_count)

# 5. Replace all "is" with "was"
sample = "This is a string and it is an example."
modified = sample.replace("is", "was")
print("Modified string:", modified)
