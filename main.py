try:
    answer = 10/0
    number= input("Enter a number:")
    print(int(number))
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

    