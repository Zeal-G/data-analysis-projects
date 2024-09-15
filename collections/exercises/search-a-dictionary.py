flavors = {
  'chocolate' : 0.35,
  'vanilla' : 0.35,
  'strawberry' : 0.42,
  'cookies and cream' : 0.45,
  'mint chocolate chip' : 0.42,
  'fudge chunk' : 0.45,
  'saffron' : 2.25,
  'garlic' : 0.05
}
print(flavors)
## Set a variable called choice to the flavor you want to search for.
choice = "strawberry"
print(choice)
## Use an if statement to check if choice is in the flavors dictionary.
if choice in flavors:
    print("true")
else:
    print("false")
## If it is, set another variable called cost to the value associated with choice.
cost = 0.42
print(cost)
## If it isn’t, set cost to 0.
## Print the cost.

### Search a Dictionary Part 2:

## Initialize two variables: highest_cost to 0 and fanciest to an empty string.
highest_cost = 0
fanciest = ()
print(highest_cost)
print(fanciest)
## Loop through the flavors dictionary using a for loop.
for character in flavors:
    print(character)

## For each flavor, check if its price is higher than highest_cost.
highest_cost = 2.25
fanciest = "saffron"
## If it is, update fanciest to this flavor and highest_cost to its price.
print(highest_cost)
print(fanciest)
## After the loop, print the most expensive flavor.
for character in flavors:
    print(character)
print(fanciest)