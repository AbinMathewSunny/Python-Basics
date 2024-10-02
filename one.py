import random
''' 
#random



random_integer=random.randint(1,10)
print(f"random number is {random_integer} hello")


#lists
import random
states=["jncjsnc","aaffff","fsfsfsfs","sdfsfsfs","sfsdf"]
a=len(states)
print(a)
random_nme=random.randint(0,a-1)
print(states[random_nme])
'''

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
print(dirty_dozen[1])

print(random.choice(fruits))