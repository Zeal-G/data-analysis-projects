# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'
print(len(text))
print(text[1:10])

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!
print(text[24:36])

# 3. Print a slice of the middle 12 characters from 'text'.
print(len(text))
print(text[12:24])

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
for char in word:
   print(char)

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
text = 'Strings_are_sequences_of_characters.'
# Obtain the reversed iterator and convert it to a list
reversed_text = ''.join(reversed(text))

print(reversed_text)


# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').
for char in word[::-1]:
   print(char)
#new variable
reversed_word = ''.join(reversed(word))
#print(reversed_word)

for char in reversed_word[::-1]:
   print(char)
