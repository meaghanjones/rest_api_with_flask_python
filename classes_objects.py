lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}
#dictionary can't do stuff with it's own numbers
#sum(lottery_player_dict['numbers'].total())

class LotteryPlayer:
    def __init__(self):
        self.name = "Rolf",
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer()
player_two = LotteryPlayer()

#print(player_one == player_two) #false: they are not the same but they share the same signiture
#print(player_one.name == player_two.name) #this is true, but they are different instances of self

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @staticmethod
    def go_to_school():
        print("I'm going to school.")

anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)
Student.go_to_school()
print(anna.average())
#print(anna.marks)
