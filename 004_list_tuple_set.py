fruit = ["apple", "banana", "cherry", "date", "fig"]
B= [5, 3, 8, 1, 9,2]
print("fruit:")
print("B")
print(len("fruit"))
print(fruit[0:-1])
print(B[1:5])
fruit.append("grape")
print("fruit")
fruit.insert(2, "orange")
B.extend([10, 11, 12])
print("B")
fruit.remove("banana")
print(fruit)
B.pop(2)
print(B)
fruit.reverse()
print("reversed fruit:")
B.sort()
print("sorted B:", B)
B.sort(reverse=True)
print("sorted B (descending):", B)
print("min:", min(B))
print("max:", max(B))
print("sum:", sum(B))
print("index of cherry:", fruit.index("cherry"))
print("is fig in fruit?", "fig" in fruit)
print("items in B:")
for num in B:
    print(num)
print("fruit with indexes:") 
for index, item in enumerate(fruit):
    print(f"{index}:{item}")
joined_fruit = "-". join(fruit)
print("joined fruit:", joined_fruit)
fruit ="apple-banana-cherry-date".split("-")
print("fruit:", fruit)
