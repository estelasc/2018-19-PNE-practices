print("Program for adding numbers from 1 to a number introduced.")

def sum(n):

    sum_nums = 0

    for num in range(n):
        sum_nums = sum_nums + num + 1

    return sum_nums

# Main Program.
not_error = True
while not_error:
    try:
        selection = int(input("Please, introduce a valid integer number: "))
        total_sum = sum(selection)
        print("The total sum is: {}".format(total_sum))
        not_error = False
    except ValueError:
        print("You have not introduced a number. Try again.")
    except Exception:
        print("Something is wrong. Try again.")