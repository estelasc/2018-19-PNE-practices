print("Program for calculating the sum of the n first numbers of the fibonacci series.")

def fibonacci(n):
    serie_fibonacci = [0, 1]

    for element in serie_fibonacci:
        new_elem = serie_fibonacci[len(serie_fibonacci) - 1] + serie_fibonacci[len(serie_fibonacci) - 2]
        if len(serie_fibonacci) <= n:
            serie_fibonacci.append(new_elem)

    return serie_fibonacci[n-1]

def sum_fibonacci(n):
    tot_sum = 0
    for i in range(n):
        tot_sum = fibonacci(i+1) + tot_sum
    return tot_sum

not_error = True
while not_error:
    try:
        choose_term = int(input("Enter a valid integer: "))  # Choose an index in order to sum the numbers from 1 to the number in this position in the fibonacci series.
        my_sol = sum_fibonacci(choose_term)
        print("The total sum is: {}".format(my_sol))
        not_error = False
    except ValueError:
        print("You have not entered a number. Try again.")
    except Exception:
        print("Something is wrong. Try again.")