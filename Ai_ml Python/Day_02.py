# Day-02 of learning Ai/ml
# Todays
# topic: Python Collection and Memory
# Goal: Learn how python stores collection of data and why they're the foundation of Ai

# List
# fruits = ["apple", "banana", "orange"]
# finding length of fruits
# print(len(fruits))
# adding mango to fruits
# fruits.append("mango")
#remove banana
# fruits.remove("banana")
#print fruits with looping
# for fruit in fruits:
#     print(fruit)

# Tuple: similar to list but cannot be updated or being changed
# coordinates = (45,34,56,66)

# Sets: In set duplicate values are entered but at the time of output one
# once it will be represented
# lang = {"java", "python", "java", "c++"}
# printing the set
# print(lang)
# Note: Output the order is also not maintained


# Dictionaries: One of the most important data structure.
# stud = {
#     "name": "Ankit",
#     "age": 20,
#     "cgpa": 8.7
# }
#
# # printing the output
# print(stud["name"])


# Why Dictionaries Matter in Ai?
# Many api and machine learning workflows use dictionaries(or json, which is very similar) to represent structure data

#excercise-01:
# techs = ["Ai/Ml", "cybersecurity", "frontend development", "backend development", "GTM engineer"]
# #print first item
# print(techs[0])
# #print last item
# print(techs[4])
# #printing len
# print(len(techs))

# #excercise-03:
# skills = ["python", "java", "python", "sql", "java"]
# skillset = set(skills)
# print(skillset)

# # excercise-04:
# me = {
#     "name" : "Ankit",
#      "age" : 20,
#     "college": "VIT",
#     "Dream_company" : "Microsoft",
#     "favourite_lang" : "python"
# }
# for key in me:
#     print(key +":" , me[key])

'''Professionals often write:

for key, value in me.items():
    print(f"{key}: {value}")

Why?

Because .items() gives you both the key and the value directly, making the code clearer.'''
'''
#Quiz:
🎯 Quiz
Q1

Which collection removes duplicates automatically?

Q2

Which collection cannot be modified?

Q3

Which collection stores key-value pairs?

Q4

Which collection is most commonly converted into a NumPy array?

Q5

Is a string mutable or immutable?

Quiz Answers:
1. set
2. tuple
3. dict
4. list
5. string are immutable.'''