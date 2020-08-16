#function to count words in a string
def word_count(user_input):
 return len(user_input.split())
res = word_count(input())
print ("The number of words in string are : " +  str(res))






