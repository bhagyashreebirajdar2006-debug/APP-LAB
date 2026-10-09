
import re

text = input("Enter a text: ")

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

print("\nEmail addresses found:")

for match in re.finditer(pattern, text):
    print(match.group())
