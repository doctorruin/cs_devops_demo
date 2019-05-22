# Hello World example to implement DevOps tools
#

def print_string():

    """
    Print String to console
    :return:
    """

    message = create_string()

    print(message)


def create_string():

    """
    Creates String and returns it
    :return:
    """
    message = "Hello, ClearShark!"

    return message


if __name__ == '__main__':
    print_string()
