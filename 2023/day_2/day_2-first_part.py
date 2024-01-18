'''day_2-first_part'''


def get_game_num(line):
    '''
    gets game number from from text where each line represents game
    '''
    split_by_semicollon = line.strip().split(':')
    game_head_separ = split_by_semicollon[0].split(' ')
    current_game = int(game_head_separ[1])
    return current_game
 
def get_game_sets(line):
    '''
    gets all sets from one game, it takes line of text where each line represents game
    '''
    split_by_semicollon = line.strip().split(':')
    game_set_res = split_by_semicollon[1]
    game_sets = game_set_res.split(';')   
    return game_sets
      
def separate_cubes_game_sets(game_set, start):
    '''
    Gets number of cubes with a specific colour from each other in one set of one game.
    '''
    cubes_in_set = game_sets[start].split(',')
    return cubes_in_set

def get_cube_colour_number(cube):
    '''
    Gets number of cubes with specific colour
    '''
    split_cube_col_num = cube.strip().split(' ')
    colour_cube_num = int(split_cube_col_num[0])
    cube_colour = split_cube_col_num[1]
    return  cube_colour, colour_cube_num



file = 'test_input_first_part'

cube_limits_dict = { 'red': 12, 'green' : 13 , 'blue': 14 }


with open(file) as f:
    text = f.readlines()

game_sum_score = 0

for line in text:
    impossible_game = False

    current_game = get_game_num(line)

    game_sets = get_game_sets(line)
    for start in range(len(game_sets)):
        cube_set = separate_cubes_game_sets(game_sets, start)    
    
        for cube in cube_set:
           cube_colour_number = get_cube_colour_number(cube)
           cube_colour = cube_colour_number[0]
           colour_cube_num = cube_colour_number[1]
           possible_cube_num = cube_limits_dict[cube_colour]
           if colour_cube_num > possible_cube_num:
                impossible_game = True
                break       
        
        if impossible_game:
            break
    
    if not impossible_game:
        game_sum_score += current_game
    
print(game_sum_score)


    
   