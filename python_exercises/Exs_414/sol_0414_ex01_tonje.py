import datetime

class Person(object):

    default_domain = "online.com"

    def __init__(self, first_name, last_name, birthyear, phone=None, domain=default_domain):
        self.first_name = first_name
        self.last_name = last_name
        self.birthyear = birthyear
        self.phone_nr = f"0047{phone}"
        self.domain = domain
    
    
    def age(self):
        """
        Args: self
        Return: person-object's age using datetime
        """

        now = datetime.datetime.now()
        return now.year - self.birthyear

    
    @property   
    def full_name(self):
        """
        Args: self
        Return: person-object's full name from its first and last name variables
        """

        return self.get_full_name()
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@{self.domain}"

    def get_email(self):
        """
        Args: self
        Return: person-object's email adress
        """

        return f"{self.first_name}.{self.last_name}@{self.domain}"
    

    def get_phone(self):
        """
        Args: self
        Return: person-object's phone-variable
        """

        return self.phone_nr

    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}, {self.age()} y/o, born {self.birthyear}, email: {self.get_email()}, phone: {self.get_phone()}")
        # return self.last_name






## Customer class starts here

class Customer(Person):

    default_domain = "online.com"

    def __init__(self,  first_name, last_name, birthyear, full_price):
        super().__init__(first_name, last_name, birthyear)
        self.full_price = full_price
        self.payed_price = 0

    
    def set_payed_price(self):
        age = self.age()
        discount = (self.full_price / 100) * age
        self.payed_price = self.full_price - discount
    
    def get_payed_price(self):
        self.set_payed_price()
        return self.payed_price
        




## Testing the program
cust1 = Customer("Tony", "Stark", 1972, 4000)
cust2 = Customer("Bruce", "Wayne", 1970, 7000)
print(cust1)
# cust1.set_payed_price()
# cust2.set_payed_price()

print(cust1.get_payed_price())
print(cust2.get_payed_price())