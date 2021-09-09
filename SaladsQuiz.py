from itertools import combinations_with_replacement

# Question 1
# We have an unlimited supply of tomatoes, bell peppers and lettuce. We want to make a salad
# out of 4 units among these three ingredients (we do not have to use all
# ingredients). The order in which we use the ingredients does not matter. How many different salads we can make?
# We do not have the formula to answer this question yet, so try to list all the salads first or create a program
# that will do that for you. Then you can count the number of salads by hand (note the answer to the problem should be the number).

count = 0

for c in combinations_with_replacement("TBL", 4):
    print("".join(c))
    count += 1

print(count)

#Other example
#Here is the code that lists all salads from the previous video.
#Here T=`tomato', B=`bell pepper', L=`lettuce', E=`eggplant'.
# You can run this code and observe the result.
for c in combinations_with_replacement("TBLE", 7):
    print("".join(c))