def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz")
         else:
            print(x)
