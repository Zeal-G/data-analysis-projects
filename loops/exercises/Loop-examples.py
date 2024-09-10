for num in range(51):
   print(num)
#iteration example

for num in range(51):
   print(num)

print("Not in the loop!")
#Definitive iteration example

for num in range(4):
   print(num)
   print("Hello" * num)

print("Done!")
# line by line example

for number in range(10):
   print("I have", 12 - number, "cookies. I'm going to eat one!")
   # FOR loops examples - The answer was 9 lines return in the output

for num in range(4):
   print(num)
   print("Hello" * num)
#more on range

num = 13

for number in range(num):
   if number%3 == 0:
      print(number, "is divisible by 3.")
   else:
      print(number, "is NOT divisible by 3.")
#printed out 13 times starting at 0 - LOOP PRACTICE

text = 'Coding ROCKS!'
num_vowels = 0

for char in text:
   if char in 'aeiou':
      num_vowels += 1

print(text, "contains", num_vowels, "lowercase vowels.")
#LOOP PRACTICE
#In the second loop, the condition char in 'aeiou' returns True if the value of char matches any part of the string.
# When this happens, num_vowels gets increased by 1 (line 6).
# Coding ROCKS! contains 2 lowercase vowels, so line 6 only runs 2 times. 
# For every other character in the string, the line gets skipped.

total = 0
increase_by = 14

while total < 1000:
   total += increase_by
   print(total)

print("Not in the loop!")
# WHILE loop example


#for num in range(21):
  #print(num)

#FOR loops vs. WHILE loops
num = 0

while num < 21:
   print(num)
   num += 1
# FOR loop re wrote as a WHILE loop

for iteration in range(42):
   print('This is iteration number:', iteration+1)

   if iteration > 4:
      break

print("The loop is done!")
# How to break a loop example!

flavors = ['Vanilla', 'Chocolate', 'Cookie Dough']
toppings = ['Hot Fudge', 'Oreos', 'Marshmallows']
for one in flavors:
   for two in toppings:
      print(one, 'Topped with', two)
#example from youtube

def happy_birthday(name, age):
   print(f'Happy birthday to {name}!')
   print(f'You are {age} years old!')
   print('Happy Birthday to you!')
   print()
happy_birthday("Bro", 20)
happy_birthday("Steve", 30)
happy_birthday("Jo", 40)
#example from youtube

def display_invoices(username, amount, due_date):
   print(f"Hello {username}")
   print(f"Your bill of ${amount: .2f} is due {due_date}")
display_invoices("Bro", 42.50, "01/01")