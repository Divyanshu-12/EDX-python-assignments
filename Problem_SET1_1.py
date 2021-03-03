#PROBLEM SET1 Q1

# Assume s is a string of lower case characters.

'''Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print: '''

vowels = 0
for char in s:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        vowels += 1
print("Number of vowels:", vowels)



# OUTPUT:

# IN[] => s = 'eapbkajcu'
# OUT[] => Number of vowels: 4