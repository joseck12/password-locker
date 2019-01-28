import unittest # Importing the unittest module
# import pyperclip
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

        self.assertEqual(self.new_User.account,"Tweeter")
        self.assertEqual(self.new_user.username,"Mercy")
        self.assertEqual(self.new_user.password,"0000")
#
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


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
            self.new_user.save_user()
            test_user = User("Tweeter", "Mercy", "0000") # new user
            test_user.user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),

    def test_find_user_by_account(self):
        '''
        test to check if we can find a user by account and display information
        '''

            self.new_user.save_user()
            test_user = User("Tweeter", "Mercy", "0000") # new user
            test_user.user()

        found_user = User.find_by_account("Tweeter")

        self.assertEqual(found_user.username,test_user.username)


    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("Tweeter", "Mercy", "0000")
        test_user.save_user()

        user_exists = User.user_exist("Tweeter")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

      def test_copy_username(self):
        '''
        Test to confirm that we are copying the username from a found user
        '''

        self.new_user.save_user()
        User.copy_username("Mercy")

        self.assertEqual(self.new_user.username,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
