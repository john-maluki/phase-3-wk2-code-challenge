from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review

class TestReview:
    def test_review_instance_created_successfully(self):
        """
            Test instance can be created successfully
        """
        customer = Customer("John", "Doe")
        restaurant = Restaurant("sarova")
        review = Review(customer, restaurant, rating=5)

        assert review != None
        assert review.restaurant() == restaurant
        assert review.customer() == customer
        assert review.rating() == 5
        assert Review.all()[-1] == review

    def test_rating(self):
        """
            Test returns ratings
        """
        review = self.__create_one_review_obj()

        assert review.rating() == 5

    def test_customer(self):
        """
            Test returns customer
        """
        review = self.__create_one_review_obj()

        assert review.customer().full_name() == "John Doe"

    def test_restaurant(self):
        """
            Test returns restaurant
        """
        review = self.__create_one_review_obj()

        assert review.restaurant().name() == "sarova"

    def test_class_method_all(self):
        """
            Test all includes review on creation
        """
        review = self.__create_one_review_obj()

        assert Review.all()[-1] == review

    def __create_one_review_obj(self):
        customer = Customer("John", "Doe")
        restaurant = Restaurant("sarova")
        review = Review(customer, restaurant, rating=5)
        return review