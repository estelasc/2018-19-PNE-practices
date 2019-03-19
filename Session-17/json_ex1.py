import json
import termcolor

f = open("PersonEx1.json", 'r')

people = json.load(f)

n_people = len(people)
print("Total people in the database: {}".format(n_people))
print()

for indiv in people:
    termcolor.cprint("Name: ", 'yellow', end='')
    print(indiv['Firstname'], indiv["Lastname"])
    termcolor.cprint("Age: ", 'yellow', end='')
    print(indiv['Age'])

    for num in indiv["Phonenumber"]:
        n_nums = len(indiv["Phonenumber"])
        print("Phone numbers: {} ".format(n_nums))

        termcolor.cprint("      Type: ", 'blue', end='')
        print(num["type"])
        termcolor.cprint("      Number: ", 'blue', end='')
        print(num['number'])
    print()
