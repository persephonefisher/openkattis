# Python 3.9 solution for Open Kattis problem "I've Been Everywhere, Man" by Persephone Fisher

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Accept the input as a string with the input() function, cast the input as an integer with the
# int() function, then iterate (with a for loop) through n times with the range() function.
for i in range(int(input())):
   
   # Initialize a set to hold a list of unique cities; initialized within the outer for loop on
   # line 3 so it will reset in between cases.
   cities = set()
    
   # This is the same as line 5, except it's a nested for loop (referred to as an "inner for loop")
   for j in range(int(input())):
      
      # Add each city to the set initialized above, on line 8
      cities.add(input())
   
   # Use the len() function to count the elements in the set, then print that number with the print() function.
   print(len(cities))
