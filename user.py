class User:

    user_list = []

    def __init__(self,account,username,password):
        self.account = account
        self.username = username
        self.password = password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in an account and returns a user that matches that account.
        '''

        for user in cls.user_list:
            if user.account == account:
                return user
    @classmethod
    def user_exist(cls,account):
        '''
        Method that checks if a user exists from the user list.
        Arg:
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.account == account:
                    return True

        return False
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_username(cls,account):
        user_found = User.find_by_username(username)
        pyperclip.copy(user_found.username)
