##advent of code 1 - calories and elves

with open('input.txt') as file_object:
    text = file_object.readlines()

elf_list = []
elf_string = ''            
for line in text:
    if line == '\n':
        calories_list = elf_string.split('\n')
        
        calorie_sum = 0
        for calorie_str in calories_list:
            if calorie_str == '':
                calorie_str = 0
            calorie_sum += int(calorie_str)
        elf_list.append(calorie_sum)
        elf_string = ''
    elf_string += line    


elf_list.sort(reverse = True)
three_elfs = elf_list[:3]
sum_caloric_elfs = sum(three_elfs)
print(sum_caloric_elfs)




