class Review:
    reviews = []
    def __init__(self, customer, restaurant, rating):
        """
        initializes customer, restaurant, and a rating (a number)
        """
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

        Review.__add_reviev(self)

    def rating(self):
        return self.rating
    
    @classmethod
    def all(cls):
        return cls.reviews
    
    @classmethod
    def __add_reviev(cls, review):
        cls.reviews.append(review)
