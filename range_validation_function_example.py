# Range validation using a function
# Source: https://www.youtube.com/watch?v=817xAvEOEN8

def is_valid_range(input, min_value, max_value):
    '''Function that determines whether the user's input falls within a specified range of values.'''
    # Returns True if the input IS within the specified range of values
    # Returns False if the input IS NOT within the specified range of values

    return len(input) <= max_value and len(input) >= min_value

def show_output(input, min_value, max_value, range_check):
    '''Function that builds and displays the output strings for this project.'''
    print(f'You entered: {input}')
    print(f'Characters in first name: {len(input)}')
    print(f'Minimum acceptable length: {min_value}')
    print(f'Maximum acceptable length: {max_value}')

    if range_check is True:
        print('Congratulations! Length of first name falls within the specified range.')
    else:
        print('Length of first name DOES NOT fall within the specified range!')


min_length = 1
max_length = 5
determination = ''
user_input = input('Please enter your first name: (Example: Mike)\n')
determination = is_valid_range(user_input, min_length,  max_length)
show_output(user_input, min_length, max_length, determination)

