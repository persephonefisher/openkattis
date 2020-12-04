# Python 3.9 solution for Open Kattis problem R2 by Persephone Fisher

# Use the input() function to get the input as a string, the string.split() method to convert the string to a list,
# then convert the elements of the list to int(egers) with the map() function. Since there are two inputs, we can 
# store the first element of the list as r1 and the second element as answer.
r1, answer = map(int, input().split())

# Use arithmetic to solve for R2: if R2/2 + R1/2 = answer, R2+R1 = 2*answer, and R2 = 2*answer - R1
r2 = (2*answer) - r1

# Use the print() function to print our answer
print(r2)
