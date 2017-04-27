my_variable = "hello"

grades = [77, 89, 90, 95]#lists are ordered in the order that we wrote them
tuple_grades = (77, 80, 90) #immutable
set_grades = {77, 80, 99} #unique and unordered

#print(sum(grades) / len(grades))
#print(set_grades)

#grades.append(100)
#print(grades)

set_grades.add(60)
set_grades.add(60)
#print(set_grades)

##Set operations

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

#print(your_lottery_numbers.intersection(winning_numbers))
#print(your_lottery_numbers.union(winning_numbers))
#print({1,2,3,4}.difference({1, 2}))

#tuple issue if there is only one number you should have a comma after it.
