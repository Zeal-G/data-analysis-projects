def greet():
    print("Hello")
    print("How do you do")

greet()

# simple def() function - define function practice, can call function again and again
# always define before calling

def greet(name):  #the variable in the greet function is called name
    print("Hello", name)
    print("How do you do") #the name Jack translate to the variable 'name' 
#then the greet function is executed with the name Jack
greet("Jack") # This value (jack) is an argument
#this example is a single argument for define function

def add_numbers(n1, n2): #2 parameters for multiple arguments
    result = n1 + n2 #inside the function
    print("The sum is", result)

number1 = 5.4 #argument 1 for addin numbers will also be read as parameter n1
number2 = 6.7 #argument 2 for addin numbers will be read as parameter n2
add_numbers(number1, number2)#2 arguments to the add numbers function
#multiple argument statement for functions

#return value from a function
def add_numbers(n1, n2): 
    result = n1 + n2
    return result #return wherever it is located means that it returns to the define function

number1 = 5.4 
number2 = 6.7 
result = add_numbers(number1, number2) #call the add nnumbers function w number1 and number2 
print("The sum is", result)
#return will always go back to the defined function

#marks = [55, 64, 75, 80, 34]

#length = len(marks)
#print("Length is", length)
#using sum function with defined variable name to get it to do the action
#marks_sum = sum(marks) 
#print("The total marks you got is", marks_sum)

#final example- functions to find average marks
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks

#calculate the grade and return it
def computer_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

marks = [55, 64, 75, 80, 34]
average_marks = find_average_marks(marks)
print("Your average mark is:", average_marks)

grade = computer_grade(average_marks)
print("Your grade is:", grade)