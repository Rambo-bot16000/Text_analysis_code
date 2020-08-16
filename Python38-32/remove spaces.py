#function to count words in a string
def word_count(user_input):
 return len(user_input.split())
res = word_count(input())
print ("The number of words in string are : " +  str(res))

#funtion to return the average length of the words in the string      
def remove(string): 
    return string.replace(" ", "")#removes spaces from string

spaceless_string = remove(input("Please enter your string:"))#new string without spaces called spaceless_string
length_of_spaceless_string = len(spaceless_string)#variable for length of spaceless string
word_count(input())#runs word count function
average_length = (length_of_spaceless_string/res)#assigns variable to average_length; calculated by dividing res(number of words in the string) by length of spaceless string
print ("The average length of words in this string is " + str(average_length))#prints average length




