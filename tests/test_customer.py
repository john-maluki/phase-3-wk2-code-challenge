from models.customer import Customer
from models.review import Review
from models.restaurant import Restaurant
class TestCustomer:
    
    def test_creating_customer(self):
        """
            Test customer object is created successfully
        """
        customer = Customer("John", "Doe")
        assert customer != None
        assert customer.first_name == "John"
        assert customer.last_name == "Doe"
        assert Customer.customers == [customer]

    def test_all(self):
        """
            Test all() method return 3 instances of classes
        """
        # the first instances has been created on the above test
        Customer("John", "Doe")
        Customer("John2", "Doe2")
        assert len(Customer.all()) == 3

    def test_full_name(self):
        """
            Test full_name return full name
        """
        customer = Customer("John", "Doe")
        assert customer.full_name() == "John Doe"

    def test_given_name(self):
        """
        Test returns first name
        """
        customer = Customer("John", "Doe")
        assert customer.given_name() == "John"

    def test_set_given_name(self):
        """
        Test updating first name
        """
        customer = Customer("John", "Doe")
        customer.set_given_name("John1")
        assert customer.given_name() == "John1"

    def test_family_name(self):
        """
        Test returns last name
        """
        customer = Customer("John", "Doe")
        assert customer.family_name() == "Doe"

    def test_set_family_name(self):
        """
        Test updates last name
        """
        customer = Customer("John", "Doe")
        customer.set_family_name("Doe1")
        assert customer.family_name() == "Doe1"

    def test_find_by_name(self):
        """
            Test given a string of a **full name**, returns the **first customer** 
            whose full name matches
        """
        customer1 = Customer("Jack", "Chank")
        customer2 = Customer("Jack", "Chank")
        
        found_customer = Customer.find_by_name("Jack Chank")
        assert found_customer == customer1
        assert found_customer != customer2

    def test_find_all_by_given_name(self):
        """
            Test given a string of a given name, returns an **list** 
            containing all customers with that given name
        """
        customer1 = Customer("Jack1", "Chank")
        customer2 = Customer("Jack1", "Chank")
        
        found_customers = Customer.find_all_by_given_name("Jack1 Chank")
        assert type(found_customers) is list
        assert len(found_customers) == 2
        assert found_customers == [customer1, customer2]

    def test_num_reviews(self):
        """
            Test returns the total number of reviews that a customer has authored
        """
        customer = Customer("Jack3", "Chank")
        restaurant = Restaurant("sarova")
        restaurant2 = Restaurant("sarova1")
        review1 = Review(customer, restaurant, 5)
        review2 = Review(customer, restaurant2, 7)

        assert customer.num_reviews() == 2
        assert Review.all() == [review1, review2]

    def test_add_review(self):
        """
            Test given a **restaurant object** and a star rating 
            (as an integer), creates a new review and associates 
            it with that customer and restaurant.
        """
        customer = Customer("Jack4", "Chank")
        restaurant = Restaurant("hilton")

        customer.add_review(restaurant, 10)

        assert customer.num_reviews() == 1
        assert len(Review.all()) == 3 # one plus two above

    def test_restaurants(self):
        """
            Test returns a **unique** list of all restaurants a customer has reviewed
        """
        customer = Customer("Jeff", "Chank")
        arestaurant = Restaurant("aee")
        arestaurant1 = Restaurant("aee")
        brestaurant = Restaurant("bee")
        crestaurant = Restaurant("dee")
        drestaurant = Restaurant("cee")
        drestaurant1 = Restaurant("cee")

        customer.add_review(arestaurant, 10)
        customer.add_review(arestaurant1, 8)
        customer.add_review(brestaurant, 10)
        customer.add_review(crestaurant, 6)
        customer.add_review(drestaurant, 9)
        customer.add_review(drestaurant1, 5)

        assert len(customer.restaurants()) == 4





        




