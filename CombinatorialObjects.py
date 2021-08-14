from itertools import product
from itertools import permutations

#Rule of sum
print(['Alice','Bob','Charlie'] + [0,1,2,3])
#output
#['Alice', 'Bob', 'Charlie', 0, 1, 2, 3]

#Rule of product
for p in product(['a','b','c'],['x','y']):
    print("".join(p))
#output
#ax
#ay
#bx
#by
#cx
#cy

#Tuples
for p in product ("ab",repeat=3):
    print("".join(p))
#Output:
#aaa
#aab
#aba
#abb
#baa
#bab
#bba
#bbb

#Permutations
for p in permutations("abcd",2):
    print("".join(p))
#Output
#ab
#ac
#ad
#ba
#bc
#bd
#ca
#cb
#cd
#da
#db
#dc