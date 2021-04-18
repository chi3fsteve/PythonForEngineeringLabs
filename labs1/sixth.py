# For a given list of numbers return a list where all
# identical, neighboring numbers are contracted to a
# single number (e.g. [1,2,2,3] [1,2,3])

numbers = [1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 2, 2, 8, 3]
pos_to_remove = []

for i in range(len(numbers)-1):
    if numbers[i] == numbers[i+1]:
        pos_to_remove.append(i)

for j in reversed(pos_to_remove):
    numbers.pop(j)

print(numbers)

