 # This is a guess the number game.
import random
import compy


def main(sc):

    sc.printf('Well, I am thinking of a number between 1 and 20.')
    sc.printf()

    number = random.randint(1, 20)
    num_guesses_taken = 0
    while True:
        guess = sc.input('Take a guess: ')
        guess = int(guess)
        num_guesses_taken = num_guesses_taken + 1
        if guess < number:
            sc.printf('Your guess is too low.')

        elif guess > number:
            sc.printf('Your guess is too high.')

        elif guess == number:
            sc.printf()
            msg = 'Good job! You guessed my number in {} guesses!'.format(num_guesses_taken)
            sc.printf(msg)
            break
        else:
            pass # Don't do anything

        sc.printf()

        if num_guesses_taken == 5:
            msg='Nope. The number I was thinking of was {}'.format(number)
            sc.printf(msg)
            break


compy.run(main)


