# Python 3.9 solution for Open Kattis problem "Nasty Hacks" by Persephone Fisher

# Use the input() function to accept input as a string, cast as an integer with
# the int() function, then iterate through each case with the range() function
# and a for loop.
for i in range(int(input())):

   # Accept the input as a string with the input() function, convert the input
   # string to a list with the string.split() method, then convert all of the
   # list elements to integers using the map() function. Since there are only
   # three expected inputs, they can be stored in the variables r, e, and c.
   r, e, c = map(int, input().split())
   
   # Marginal advertising revenue is profit minus what it cost
   ad_rev = e - c
   
   # Use an if/else if/else statement to determine what to print for each case.
   if r < ad_rev:
      print("advertise")
   elif r > ad_rev:
      print("do not advertise")
   else:
      print("does not matter")
