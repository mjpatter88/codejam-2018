import math
import sys

correct = "CORRECT"
too_small = "TOO_SMALL"
too_big = "TOO_BIG"



def main():
    num_cases = input()

    for case in range(int(num_cases)):
        line = input()
        a, b = line.split()
        a = int(a)
        b = int(b)
        max_guesses = int(input())

        done = False
        lower = a # Lower is exclusive
        upper = b # Upper is inclusive
        while not done:
            guess = calc_guess(lower, upper)
            print(guess)
            sys.stdout.flush()
            response = input()
            if response == correct:
                done = True
            elif response == too_small:
                lower = guess
            elif response == too_big:
                upper = guess - 1
            else:
                assert False, response

def calc_guess(lower, upper):
    return lower + math.ceil((upper - lower) / 2)

if __name__ == "__main__":
    main()
