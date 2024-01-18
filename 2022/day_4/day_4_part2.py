'''Day 4 second part'''

file_name = 'input.txt'

with open(file_name) as file:
    text = file.read()
    text_split = text.split('\n')
    #print(text_split)
    
    space_list = []
    for row in text_split[:-1]:
        spaces_row = row.split(',')
        for space in spaces_row:
            space_split = space.split('-')
            space_list.append((int(space_split[0]), int(space_split[1])))
          
overlap_count = 0
space_index = 0
while space_index < len(space_list):
    
    elf_1_space = space_list[space_index]
    elf_2_space = space_list[space_index + 1]
    elf_1_start = elf_1_space[0]
    elf_1_end = elf_1_space[1]
    elf_2_start = elf_2_space[0]
    elf_2_end = elf_2_space[1]
    
   

    overlap_case_1 = elf_1_start <= elf_2_start and elf_1_end >= elf_2_start
    overlap_case_2 = elf_2_start <= elf_1_start and elf_2_end >= elf_1_start

    if overlap_case_1 or overlap_case_2:
       # print(elf_1_space, elf_2_space)
        overlap_count += 1

    
    space_index += 2
print(overlap_count)

        
        




