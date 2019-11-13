# This is the driver for Person.py

from Person import Person

markhus = Person("Markhus", "Dammar", 18, "Brown", 145)

print("Let's learn about the creator of this program!")
input("\nPress ENTER to continue")
print("\nThe creator's first name is " + markhus.first)
input("\nPress ENTER to continue")
print("\n" + markhus.first + "'s last name is " + markhus.last)
input("\nPress ENTER to continue")
date = input("\nIs today April 9th? (Y/N) >>>")
if date == "Y" or date == "yes" or date == "Yes" or date == "y":
    markhus.birthday()
    print("\n" + markhus.first + " is " + str(markhus.age) + " years old today!")
    print("Be sure to wish him a happy birthday!")
else:
    print("\n" + markhus.first + " is " + str(markhus.age) + " years old")
input("\nPress ENTER to continue")
print("\n" + markhus.first + " has " + markhus.eye + " colored eyes.")
input("\nPress ENTER to continue")
exercise = input(f"\nHas {markhus.first} been working out? (Y/N) >>>")
if date == "Y" or date == "yes" or date == "Yes" or date == "y":
    print("\nLast time he weighed himself, " + markhus.first + " weighs " + str(markhus.weight) + " pounds.")
else:
    markhus.workout()
    print("\n" + markhus.first + " weighs " + str(markhus.weight) + " pounds. He needs to hit the gym.")
input("\nPress ENTER to continue")
print("\nThanks for taking time to learn about " + markhus.first + " " + markhus.last)
exit()
