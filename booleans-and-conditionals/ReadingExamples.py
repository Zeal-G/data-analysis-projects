#Data Type Practice
print('dog' == 'cat')
print(3 < 4)
print(3 > 10)
print('dog' != 'cat')
#false In line 1, the equality operator, ==, compares the strings 'dog' and 'cat'. Since these are not the same, the comparison returns the value False.
#true In line 1, the equality operator, ==, compares the strings 'dog' and 'cat'. Since these are not the same, the comparison returns the value False.
#false The comparison in line 3 returns False, since 3 is not larger than 10
#true In line 4, the != operator stands for “not equal”, so 'dog' != 'cat' returns True, while something like 3 != 3 would return False
print(3 < 4)
print(type(3 < 4))

print('dog' == 'cat')
print(type('dog' == 'cat'))
#True
#<class 'bool'>
#False
#<class 'bool'>
print(type(True))
print(type("True"))
print(True == "True")
#<class 'bool'> Putting quotes around boolean values ("True" and "False") makes them strings, just like "1234" is a string rather than an int data type
#<class 'str'>
#False Line 3 shows that even though they look similar, True and "True" are not the same! str and bool are different data types


num = 37
other_num = 40

print(5 == 5)
print('abc' == 'def')
print(num == other_num - 3)
#True In line 28 the two values are equal, so the expression evaluates to True
#False In line 29, the string 'abc' is not equal to 'def', so we get False
#True Line 30 compares the result of other_num - 3 with the value stored in num
#text = "Don't Panic"

#if len(text) >= 10:
 #  print(text, "has more than 10 characters.")
#If the comparison is True, then line 4 prints the message to the console. 
# If the string is less than 10 characters long, then no message appears

num = 10
other_num = 20

if num > other_num:
   print(num, "is greater than", other_num)
elif num < other_num:
  print(num, "is less than", other_num)
else:
   print(num, "is equal to", other_num)
#elif book example ^^^^

character = 'P'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

if character in lowercase:
   print(character, 'is a lowercase letter.')
elif character in uppercase:
   print(character, 'is an UPPERCASE letter.')
elif character in digits:
   print(character, 'is a number.')
else:
   print('&**%#!', character, 'is a punctuation mark or a space.')
#multiple elif example ^^^

#entry = int(input("Enter a whole number: 7"))

#if entry%2 == 0:
 #  print("EVEN!")

  # if entry > 0:
  #    print("POSITIVE")

#Nested conditionals example - doesnt return positive statement though? why?


num = 7
if num%2 == 0:
   if num%2 == 1:
      print("odd")  #The code runs but doesn’t print anything.


#checking understanding questions
answer_1 = 'yes'
answer_2 = 'no'


if answer_1 == 'yes':
   if answer_2 == 'yes':
      print("Both of you agree!")
   else:
      print("You two need to work this out.") #You two need to work this out.
else:
   if answer_2 == 'yes':
      print("Stop arguing and work it out.")
   else:
      print("Clean your bathroom anyway!") 
#correct answer in line 93

word = input('Please enter a word: Dogs ')

if len(word) == 4:
   print("What did your mom tell you about using 4-letter words?")
else:
   if len(word) < 4:
      print("You can think of a longer word than that!")
   else:
      print("Excellent word!") # Nested conditional example and the output was line 109
# Nested conditional ^^
word = input('Please enter a word: Dogs ')

if len(word) == 4:
   print("What did your mom tell you about using 4-letter words?")
elif len(word) < 4:
   print("You can think of a longer word than that!")
else:
   print("Excellent word!") # Chained conditional example and got the same result as nested
#CHAINED CONDITIONAL^^
