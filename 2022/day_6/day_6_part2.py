'''6_day'''

def find_repetition(text_window):
    letter_index = 0
    for letter in text_window[:-1]:
        letter_index += 1
        if letter in text_window[letter_index:]:
            return True
    return False

file = 'input_part2.txt'

with open(file) as f:
    text = f.read()
start_letter = -1
badge_found = None
for letter_index in range(14 , len(text)):
    start_letter += 1
    window = text[start_letter:letter_index]
    repetition = find_repetition(window)
    
    if not repetition:
        badge_found = window
        break
    
print(f"The result is: {letter_index}")
