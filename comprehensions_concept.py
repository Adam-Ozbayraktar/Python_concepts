# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)

# Dictionary comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# I want a dict{'name': 'hero'} for each name,hero in zip(names,hero)

my_dict = {name: hero for name, hero in zip(names,heros)}
print(my_dict)

# Set comprehension (a set is a list with all unique values)
nums = [1,1,2,1,3,4,3,4,5,5,6,7,7,8,9,9,5]

# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

my_set = {n for n in nums}
print(my_set)

# Generator expressions
# I want to yield 'n*n' for each n in nums

nums = [n for n in range(10)]

# def gen_func(nums):
#     for n in nums:
#         yield n*n
#
# my_gen = gen_func(nums)
#
# for i in my_gen:
#     print(i)

my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)
