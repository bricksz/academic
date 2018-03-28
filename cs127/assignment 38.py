#terry huang
#3/27/2018
#assignment 38

def monthString(monthNum):
    """
    Takes as input a number, monthNum, and
    returns the corresponding month name as a string.
    Example: monthString(1) returns "January".
    Assumes that input is an integer ranging from 1 to 12
    """

    #monthString = ""
    if monthNum == 1:
        return 'January'
    elif monthNum == 2:
        return 'February'
    elif monthNum == 3:
        return 'March'
    elif monthNum == 4:
        return 'April'
    elif monthNum == 5:
        return 'May'
    elif monthNum == 6:
        return 'June'
    elif monthNum == 7:
        return 'July'
    elif monthNum == 8:
        return 'August'
    elif monthNum == 9:
        return 'September'
    elif monthNum == 10:
        return 'October'
    elif monthNum == 11:
        return 'November'
    else:
        return 'December'

def main():
    n = int(input('Enter the number of the month: '))
    mString = monthString(n)
    print('The month is', mString)


# Allow script to be run directly:
if __name__ == "__main__":
    main()