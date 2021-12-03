def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'fizz buzz'
    if num % 3 == 0 :
        return 'fizz'
    if num % 5 == 0:
        return 'buzz'
    else:
        return num
