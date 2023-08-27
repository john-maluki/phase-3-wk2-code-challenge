from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review

class TestRestaurant:

    def test_restaurant_instance_created_successfully(self):
        """
            Test restaurant instance can be created successfully
        """
        # customer = Customer("John", "Doe")
        restaurant = Restaurant("dubo")
        # review = Review(customer, restaurant, rating=6)

        assert restaurant != None
        assert restaurant.name() == "dubo"

    def test_name(self):
        """
            Test returns name
        """
        restaurant = Restaurant("dabo")

        assert restaurant.name() == "dabo"

    def test_reviews(self):
        """
            Test returns a list of all reviews for that restaurant
        """
        restaurant = self.__create_reviews_for_restaurant()

        assert len(restaurant.reviews()) == 8

    def test_customers(self):
        """
            Test returns a **unique** list of all customers who have reviewed a particular restaurant
        """
        restaurant = self.__create_reviews_for_restaurant()

        assert len(restaurant.customers()) == 8

    def test_average_star_rating(self):
        """
            Tests returns the average star rating for a restaurant based on its reviews
            Reminder: you can calculate the average by adding up all the ratings 
            and dividing by the number of ratings
        """

        restaurant = self.__create_reviews_for_restaurant()
        assert restaurant.average_star_rating() == 3.75
        


    def __create_reviews_for_restaurant(self):
        customer1 = Customer("John1", "Doe")
        customer2 = Customer("John2", "Doe")
        customer3 = Customer("John3", "Doe")
        customer4 = Customer("John4", "Doe")
        restaurant1 = Restaurant("dubo")
        restaurant2 = Restaurant("dabo")
        restaurant3 = Restaurant("dibo")

        Review(customer1, restaurant1, rating=5)
        Review(customer2, restaurant1, rating=4)
        Review(customer3, restaurant1, rating=2)
        Review(customer4, restaurant1, rating=4)

        Review(customer1, restaurant1, rating=5)
        Review(customer2, restaurant1, rating=4)
        Review(customer3, restaurant1, rating=2)
        Review(customer4, restaurant1, rating=4)

        Review(customer1, restaurant2, rating=5)
        Review(customer2, restaurant2, rating=6)
        Review(customer3, restaurant2, rating=2)
        Review(customer4, restaurant2, rating=4)

        Review(customer1, restaurant3, rating=5)
        Review(customer2, restaurant3, rating=6)
        Review(customer3, restaurant3, rating=2)
        Review(customer4, restaurant3, rating=4)

        return restaurant1