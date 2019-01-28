import unittest # Importing the unittest module
import random
from user import User # Importing the user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Tweeter", "Mercy", "0000") # create user object

        def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.account,"Tweeter")
        self.assertEqual(self.new_user.username,"Mercy")
        self.assertEqual(self.new_user.password,"0000")

        def test_save_multiple_user(self):
            '''
            test_save_multiple_contact to check if we can save multiple user
            objects to our contact_list
            '''
            self.new_user.save_user()
            test_user = UserUser("Tweeter", "Mercy", "0000") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    if __name__ == '__main__':
    unittest.main()
