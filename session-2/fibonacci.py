print("Program that calculates the nth term of the fibonacci series. ")


def fibonacci(n):
    serie_fibonacci = [0, 1]

    for element in serie_fibonacci:
        new_elem = serie_fibonacci[len(serie_fibonacci) - 1] + serie_fibonacci[len(serie_fibonacci) - 2]
        if len(serie_fibonacci) <= n:  # In order to avoid creating an infinite series (my computer fails if I do it)
            serie_fibonacci.append(new_elem)

    return serie_fibonacci[n-1]


# main
not_error = True
while not_error:
    try:
        choose_num = int(input("Enter a valid integer: "))
        if choose_num < 1:
            print("The integer entered must be greater or equal to 1. Try again.")
        else:
            solution = fibonacci(choose_num)
            print("The term of the fibonacci series in that position is: {}".format(solution))
            not_error = False
    except ValueError:
        print("You have not entered a number. Try again.")
    except Exception:
        print("Something is wrong. Try again.")
