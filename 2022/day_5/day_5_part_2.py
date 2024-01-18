'''day_5_using'''

def parse_stacks(input, column_step, column_range, line_start, line_stop):
    column_extraction = []
    index = 1
    for i in range(column_range):
        column = []
        empty = ' '
        for lines in input[line_start:line_stop]:
            if lines[index] != empty:
                column.append(lines[index])
        column_extraction.append(column)
        index += column_step   
    return column_extraction    

def parse_instructions(input, number_of_instructions, column_step, line_start):  
    instruction_list = []
    string_index = 1
    for item in range(number_of_instructions):
        instruction = []        
        for line in input[line_start:]:            
            instruction_separation = line.rstrip().split(' ')
            instruction.append(int(instruction_separation[string_index]))
        instruction_list.append(instruction)
        string_index += column_step
    return instruction_list


input_file = 'input.txt'

with open(input_file) as file:
    text = file.readlines()

stacks = parse_stacks(text, 4, 9, 0, 8)

moving_instructions = parse_instructions(text, 3, 2, 10)

boxes_to_move_list = moving_instructions[0]
move_from_list = moving_instructions[1]
move_to_list = moving_instructions[2]
current_stacks = stacks

for index in range(len(move_from_list)):
    number_move = boxes_to_move_list[index]
    move_from = move_from_list[index] -1
    move_to = move_to_list[index] -1

    remove_from_current = current_stacks[move_from]
    move_to_current = current_stacks[move_to]

    current_stacks[move_from] = remove_from_current[number_move:]
    additions = remove_from_current[:number_move]
    #additions.reverse()
    current_stacks[move_to] = additions + current_stacks[move_to]

result = ''
for i in current_stacks:
    result += i[0]
print(f"The result is: {result}")
