number = 18

print("Guess a number, you have three guesses")
guess = int(input())
count = 0
if guess < 1:
    print("Your guess need to be within 1 - 20")
elif guess < number:
        print("That is too low")
elif guess > 20:
    print("Your guess need to be within 1 - 20")
elif guess > number:
    print("That is too high")
else:
    print("That is the correct number")




