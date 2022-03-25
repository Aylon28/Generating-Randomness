def only_0_and_1(lin, text='Print a random string containing 0 or 1:'):
    line_ = input(text)
    for ch in line_:
        if ch == '0' or ch == '1':
            lin += ch
    return lin


def get_start_three():
    return game_line[0] + game_line[1] + game_line[2]


first_line = ''
text_line = ''
prediction_line = ''
game_line = ''
money = 1000
while len(first_line) < 100:
    first_line = only_0_and_1(first_line)
    if len(first_line) < 100:
        print(f"The current data length is {len(first_line)}, {100 - len(first_line)} symbols left")
    print()

print("Final data string:")
print(first_line)
print()

triads = ['000', '001', '010', '011', '100', '101', '110', '111']
the_0s = dict.fromkeys(triads, 0)
the_1s = dict.fromkeys(triads, 0)

for i in range(0, len(first_line) - 3):
    triad = first_line[i] + first_line[i + 1] + first_line[i + 2]
    if int(first_line[i+3]) == 0:
        the_0s[triad] += 1
    else:
        the_1s[triad] += 1

print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
print("Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!", end='\n\n')

print("Print a random string containing 0 or 1:")
svar = input()
while svar != 'enough':
    game_line = ''
    for ch in svar:
        if ch == '0' or ch == '1':
            game_line += ch
    if game_line != '':
        prediction_line = get_start_three()
        i = 0
        while len(prediction_line) != len(game_line):
            triad = game_line[i] + game_line[i + 1] + game_line[i + 2]
            if the_0s[triad] > the_1s[triad]:
                prediction_line += '0'
            else:
                prediction_line += '1'
            i += 1

        total_right = 0
        for i in range(3, len(game_line)):
            if game_line[i] == prediction_line[i]:
                total_right += 1
                money -= 1
            else:
                money += 1
        print("prediction:")
        print(prediction_line, end='\n\n')
        print(f"Computer guessed right {total_right} out of {len(game_line) - 3} symbols ({round(total_right / (len(game_line) - 3) * 100, 2)} %)")
        print("Your balance is now $" + str(money), end='\n\n')
        for i in range(0, len(game_line) - 3):
            triad = game_line[i] + game_line[i + 1] + game_line[i + 2]
            if int(game_line[i + 3]) == 0:
                the_0s[triad] += 1
            else:
                the_1s[triad] += 1
    print("Print a random string containing 0 or 1:")
    svar = input()

print("Game over!")
