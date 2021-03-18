from itertools import product
from itertools import permutations

# --> P R O D U C T S
# --> Listing the product of two lists
# --> Don't forget to put "list" inside the print() function 
# --> print(list(prod))

list_one = [1, 2]
list_two = [3, 4]
prod = product(list_one, list_two)


# --> P E R M U T A T I O N S
# --> Different combintations of the same list

different_combinations = [1, 2, 3]
perm = permutations(different_combinations)
# Use the number of values that you wanna print 
# perm = permutations(different_combinations, 2)


# --> TO FIND MORE INFO ABOUT THE INTERTOOLS YOU JUST NEED TO GOOGLE SEARCH ABOUT "HOW TO USE INTERTOOLS"