# Creating a list

favourite_fruits = ["Mango","Watermelon","Grape","Apple","Strawberry"]
print(favourite_fruits)


# Accessing Elements

colors = ['red', 'blue', 'purple', 'yellow','green']
print(colors[0])
print(colors[2])
print(colors[-1])


#Modifying a List

numbers = [10,20,30,40,50]
numbers[1] = 25  #changes the second item to 25
numbers.append(60)  #adds 60 in the end of the list
print(numbers)



#List slicing

names = ['Marcus' ,'Mia', 'Bob', 'Kenny', 'Kelton']
subset = names[:3]   #slicing the first three elements
print(subset)



#Looping through a List

numbers = list(range(1, 11))  #list of numbers from 1 to 10
for number in numbers:
    print(number ** 2)  #prints each number squared



#List methods: append and extend

shopping_cart = []  # Create an empty list
shopping_cart.append('milk')  
shopping_cart.append('bread')
shopping_cart.append('eggs')

shopping_cart.extend(['butter', 'cheese']) 
print(shopping_cart)



#Finding Maximum and minimum in a List

numbers = [45, 22, 88, 56, 92, 33]
max_value = max(numbers)
min_value = min(numbers)  
print("Maximum value:", max_value)
print("Minimum value:", min_value)



#Counting occurences

letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_a = letters.count('a')
print("The letter 'a' appears", count_a, "times.")



#List Comprehension

squares_of_evens = [x**2 for x in range(0, 11) if x % 2 == 0]
print(squares_of_evens)



# Removing Duplicates

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_numbers = list(set(numbers))  
print(unique_numbers)