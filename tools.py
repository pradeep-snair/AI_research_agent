#Tools need for the AI chat agent. 
from datetime import datetime
from random import randint
import string
import secrets 

from datetime import datetime
print(datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))
from random import randint
import secrets 
print(randint(1,6))
import string 

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
    