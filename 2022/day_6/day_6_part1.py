'''6 day'''

file_name = 'input.txt'

with open(file_name) as file:
    input = file.read()
    text = input[:-1]

    start_1 = 0
    start_2 = 2
    char_in_window = 4
    badge = ''
    badge_found = False
    while not badge_found:
        letter_pair_1 = text[start_1: start_2]
        letter_pair_2 = text[start_2 : char_in_window]
        same_1_letters = letter_pair_1[0] == letter_pair_1[1]
        same_2_letters = letter_pair_2[0] == letter_pair_2[1]
        letter_in_pairs =  letter_pair_1[0] in letter_pair_2 or letter_pair_1[1] in letter_pair_2

        if same_1_letters or same_2_letters or letter_in_pairs:
            start_1 += 1
            start_2 += 1 
            char_in_window += 1
        else:
            badge = letter_pair_1 + letter_pair_2
            badge_found = True
            break         
print(badge, start_2 + 2)
