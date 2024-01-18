##2 rock paper scizors
#X for Rock, Y for Paper, and Z for Scissors.
#A for Rock, B for Paper, and C for Scissors
# the score for shape: 1 for Rock, 2 for Paper, and 3 for Scissors
#outcome of the round 0 if you lost, 3 if the round was a draw, and 6 if you won

file = ('/home/Yvey/Documents/advent_of_code/2022/day_2/input_part1.txt')

with open(file) as file_formate:
    text = file_formate.read()

game_list = text.split('\n')[:-1]

opponents_rounds = []
my_rounds = []
for item in game_list:
    opponents_rounds.append(item.split()[0])
    my_rounds.append(item.split()[1])

strategy_dict = {'A': 1, 'X' : 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}
points_dict = {'win': 6, 'draw': 3, 'loose': 0}

sum_opponent_points = 0
sum_my_points = 0


for game in range(len(game_list)):
    opponent_points = 0
    my_points = 0
    opponent_selected_shape = strategy_dict[opponents_rounds[game]]
    my_selected_shape = strategy_dict[my_rounds[game]]

    if opponent_selected_shape == my_selected_shape:
        opponent_points = points_dict['draw'] + opponent_selected_shape
        my_points = points_dict['draw'] + my_selected_shape
    
    if opponent_selected_shape > my_selected_shape:
        opponent_points = points_dict['win'] + opponent_selected_shape
        my_points = points_dict['loose'] + my_selected_shape

    if opponent_selected_shape < my_selected_shape:
        opponent_points = int(points_dict['loose']) + opponent_selected_shape
        my_points = int(points_dict['win']) + my_selected_shape

    print(opponent_points, my_points)

    sum_my_points += my_points
    sum_opponent_points += opponent_points


if sum_opponent_points > sum_my_points:
    print(f"I am loosing {sum_my_points} points to my oppenents {sum_opponent_points} points")

if sum_opponent_points < sum_my_points:
    print(f"I am winning {sum_my_points} points to my oppenents {sum_opponent_points} points")

if sum_opponent_points == sum_my_points:
    print(f"We draw with my {sum_my_points} points to my oppenents {sum_opponent_points} points")

