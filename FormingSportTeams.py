from itertools import combinations

#In how many ways can one select a team of five students out of ten students? R/: 252
teams = 0;
for c in combinations("abcdefghij",5):
    print("".join(c))
    teams+=1
print(teams)

#In how many ways can one partition ten students into two teams of size five? R/ 126
print(teams/2)
