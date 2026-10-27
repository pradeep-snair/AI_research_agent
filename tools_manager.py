from tools import (
    generate_password, 
    get_time,
    roll_dice,
    read_file
)

def execute_tool(user_input):
    user_input = user_input.lower()
    if 'time' in user_input or 'clock' in user_input:
        return get_time()
    elif 'roll dice' in user_input or 'dice' in user_input \
    or 'die' in user_input:
        return roll_dice()
    elif 'password' in user_input:
        return generate_password()
    else:
        return None

if __name__ == "__main__":

    print(execute_tool('time')) 
