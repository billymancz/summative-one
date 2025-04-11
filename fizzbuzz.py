def fizzbuzz(n):
    if n % 4 == 0 and n % 8 == 0:
        return "FizzBuzz"
    elif n % 9 == 0:
        return "Fizz"
    elif n % 7 == 0:
        return "Buzz"
    else:
        return str(n)

if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))