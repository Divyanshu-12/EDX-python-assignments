# Assume s is a string of lower case characters.

''' Write a program that prints the longest substring of s in which the letters occur in alphabetical order '''



input_list = ['pufhfqzqkvszza', 'jafyralpkjatvqrlnuv', 'gadumzqj', 'abcdefghijklmnopqrstuvwxyz']

def longest_substring(input_string):     # Function which takes an Input String

	string_size = len(input_string)      # Fetching Length of the Input String
	#print(string_size)

	str_list = []                        # Empty List to store the substrings

	for indx in range(string_size):         
		flag = 0
		temp_str = ''+input_string[indx]        
		temp_indx = indx
		while flag==0:
			if (temp_indx+1) == string_size:              # Breaks the Loop if current index is greater than the Size of String
				flag=1
				#print(temp_str)
				str_list.append(temp_str)                 # Appends the SubString to the List
			elif input_string[temp_indx] <= input_string[temp_indx+1]:      # Compares the characters
				temp_str += input_string[temp_indx+1]
				temp_indx += 1
			else:
				flag=1
				#print(temp_str)
				str_list.append(temp_str)                 # Sets the flag = 1 and appends the substring to the list
	#print(str_list)
	return(max(str_list, key=len))                        # returns the string with maximum length 

for strng in range(len(input_list)):
	res = longest_substring(input_list[strng])
	print(f"Longest Substring of {input_list[strng]} is: {res}")   # applies the function on the list of strings and returns the output.


# OUTPUT:
'''

OUT[]: Longest Substring of pufhfqzqkvszza is: fqz
	   Longest Substring of jafyralpkjatvqrlnuv is: lnuv
	   Longest Substring of gadumzqj is: adu
	   Longest Substring of abcdefghijklmnopqrstuvwxyz is: abcdefghijklmnopqrstuvwxyz

'''