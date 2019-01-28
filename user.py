class User:

    user_list = []

    def __init__(self,account,username,password):

     def save_user(self):

            '''
            save_user method saves user objects into user_list
            '''

            User.user_list.append(self)

            self.account = account
            self.username = username
            self.password = password
