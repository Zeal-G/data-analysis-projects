#Data Type Practice
#print('dog' == 'cat')
#print(3 < 4)
#print(3 > 10)
#print('dog' != 'cat')
#false In line 1, the equality operator, ==, compares the strings 'dog' and 'cat'. Since these are not the same, the comparison returns the value False.
#true In line 1, the equality operator, ==, compares the strings 'dog' and 'cat'. Since these are not the same, the comparison returns the value False.
#false The comparison in line 3 returns False, since 3 is not larger than 10
#true In line 4, the != operator stands for “not equal”, so 'dog' != 'cat' returns True, while something like 3 != 3 would return False
#print(3 < 4)
#print(type(3 < 4))

#print('dog' == 'cat')
#print(type('dog' == 'cat'))
#True
#<class 'bool'>
#False
#<class 'bool'>
#print(type(True))
#print(type("True"))
#print(True == "True")
#<class 'bool'> Putting quotes around boolean values ("True" and "False") makes them strings, just like "1234" is a string rather than an int data type
#<class 'str'>
#False Line 3 shows that even though they look similar, True and "True" are not the same! str and bool are different data types
#num = 37
#other_num = 40

#print(5 == 5)
#print('abc' == 'def')
#print(num == other_num - 3)
#True In line 28 the two values are equal, so the expression evaluates to True
#False In line 29, the string 'abc' is not equal to 'def', so we get False
#True Line 30 compares the result of other_num - 3 with the value stored in num
#text = "Don't Panic"

#if len(text) >= 10:
 #  print(text, "has more than 10 characters.")
#If the comparison is True, then line 4 prints the message to the console. 
# If the string is less than 10 characters long, then no message appears
name = input('Aaliyah')
if len(name) < 5: #if len(name) >= 8:
  print("Welcome, " + name + "!")
else:
   print("Invalid username.")