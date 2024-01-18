'''day_5_using_classes'''


class Stack:
    '''Each stack contains crates which can be moved from one stack to another one'''
    def __init__(self, crates):
        #self.stack_number = stack_number
        self.crates = crates

    def move_from(self):
        '''moves crates from the stacks to another'''
        print(self.crates)
        

    def move_in(self, instruction_list, stack_list):
        '''moves crates into the stacks'''

def stack_lists(input, column_step, column_range, line_start, line_stop):
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

def instructions(input, number_of_instructions, column_step, line_start):  
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

stacks = stack_lists(text, 4, 9, 0, 8)

moving_instructions = instructions(text, 3, 2, 10)

boxes_to_move_list = moving_instructions[0]
move_from_list = moving_instructions[1]
move_to_list = moving_instructions[2]
current_stacks = stacks

for item in range(len(move_from_list)):
    number_move = boxes_to_move_list[item]
    move_from = move_from_list[item] -1
    move_to = move_to_list[item] -1

    remove_from_current = current_stacks[move_from]
    move_to_current = current_stacks[move_to]

    current_stacks[move_from] = remove_from_current[number_move:]
    additions = remove_from_current[:number_move]
    additions.reverse()
    current_stacks[move_to] = additions + current_stacks[move_to]

result = ''
for i in current_stacks:
    result += i[0]
print(f" The result is: {result}")

    









    

