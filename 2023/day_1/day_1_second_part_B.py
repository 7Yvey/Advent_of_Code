'''day_1'''

number_dict = {'one': '1', 'two' : '2', 'three': '3', 'four' : '4', 
'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9',
 '1' : '1', '2' : '2', '3' : '3', '4' : '4', '5' : '5', '6': '6', '7' : '7',
 '8': '8', '9': '9'}

def try_parse_number(line, start):
    for number in number_dict.keys():
            if line.startswith(number, start):
                return number_dict[number]
    return None


test_input_file = 'input_second_part'

with open(test_input_file) as file:
    text = file.readlines()

calibration_values_sum = 0
for line in text:
    first_num = None
    last_num = None

    for start in range(len(line)):
        current_number = try_parse_number(line, start)
        if current_number is None:
            continue

        if first_num is None:
            first_num = current_number

        last_num = current_number
    calibration_value = first_num + last_num
    calibration_values_sum += int(calibration_value)
print(f"The sum of calibration values is: {calibration_values_sum}")