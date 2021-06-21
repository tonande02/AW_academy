# The class 'Person'
# NB: I've been running my code in main, see bottom of file and un-comment to
# run program from this file

import datetime

class Person(object):

    default_domain = "online.com"

    def __init__(self, first_name, last_name, birthyear, phone=None, domain=default_domain):
        self.first_name = first_name
        self.last_name = last_name
        self.birthyear = birthyear
        self.phone_nr = f"0047{phone}"
        self.domain = domain
        self.email = f"{self.first_name}.{self.last_name}@{self.domain}"
    
    
    def age(self):
        """
        Args: self
        Return: person-object's age using datetime
        """

        now = datetime.datetime.now()
        return now.year - self.birthyear

    
    def full_name(self):
        """
        Args: self
        Return: person-object's full name from its first and last name variables
        """

        return f"{self.first_name} {self.last_name}"
    

    def get_email(self):
        """
        Args: self
        Return: person-object's email adress
        """

        return self.email
    

    def get_phone(self):
        """
        Args: self
        Return: person-object's phone-variable
        """

        return self.phone_nr


## initializing the objects
# first_person = Person("Daisy", "Duck", 1990)
# second_person = Person("Tom", "Cat", 1994, 12341234)
# third_person = Person("Jerry", "Mouse", 1994, domain="gmail.com")

## testing object methods
# print(first_person.full_name(), first_person.age(), first_person.birthyear)
# print(second_person.full_name(), second_person.age(), second_person.birthyear)
# print(third_person.full_name(), third_person.age(), third_person.birthyear)
# print()

# print(first_person.get_email())
# print(second_person.get_phone())
# print(third_person.get_email())
# print()

## testing help and dir
# print(help(Person.age))
# print(dir(Person))