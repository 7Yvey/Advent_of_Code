'''Day 4: Camp Cleanup'''

file_name = 'input.txt'

with open(file_name) as file:
    text = file.read()
    text_split = text.split('\n')[:-1]

space_list = []
for line in text_split:
    clean_range = line.split(',')
    for item in clean_range:
        space = item.split('-')
        space_list.append((int(space[0]), int(space[1])))

index = 0
same_assignments = 0
while index < len(space_list):
    elf_1 = space_list[index]
    area_start_1 = elf_1[0]
    area_end_1 = elf_1[1]
    elf_2 = space_list[index + 1]
    area_start_2 = elf_2[0]
    area_end_2 = elf_2[1]

    first_in_second = area_start_1 <= area_start_2 and area_end_1 >= area_end_2
    second_in_first = area_start_2 <= area_start_1 and area_end_2 >= area_end_1
    if first_in_second or second_in_first and not (first_in_second and second_in_first):
        same_assignments += 1
    
    index += 2
print(same_assignments)       
        