##3 Rucksack Reorganization

file_name = 'all_ruksaks_badges.txt'

with open(file_name) as file:
    text = file.read()
all_rucksaks = text.split()

badge_items = []
for start in range(0, len(all_rucksaks), 3):
    for letter in all_rucksaks[start]:
        if letter in all_rucksaks[start + 1] and letter in all_rucksaks[start + 2]:
            badge_items.append(letter)
            break

priority_sum = 0
for badge in badge_items:
    if badge.isupper():
        priority = ord(badge) - 38 
    else:
        priority = ord(badge) - 96
    priority_sum += priority 

print(f'sum of prioroties is:{priority_sum}')
