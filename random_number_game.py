import random
secret_num = random.randint(1, 100)
guess = 0
print("Guess a number between 1 and 100.")
while guess != secret_num:
    user_input = input("What is your guess?")
    try:
        int(user_input)
    except (ValueError):
        print("use a NUMBER stoopid!")
        break

    guess = int(user_input)
    if guess > secret_num:
        print("Too high bitch, guess again!")
    elif guess < secret_num:
        print("Too low bitch, guess again!")
print("HOORAY YOU GOT IT bizNATCH!")
print("I learned that at work haha ^ - Sam")
