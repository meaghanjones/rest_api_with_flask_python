#should_continue = True
#if should_continue:
    #print("Hello")

# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")
#
# if person in known_people:
#     print("You know {}!".format(person))
#
# else:
#     print("You don't know {}".format(person))

## Exercise

def who_do_you_know():
    #ask the user for a list of people they know
    people_without_spaces = [person.strip().lower() for person in input("Enter the name of people you know separated by commas:").split(',')]

    return people_without_spaces


def ask_user():
    #ask user for their name
    person = input("Enter a name of someone you know:")
    if person in who_do_you_know():
        print("You know {}!".format(person))

ask_user()
