# PROBLEM SET1 Q2

# Assume s is a string of lower case characters.

''' Write a program that prints the number of times the string 'bob' occurs in s. 
    For example, if s = 'azcbobobegghakl', then your program should print '''

input_string = 'azcbobobegghakl'
sub_string = 'bob'
res = 0

for i in range(len(input_string)):
	if input_string.startswith('bob', i):
		res += 1

print(f"Number of times {sub_string} occurs is: {res}")


# OUTPUT:

# OUT[] => Number of times bob occurs is: 4