

strs = input().split()
numbers = list(map(int, strs))
sum_of_positives = sum(x for x in numbers if x > 0)
print(sum_of_positives)