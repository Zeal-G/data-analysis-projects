#collection readind examples
#quotes example on how triple quotes around string print in seperate lines in the output
text = "Don't count the number of characters yourself. Python will do it for you!"

length_of_text = len(text)
print(length_of_text)
#73 output

sentence = '''This string covers
multiple lines.
Cool!'''

print(sentence)

#some_string[index] examples
'school'[2]

comics = {
    'Georgia Dunn' : 'Breaking Cat News',
    'Jan Eliot' : 'Stone Soup',
    'Wiley Miller' : 'Non Sequitur',         
    'Bill Watterson' : 'Calvin and Hobbs'
}

for key in comics.keys():
    print(key, comics[key])

 

def is_even(num): 
   return num % 2 == 0

num = 42
print(is_even(43))

 
