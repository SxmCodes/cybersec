'''
This will print the sum of all the numbers from 1 till the number.
number = 3 = 1+2+3 ans = 6.
'''

# This will store the sum of all the numbers.
store = 0
number = int(input("Enter a number :- "))

for i in range(1, number+1):
    store+=i

print(store)
