import common

def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """


    raw = ""
    dashed_raw = ""
    for j in range(0,len(title_list)):
        dashed_raw += "|"
        raw += "|"
        raw += ("{:^"+str(common.column_length(table, j))+"}").format(title_list[j])
        dashed_raw += "-"*common.column_length(table,j)
    dashed_raw += "|"
    raw += "|"
    raw_length = len(raw)
    print("/" + "-"*(raw_length-2) + "\\")
    print(raw)

    raw = ""
    for i in range(0,len(table)):
        print(dashed_raw)
        for j in range(0,len(title_list)):
            raw += "|"
            raw += ("{:^"+str(common.column_length(table, j))+"}").format(table[i][j])


        raw += "|"
        print(raw)
        raw = ""
    print("\\" + "-"*(raw_length-2) + "/")


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result

    Returns:
        This function doesn't return anything it only prints to console.
    """

    

    if type(label) is str:
        print(label)
    elif type(label) is list:
        print(label[len(label)-1])


    if len(result) == 0:
        pass
    elif type(result) is str or type(result) is int or type(result) is float:
        print(result)
    elif type(result) is dict:
        print('')
        for key in result:
            print(key,':',result[key])
    elif type(result) is list:
        print('')
        if type(result[0]) is list:
            result = common.convert_all_elements_to_string(result)
            print_table(result, label[0:len(label)-1])
        else:
            for i in range(0,len(result)):
                print(result[i])

    print('')


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print(title + ":")
    option_number = 1
    for item in list_options:
        print("\t(" + str(option_number) + ") " + item)
        option_number += 1
    print("\t(0) " + exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    for i in range(0,len(list_labels)):
        inputs.append(input(list_labels[i]))

    print("\n"*100)
    return inputs


# This function displays an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    """
    Displays an error message

    Args:
        message(str): error message to be displayed

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print("Error: ", message)
