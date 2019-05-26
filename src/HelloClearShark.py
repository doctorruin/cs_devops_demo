# Hello World example to implement DevOps tools
# author: Randolph Abeyta


def print_string():

    """

    Print String to console

    """

    # Retrieve string and place it in var
    message = clearshark_string()

    # Prints string to console
    print(message)


def clearshark_string():

    """

    Creates String and returns it

    :return:
        String

    """

    # Instantiate string variable
    message = "Hello, ClearShark!"

    # Returns var message
    return message


if __name__ == '__main__':
    print_string()
