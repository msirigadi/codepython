"""
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
"""

max_number = int(input("Enter an integer num: "))2
odd_list = [i for i in range(1, max_number) if i%2 == 1 ]
print(odd_list)