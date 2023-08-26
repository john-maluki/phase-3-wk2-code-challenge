from review import Review

class Customer:
    customers = []
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
    
    def restaurants(self):
        """
            Returns a **unique** list of all restaurants a customer has reviewed
        """
        customer_reviews = self.__get_customer_reviews()
        unique_restaurant_names = set([review.restaurant.name for review in customer_reviews])
        unique_restaurant = [review.restaurant for review in customer_reviews if review.restaurant.name in unique_restaurant_names]
        return unique_restaurant
    
    def add_review(self, restaurant, rating):
        """
            Given a **restaurant object** and a star rating 
            (as an integer), creates a new review and associates 
            it with that customer and restaurant.
        """
        Review(self, restaurant, rating)

    def num_reviews(self):
        """
            Returns the total number of reviews that a customer has authored
        """
        customer_reviews = self.__get_customer_reviews()
        return len(customer_reviews)


    def __get_customer_reviews(self):
        customer_reviews = [review for review in Review.reviews if review.customer.full_name() == self.full_name()]
        return customer_reviews

    @classmethod
    def add_customer(cls, customer):
        cls.all.append(customer)

    @classmethod
    def all(cls):
        return cls.customers
    
    @classmethod
    def find_by_name(cls, name):
        """
            given a string of a **full name**, returns the **first customer** 
            whose full name matches
        """
        found_customer = None
        for customer in cls.customers:
            if customer.full_name() == name:
                found_customer = customer
                break
            
        return found_customer
    
    @classmethod
    def find_all_by_given_name(cls, name):
        """
            given a string of a given name, returns an **list** 
            containing all customers with that given name
        """
        found_customers = []
        for customer in cls.customers:
            if customer.full_name() == name:
                found_customers.append(customer)
            
        return found_customers
