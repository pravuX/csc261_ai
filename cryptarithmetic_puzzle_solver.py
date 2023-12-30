# adapted from
# https://stackoverflow.com/a/35976872
import itertools
from json import dumps


def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def solve(equation):
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    left = left.split('+')
    # create list of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    first_letters = set(word[0] for word in left)
    first_letters.add(right[0])

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        # mapping of integers to characters
        sol = dict(zip(letters, perm))

        # to make sure the first letter is never 0
        first_letter_is_zero = False
        for letter in first_letters:
            if sol[letter] == 0:
                first_letter_is_zero = True
                break
        if first_letter_is_zero:
            continue

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(f"Mapping:\n{dumps(sol, indent=4)}")
            print(f"Solution:\n{' + '.join(str(get_value(word, sol)) for word in left)} = {get_value(right, sol)}")
            print(f"{' + '.join(word for word in left)} = {right}")
            # found a solution so break out of the loop
            # remove break if you wish to look for more than one solutions
            break


if __name__ == '__main__':
    solve('SEND + MORE = MONEY')
    solve('TWO + TWO = FOUR')
