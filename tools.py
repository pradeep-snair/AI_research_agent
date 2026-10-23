#Tools need for the AI chat agent. 
import os
import string
import secrets 

from datetime import datetime
from random import randint


def get_time():

    return datetime.now().strftime("%d-%m-%y %I:%M:%S %p")    

def roll_dice():

    return randint(1,6)

def generate_password(length=12):

    passwd_seed=string.ascii_letters+string.punctuation+string.digits
    password = ""
    for _ in range(length):
        password+= secrets.choice(passwd_seed)
    return password

def read_file(file_name):
    try:
        with open(file_name, 'r')  as f:
            return f.read()
    except FileNotFoundError:
        return ("Error: File Not Found")