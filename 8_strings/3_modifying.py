# Python has a set of built-in methods that you can use on strings.
#? UpperCase
a = "       heLlO wOrLd"
print(a.upper()) #? Converts to upper-case
print(a.capitalize()) #? First letter is capitalized
print(a.lower()) #? Converts to lower-case
print(a.title()) #? Converts all fisrt letter of the word capitalized
print(a.strip()) #? Removes all whitespace from both-side(left to right)
print(a.rstrip()) #? Removes whitespace of right-side
print(a.lstrip()) #? Removes whitespace of left-side
print(a.split()) #? Converts string to a list separated by comma of each word
print(a.lower().replace("hello", "welcome")) #? Replaces the word. First parameter takes old word and second takes new word