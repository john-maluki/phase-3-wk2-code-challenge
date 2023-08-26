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
        reviews = [review for review in Review.reviews if review.customer.full_name() == self.full_name()]
        unique_restaurant_names = set([review.restaurant.name for review in reviews])
        unique_restaurant = [review.restaurant for review in reviews if review.restaurant.name in unique_restaurant_names]
        return unique_restaurant
    
    def add_review(self, restaurant, rating):
        """
            Given a **restaurant object** and a star rating 
            (as an integer), creates a new review and associates 
            it with that customer and restaurant.
        """
        Review(self, restaurant, rating)

    @classmethod
    def add_customer(cls, customer):
        cls.all.append(customer)

    @classmethod
    def all(cls):
        return cls.customers

    