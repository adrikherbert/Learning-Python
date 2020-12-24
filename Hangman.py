# Hangman -- Adrik Herbert

target_word = input('Enter your Hangman word: ')

while True:
    try:
        wrong = int(input('Enter the number of allowed incorrect guesses: '))
        break
    except ValueError as e:
        print('Invalid Input: please enter an integer')

hangman_word = []
for i in target_word:
    hangman_word.append('_')

solved = False


def guess_filter(current, letter, target):
    temp = current

    for i in range(len(target)):
        if target[i] == letter:
            temp[i] = letter

    return temp


while not solved and wrong > 0:
    print(f'Wrong guesses left: {wrong}\n')
    print(''.join(hangman_word))
    print('\n\n')
    guess = '...'
    while len(guess) != 1:
        guess = input('Enter a guess: ')
        if len(guess) != 1:
            print('Invalid Input: enter a single character')

    if guess in target_word:
        hangman_word = guess_filter(hangman_word, guess, target_word)
    else:
        wrong -= 1
