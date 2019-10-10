import itertools

data = [1, 2, 3, 4, 5]

some_data = list(zip(itertools.count(), data))
print(some_data)

name = list('Madiyor')
# keeps iterating by cycling
counter = itertools.cycle(name)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


# combinations using letters
letters = ['a', 'b', 'c', 'd', 'e']
letters_perm = ['a', 'b', 'c']
numbers = [1, 2]
names = ['Madiyor', 'Mirzashamol']

result = list(itertools.combinations(letters, 3))
result_perm = list(itertools.permutations(letters_perm, len(letters_perm)))
result_product = list(itertools.product(numbers, repeat=4))

# prints all the combinations
print("The result of combinations: ", result)
# prinnts all the permutations
print("The result of permutations: ", result_perm)
print("The result of products with repeat=4 >")
for prod in result_product:
    print(prod)

combined_item = itertools.chain(letters, numbers, names)

for item in combined_item:
    print(item)

