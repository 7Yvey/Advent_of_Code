'''day_1'''

test_input_file = 'test_input'

with open(test_input_file) as file:
    text = file.readlines()


calibration_values_sum = 0

for line in text:
    first_num = None
    last_num = None
    found_num = None
    for number_1 in line:
        if number_1.isnumeric():
            found_num = str(number_1)
        if first_num is None:
            first_num = found_num
        last_num = found_num


    calibration_value = first_num + last_num
    calibration_values_sum += int(calibration_value)
print(calibration_values_sum)

