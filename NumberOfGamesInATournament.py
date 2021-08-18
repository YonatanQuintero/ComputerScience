from itertools import combinations


for c in combinations("abcdefgh",2):
    print("".join(c))

#Recursion
def T(n):
    if n <= 1:
        return 0

    return (n -1) + T(n - 1)

print(T(8))