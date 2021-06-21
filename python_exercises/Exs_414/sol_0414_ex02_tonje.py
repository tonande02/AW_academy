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






## Employee class starts here

class Employee(Person):

    default_domain = "academy.com"

    def __init__(self,  first_name, last_name, birthyear, salary, dom=default_domain):
        super().__init__(first_name, last_name, birthyear, domain=dom)
        self.salary = salary
        self.customers = []
    

    def add_customer(self, customer):
        self.customers.append(customer)
    

    def drop_customers(self):
        self.customers = []
    

    def print_earnings(self):
        earnings = 0

        for customer in self.customers:
            earnings += customer.get_payed_price()
        
        profit = earnings - self.salary

        print(f"{self.full_name}, {self.age()}, {earnings}, {profit}")







cust1 = Customer("Tony", "Stark", 1972, 4000)
cust2 = Customer("Bruce", "Wayne", 1970, 7000)
cust3 = Customer("Diana", "Prince", 1975, 4200)

emp1 = Employee("Peter", "Parker", 1996, 35000)
emp2 = Employee("Barry", "Allen", 1992, 37500)

emp1.add_customer(cust1)
emp2.add_customer(cust2)
emp2.add_customer(cust3)

emp1.print_earnings()
emp2.print_earnings()

# print(emp1)
# print(emp2)
# print(cust1)
# print(cust2)
# print(cust3)
# print(emp1.customers)
# print(emp2.customers)


# emp1.drop_customers()


print(emp1.customers)





