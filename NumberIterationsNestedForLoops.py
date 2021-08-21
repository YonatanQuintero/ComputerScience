#Number of Iterations of Nested For Loops

#What will the following program print?
n = 10
count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j and j < k:
                count += 1

print(count)