from itertools import product

#Question
#What is the number of non-negative integers with at most four digits at least one of which is equal to 7?
#Answer 10^4 - 9^4 = 3439

count = 0
for d in product(range(10), repeat= 4):
    if 7 in d:
        count += 1

print(count)
print(10**4 - 9**4)

#Question
#What is the number of non-negative integers with at most four digits whose digits are increasing? 
#Answer 10 choose 4 = 210

count = 0
for d in product(range(10), repeat=4):
    if d[0] < d[1] and d[1] < d[2] and d[2] < d[3]:
        count += 1
        print(d)

print(count)