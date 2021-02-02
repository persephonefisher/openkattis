# Python 3.9 solution for Open Kattis problem "Quality-Adjusted Life-Year" by Persephone Fisher

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Initialize counter variable
answer = 0

# Accept input (the number of life periods) as a string with the input() function, convert that
# number to an integer with the int() function, then cycle through that many times using a for 
# loop and the range() function
for i in range(int(input())):

   # accept input as a string with input(), convert the string to a list with string.split() method,
   # then convert the elements of the list to float with the map() function. Since there are only
   # two inputs, store the first element of the list in the q variable and the second in the y 
   # variable
   q, y = map(float, input().split())
   
   # Keep a running total of the quantity of life periods
   answer += q * y

# Use the print() function to display the answer calculated in the for loop above
print(answer)
