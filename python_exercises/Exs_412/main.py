# Main for sol_0412_ex01_tonje.py

from sol_0413_ex01_tonje import Person

def main():

    # initializing the objects
    first_person = Person("Daisy", "Duck", 1990)
    second_person = Person("Tom", "Cat", 1994, 12341234)
    third_person = Person("Jerry", "Mouse", 1994, domain="gmail.com")

    # testing object methods
    print(first_person.full_name(), first_person.age(), first_person.birthyear)
    print(second_person.full_name(), second_person.age(), second_person.birthyear)
    print(third_person.full_name(), third_person.age(), third_person.birthyear)
    print()

    print(first_person.get_email())
    print(second_person.get_phone())
    print(third_person.get_email())
    print()

    # testing help and dir
    print(help(Person.age))
    print(dir(Person))
    print()

    # changing object variables the wrong way
    first_person.first_name = "Donald"
    first_person.last_name = "Goose"
    first_person.birthyear = 1980
    first_person.domain = "yahoo.com"
    print(first_person.full_name, first_person.age(), first_person.birthyear, first_person.domain)
    print(first_person.get_email())
    print()

    # testing the __repr__ -method
    print(second_person)
    print(first_person)

    # testing using property for the email variable / getter
    print(first_person.email)



if __name__== "__main__":
    main()