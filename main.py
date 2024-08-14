from operator import truediv

high = 1000
low = 1
print("think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while True:
    guess = low + (high - low) // 2
    hilo = input("My guess is {} should i guess higher or lower? "
                 "\nEnter h for higher l for lower and c if correct: ".format(guess))
    if hilo.casefold() == "c":
        print("Your number is {}\nI got it in {} guesses".format(guess, guesses))
        break
    elif hilo.casefold() == "h":
        low = guess + 1
    elif hilo.casefold() == "l":
        high = guess - 1
    else:
        print("Enter h, l or c")
    if high == low:
        print("Your number is {}\nI got it in {} guesses".format(guess+1, guesses))
        break
    guesses += 1


