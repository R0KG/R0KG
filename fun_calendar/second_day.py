<<<<<<< HEAD
    # # Determine which games would have been possible if the bag had been loaded with only 12
    # #  red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

    # with open("./inp_2.txt","r") as file: 
    #     total_sum = 0
    #     red_lim = 12
    #     green_lim = 13
    #     blue_lim = 14
    #     for line in file:
    #         red_total = 0
    #         green_total = 0
    #         blue_total = 0
    #         possible_to_play = True
    #         for index in range(len("Game 1: "),len(line)):
    #             if line[index].isdigit():
    #                 if line[index+1].isdigit():
    #                     temp_digit = int(line[index])*10 + int(line[index+1])
    #                     first_char = line[index+3]
    #                 else:
    #                     temp_digit = int(line[index])
    #                     first_char = line[index+2]
                        
    #                 if first_char == "r" and temp_digit > red_lim:
    #                     possible_to_play = False
    #                 elif first_char == "g" and temp_digit > green_lim:
    #                     possible_to_play = False
    #                 elif first_char == "b" and temp_digit > blue_lim:
    #                     possible_to_play = False
    #         if possible_to_play:
    #             if line[6] == ":":
    #                 print(int(line[5]))
    #                 total_sum += int(line[5])
    #             elif line[6] != ":" and line[7] == ":":
    #                 print(int(line[5])*10 + int(line[6]))
    #                 total_sum += int(line[5])*10 + int(line[6])
    #             elif line[7] != ":":
    #                 total_sum += int(line[5])*100 + int(line[6])*10 + int(line[7])
    #     print(total_sum)
            
def parse_game_line(line):
    """Parses a line of game data and returns the maximum number of each color of cubes."""
    parts = line.split(':')[1].split(';')
    max_red, max_green, max_blue = 0, 0, 0

    for part in parts:
        cubes = part.split(',')
        for cube in cubes:
            number, color = cube.strip().split(' ')
            number = int(number)

            if color == 'red':
                max_red = max(max_red, number)
            elif color == 'green':
                max_green = max(max_green, number)
            elif color == 'blue':
                max_blue = max(max_blue, number)

    return max_red, max_green, max_blue

def is_game_possible(max_red, max_green, max_blue, red_limit, green_limit, blue_limit):
    """Checks if a game is possible within the given cube limits."""
    return max_red <= red_limit and max_green <= green_limit and max_blue <= blue_limit
# def calculate_total_sum(file_path, red_limit, green_limit, blue_limit): for the first part
def calculate_total_sum(file_path):
    total_sum = 0

    with open(file_path, "r") as file:
        for line in file:
            # game_id = int(line.split(':')[0].split(' ')[1])
            max_red, max_green, max_blue = parse_game_line(line)

            # if is_game_possible(max_red, max_green, max_blue):
            #     total_sum += max_red * max_green* max_blue
            max_red, max_green,max_blue, = parse_game_line(line=line)
            total_sum += max_red * max_green* max_blue

    return total_sum

# Example usage
# red_limit, green_limit, blue_limit = 12, 13, 14
total_sum = calculate_total_sum("./inp_2.txt")
print(f"Total Sum: {total_sum}")
=======
    # # Determine which games would have been possible if the bag had been loaded with only 12
    # #  red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

    # with open("./inp_2.txt","r") as file: 
    #     total_sum = 0
    #     red_lim = 12
    #     green_lim = 13
    #     blue_lim = 14
    #     for line in file:
    #         red_total = 0
    #         green_total = 0
    #         blue_total = 0
    #         possible_to_play = True
    #         for index in range(len("Game 1: "),len(line)):
    #             if line[index].isdigit():
    #                 if line[index+1].isdigit():
    #                     temp_digit = int(line[index])*10 + int(line[index+1])
    #                     first_char = line[index+3]
    #                 else:
    #                     temp_digit = int(line[index])
    #                     first_char = line[index+2]
                        
    #                 if first_char == "r" and temp_digit > red_lim:
    #                     possible_to_play = False
    #                 elif first_char == "g" and temp_digit > green_lim:
    #                     possible_to_play = False
    #                 elif first_char == "b" and temp_digit > blue_lim:
    #                     possible_to_play = False
    #         if possible_to_play:
    #             if line[6] == ":":
    #                 print(int(line[5]))
    #                 total_sum += int(line[5])
    #             elif line[6] != ":" and line[7] == ":":
    #                 print(int(line[5])*10 + int(line[6]))
    #                 total_sum += int(line[5])*10 + int(line[6])
    #             elif line[7] != ":":
    #                 total_sum += int(line[5])*100 + int(line[6])*10 + int(line[7])
    #     print(total_sum)
            
def parse_game_line(line):
    """Parses a line of game data and returns the maximum number of each color of cubes."""
    parts = line.split(':')[1].split(';')
    max_red, max_green, max_blue = 0, 0, 0

    for part in parts:
        cubes = part.split(',')
        for cube in cubes:
            number, color = cube.strip().split(' ')
            number = int(number)

            if color == 'red':
                max_red = max(max_red, number)
            elif color == 'green':
                max_green = max(max_green, number)
            elif color == 'blue':
                max_blue = max(max_blue, number)

    return max_red, max_green, max_blue

def is_game_possible(max_red, max_green, max_blue, red_limit, green_limit, blue_limit):
    """Checks if a game is possible within the given cube limits."""
    return max_red <= red_limit and max_green <= green_limit and max_blue <= blue_limit
# def calculate_total_sum(file_path, red_limit, green_limit, blue_limit): for the first part
def calculate_total_sum(file_path):
    total_sum = 0

    with open(file_path, "r") as file:
        for line in file:
            # game_id = int(line.split(':')[0].split(' ')[1])
            max_red, max_green, max_blue = parse_game_line(line)

            # if is_game_possible(max_red, max_green, max_blue):
            #     total_sum += max_red * max_green* max_blue
            max_red, max_green,max_blue, = parse_game_line(line=line)
            total_sum += max_red * max_green* max_blue

    return total_sum

# Example usage
# red_limit, green_limit, blue_limit = 12, 13, 14
total_sum = calculate_total_sum("./inp_2.txt")
print(f"Total Sum: {total_sum}")
>>>>>>> eead956efcab8f77cd289575815d74a798fdaa14
