def fizz_buzz(number):
    if number == 0:
        return str(number)
    elif number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

def list_sequence(number):
    result = []
    for i in range(number + 1):
        result.append(fizz_buzz(i))
    return result