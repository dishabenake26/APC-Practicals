
text = input("Enter a string: ")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("Reversed string:", text[::-1])
##################################################
text = input("Enter a string: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count = count + 1

print("Number of vowels:", count)
##################################################3
text = input("Enter a word: ")

if text == text[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
################################################3
text = input("Enter a sentence: ")

words = text.split()

print("Number of words:", len(words))
#############################################3
text = input("Enter a sentence: ")
old = input("Enter word to replace: ")
new = input("Enter new word: ")

result = text.replace(old, new)

print("Updated sentence:", result)
