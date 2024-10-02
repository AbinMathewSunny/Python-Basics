
#square of alost using list comprehension

'''
numbers = [1,2,3]
new_list = [n**2 for n in numbers]
print(new_list)
'''


#Dictionary comprehension
#print the length of each word of the sentence using dictionary comprehension
sentence = input("Enter the sentence")
result = {word:len(word) for word in sentence.split()}
print(result)