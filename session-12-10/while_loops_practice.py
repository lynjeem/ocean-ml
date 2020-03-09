
# 1. Use a while loop to print numbers 1-10:

# 2. Use a while loop to print the first 10 multiples of 24:

# 3. Use a while loop to find the average of these numbers:
numbers = [10,42,-2, 900,5,8,39]
print(numbers[1])
i = 0
total = 0

while i < len(numbers):
	total += numbers[i]
	i+=1

print(total)
average = total/len(numbers)

print(average)