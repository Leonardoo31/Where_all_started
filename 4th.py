
#fizz buzz
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizzbuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "buzz"
    return input

print(fizz_buzz(int(input("say a number: "))))
