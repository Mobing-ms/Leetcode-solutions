import math

lists = []

n = int(input("Enter number of elements in the list: "))

for i in range(n):
    lists.append(int(input(f"Enter the element {i+1}:")))

print("\n\n")
print(f"Original list: {lists}\n")

new_sqrlist = [
    d**2
    for d in lists
    if d % 2 == 0
]
print(f"Squared list of even numbers: {new_sqrlist}\n")

new_cubelist = list(map(lambda x: x**3,lists))
print(f"Cubed list: {new_cubelist}\n")

new_filteredlist = list(filter(lambda x: x > 20000,new_cubelist))
print(f"Filtered list of cubes greater than 20000: {new_filteredlist}\n")

sumlist = sum(new_filteredlist)
print(f"Sum of the filtered list: {sumlist}\n")