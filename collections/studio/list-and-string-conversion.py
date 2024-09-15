proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]
print(strings)

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
if "," ";" or "just_spaces" in strings:
  print("yes")

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
for x in proto_list1:
  print(x)
reversed_proto1 = reversed(proto_list1)
print(reversed_proto1)

for x in reversed_proto1:
    print(x)

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
for x in proto_list2:
  print(x)
reversed_proto2 = reversed(proto_list2)
print(reversed_proto2)

for x in reversed_proto2:
    print(x)

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
for x in proto_list3:
  print(x)

reversed_proto3 = reversed(proto_list3)
print(reversed_proto3)

for x in reversed_proto3:
    print(x)

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
for x in proto_list4:
  print(x)

reversed_proto4 = reversed(proto_list4)
print(reversed_proto4)

for x in reversed_proto4:
    print(x)
