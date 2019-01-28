#!/usr/bin/env python3.6
from user import User

 def create_account(account,username,password):
    '''
    Function to create a new account
    '''
    new_user = Username(account,username,password)
    return new_user
    # save users
def save_users(user):
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
