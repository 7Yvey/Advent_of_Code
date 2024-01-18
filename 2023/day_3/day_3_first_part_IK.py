'''day 3 first part'''

def isnot_dot(line_char):
    return not (line_char == '.')
          
def find_symbol_number_upperline(line_num, lines_of_input,start_num_pos, end_num_pos):
    if line_num != 0:
        line = lines_of_input[line_num - 1]
        for item in range(len(line)):
            c = line[item]
            if isnot_dot(c):
                if item == start_num_pos - 1 and start_num_pos != 0 or item == end_num_pos +1 and end_num_pos < len(line) or item >= start_num_pos and item <= end_num_pos:
                    return True

def find_symbol_number_lowerline(line_num, lines_of_input, start_num_pos, end_num_pos):
     if line_num < len(lines_of_input) - 1:
        line = lines_of_input[line_num + 1]
        for item in range(len(line)):
            c = line[item]
            if isnot_dot(c):
                if item == start_num_pos - 1 and start_num_pos != 0 or item == end_num_pos +1 and end_num_pos < len(line) or item >= start_num_pos and item <= end_num_pos:
                    return True

def find_symbol_next_number(line_num, lines_of_input,start_num_pos, end_num_pos):
    line = lines_of_input[line_num]

    if start_num_pos != 0 and end_num_pos < len(line) - 1:
        next_c = line[end_num_pos + 1]
        previous_c = line[start_num_pos - 1]

        if isnot_dot(next_c) or isnot_dot(previous_c):
            return True 

    if start_num_pos == 0 and end_num_pos < len(line) - 1:
        next_c = line[end_num_pos + 1]
        if isnot_dot(next_c):
            return True

    if start_num_pos != 0 and end_num_pos == len(line) - 1:
        previous_c = line[start_num_pos - 1]
        if isnot_dot(previous_c):
            return True


file = "input_first_part"

with open(file) as f:
    text = f.readlines()


lines_of_input = []
for item in range(len(text)):
    text_line = text[item].strip()
    lines_of_input.append(text_line)


adjucent_num_sum = 0

for line_num in range(len(lines_of_input)):
    line = lines_of_input[line_num]   
    item = 0
    while item < len(line):
        num_position = []
        c = line[item]
        while c.isnumeric():
            num_position.append(item)
            item += 1
            if item < len(line):
                c = line[item]
            else:
                break

        if num_position != []:
            num_start = int(num_position[0])
            num_end = int(num_position[-1])

            upper_line_symbol = find_symbol_number_upperline(line_num, lines_of_input,num_start, num_end)
            lower_line_symbol = find_symbol_number_lowerline(line_num, lines_of_input, num_start, num_end)
            next_symbol = find_symbol_next_number(line_num, lines_of_input,num_start, num_end)

            if upper_line_symbol or lower_line_symbol or next_symbol:
                multi_dig_num = ''
                for position in num_position:

                    multi_dig_num += line[position]
                adjucent_num_sum += int(multi_dig_num)
               
        item += 1
            
print(adjucent_num_sum)




 