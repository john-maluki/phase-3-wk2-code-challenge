class Customer:
    all = []
    def __init__(self, first_name, last_name):
        """
            Initialized customer with a given name (first_name) 
            and family name(last_name)
        """
        self.first_name = first_name
        self.last_name = last_name

        Customer.add_customer(self)

    def given_name(self):
        """
        Returns the Customer name
        """
        return self.first_name
    
    def set_first_name(self, first_name):
        self.first_name = first_name

    def family_name(self):
        return self.last_name
    
    def set_family_name(self, last_name):
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}" 

    @classmethod
    def add_customer(cls, customer):
        cls.all.append(customer)

    