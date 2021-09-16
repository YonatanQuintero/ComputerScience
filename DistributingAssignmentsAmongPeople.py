from itertools import permutations
#Suppose there
#are 4 people and 9 different assignments. Each person should receive one
#assignment. Assignments for different people should be different. How many ways
#are there to do it?

count = 0

for a in permutations("123456789", 4):
    print("".join(a))
    count += 1

print(count)