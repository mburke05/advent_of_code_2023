import re


def get_input_file() -> list:
    with open("input.txt", "r") as f:
        return f.readlines()


def is_valid_game(game: str, rules: dict()) -> int:
    """
    Takes a game string which is the line of an input file, the first colon is the game and ID as an integer, then the subsequent semi-colon separated sequences are the game sequences.

    This parses that separated sequence and returns the game ID if the game is valid, otherwise returns 0. To do that it receives as input a dict of rules {"red":some_int, ...} for the number of cubes of each color that are allowed for a valid game. The number of cubes shown in each sequence must be less than or equal to the number in the rules dict.

    Example game line:
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green -> id: 1, sequences: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    """

    # first split the game to get an id and the sequences
    game_id, game_sequences = game.split(":")
    game_id = int(game_id.split()[1])

    # now split the sequences by semi-colon
    sequence = game_sequences.split(";")

    # check each sequence to see if it exceeds any of the rule values, if so return 0
    for subsequence in sequence:
        # make this into a dict of cubes by color of cube pulled and number of those cubes
        cubes_pulled = subsequence.split(",")
        for pull in cubes_pulled:
            # extract integer using regex which represents the number of cubes pulled
            num_cubes = int(re.findall(r"\d+", pull)[0].strip())
            # then extract the color which is the text in the string
            color = str(re.findall(r"[a-zA-Z]+", pull)[0].strip())
            # check if the number of cubes pulled exceeds the rule value for that color
            if num_cubes > rules[color]:
                return 0
    # if we get here then all the sequences were valid so return the game id
    return game_id


valid_sum = 0
file = get_input_file()
for line in file:
    valid_sum += is_valid_game(line, {"red": 12, "green": 13, "blue": 14})
print(valid_sum)
