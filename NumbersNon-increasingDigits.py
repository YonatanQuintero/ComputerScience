from itertools import product

# How many four-digit numbers are there such that their digits are non-increasing,
# that is each next digit is not greater than the previous one?
# Three-digit numbers are also four-digit, they just start with 0.

count = 0

for d in product(range(10), repeat=4):
        if d[0] >= d[1] and d[1] >= d[2] and d[2] >= d[3] :
            print(d)
            count += 1

print(count)