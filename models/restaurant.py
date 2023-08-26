from review import Review

class Restaurant:
    def __init__(self, name):
        """
        Initializes name, as a string
        """
        self.__name = name

    def name(self):
        return self.__name

    def reviews(self):
        """
            Returns a list of all reviews for that restaurant
        """
        return [review for review in Review.reviews if review.restaurant.name() == self.__name]
    
    def customers(self):
        """
            Returns a **unique** list of all customers who have reviewed a particular restaurant
        """
        unique_customer_names = set(
            [review.customer.full_name() for review in self.reviews()])
        unique_customers = [
            review.customer for review in self.reviews if review.customer.full_name() in unique_customer_names
        ]
        return unique_customers
    
    def average_star_rating(self):
        """
            returns the average star rating for a restaurant based on its reviews
            Reminder: you can calculate the average by adding up all the ratings 
            and dividing by the number of ratings
        """
        restaurant_reviews = self.reviews()
        average = sum(
            [review.rating for review in restaurant_reviews]
        ) / len(restaurant_reviews)
        return average

    