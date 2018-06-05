# implement commonly used functions here

import random



# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):


    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
               'r','s','t','u','w','x','y','z']
    generated = ''

    while(not len(generated)):
        generated += letters[random.randrange(0,len(letters))].lower()
        generated += letters[random.randrange(0,len(letters))].upper()
        generated += str(random.randrange(0,10))
        generated += str(random.randrange(0,10))
        generated += letters[random.randrange(0,len(letters))].upper()
        generated += letters[random.randrange(0,len(letters))].lower()
        generated += "#&"

        for i in range(0,len(table)):
            if table[i][0] == generated:
                generated = ''



    return generated


def column_length(table, column_number):
    length = 0
    for i in range(0,len(table)):
        if len(table[i][column_number]) > length:
            length = len(table[i][column_number])
    if length < 15:
        return 15
    else:
        return length


def alphabetical_sorting(string_list):
    for i in range(len(string_list)-1, 0, -1):
        for j in range(0,i):
            if string_list[j].upper() > string_list[j+1].upper():
                string_list[j], string_list[j+1] = string_list[j+1], string_list[j]

    return string_list


def find_index_by_name(table,name):
    for i in range(0,len(table)):
        if table[i] == name:
            return i


def convert_all_elements_to_string(table):
    for i in range(0,len(table)):
        for j in range(0,len(table[i])):
            table[i][j] = str(table[i][j])
    return table