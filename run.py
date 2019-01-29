#!/usr/bin/env python3.6
from user import User
def create_account(account,username,password):
    '''
    Function to create a new account
    '''
    new_user = User(account,username,password)
    return new_user
    # save users
def save_user(user):
    '''
    Function to save users
    '''
    user.save_user()
    # delete users
def del_user(user):
    '''
    Function to delete a users
    '''
    user.delete_user()
    # finding a user
def find_user(account):
    '''
    Function that finds a user by account and returns the account
    '''
    return User.find_by_account(account)
    # checkif a contact exists
def check_existing_users(account):
    '''
    Function that check if a user exists with that account and return a Boolean
    '''
    return User.user_exist(account)
    # display all users
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def main():
    print("Hello Welcome to Password Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
                    print("Use these short codes : cc - create a new account, dc - display users, fc -find a user, ex -exit the Password Locker")
                    short_code = input('Enter : ').lower()
                    if short_code == 'cc':
                            print("Sign up for Password Locker")
                            your_name = input("Enter username: ")
                            password = input("Enter your password: ")
                            print('\033[94m')
                            print( your_name +" " + " Welcome to password Locker!")
                            print('\033[0m')
                            print("______________ ")
                            print("Which account details would you like to store?")
                            account = input("Account name: ")
                            username = input("What's your username: ")
                            password = input("Enter your password: ")
                            save_user(User(account, username, password)) # create and save new contact.
                            print ('\033[93m \n')
                            print(f"Successful new User {username} stored")
                            print ( '\033[0m \n')

                    elif short_code == 'dc':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.username}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the username you want to search for")

                            search_username = input()
                            if check_existing_users(search_username):
                                    search_user = find_user(search_username)
                                    print(f"{search_user.username}")
                                    print('-' * 20)

                                    # print(f"Phon.......{search_contact.phone_number}")
                                    # print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That user does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    main()
