def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

#print(methodception(add_two_numbers))
#print(methodception(lambda: 35 + 77))

#functional programming - useful when we want to work with dat
#filter is more fimiliar to ppl who program in other languages
my_list = [13, 56, 77, 484]
print(list(filter(lambda x: x != 13, my_list)))

#you dont have to use lambda
def not_thirteen(x):
    return x != 13

print(list(filter(not_thirteen, my_list)))

#performace wise this might be faster
#up to your prefrences
#this is called list comprehensions
print([x for x in my_list if x != 13])
