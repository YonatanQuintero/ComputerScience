from itertools import product
import itertools as it

# How many non-negative integer numbers are there below 10000 such that their sum of digits is equal to 9?

count = 0

for d in product(range(10), repeat=4):
    if d[0] + d[1] + d[2] + d[3] == 9:
        print(d)
        count += 1

print(count)

#How many non-negative integer numbers are there below 10000 such that their sum of digits is equal to 10?

count = 0

for d in product(range(10), repeat=4):
    if d[0] + d[1] + d[2] + d[3] == 10:
        print(d)
        count += 1

print(count)

#Another way

count = 0

for d in it.product(range(10), repeat = 4):
    if sum(d) == 10:
        count += 1
print(count)