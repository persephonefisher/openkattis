# Python 3.9 solution for Open Kattis problem "Piece of Cake" by Persephone Fisher

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Initialize the cake list
cake = []

# Use the input() function to accept input as a string, the string.split() method to convert the
# input to a list, then cast all three list elements as int(egers) with the map() function. Since
# there are three expected inputs, each element of the list can be stored directly into variables.
n, h, v = map(int, input().split())

# Append all possible combinations of the cake's two cuts/four slices
cake.append(h * v)
cake.append((n - h) * v)
cake.append(h * (n - v))
cake.append((n - h) * (n - v))

print(max(cake) * 4)
