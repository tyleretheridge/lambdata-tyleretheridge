
def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return int(n) * 100


if __name__ == "__main__":
    # only run the code below
    # when this script is invoked from the command-line
    # not if it is imported from another script

    x = 5
    print(enlarge(x))
    z = input("Please choose a number to enlarge: ")
    print(enlarge(int(z)))
