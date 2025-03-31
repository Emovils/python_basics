start = int(input("enter a starting number: "))
end = int(input("enter a ending number: "))
print("even number in range: ")
for num in range(start, end +1):
    if num % 2 == 0:
        print(num)
    
