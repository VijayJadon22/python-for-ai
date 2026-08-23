
numbers=[3,1,2,7,5,6,1]

#Information
print(len(numbers))
print(numbers.count(1))
print(numbers.index(7))
numbers.sort()
numbers.reverse()

new_list=numbers.copy()
numbers.reverse()
print(numbers)
print(new_list)