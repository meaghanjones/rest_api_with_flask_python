#create list programmatically
my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)

print(8 % 3)
#we care if we want to know if a number is odd or even

print(9 % 2) # 4 % 2 == 0, 5 % 2 == 1 so we know which is odd and even

print([n for n in range(10) if n % 2 == 0])

people_you_know = ["Anna", "Chris", "Greg"]
normalised_people = [person.strip().lower() for person in people_you_know]
print(normalised_people)
