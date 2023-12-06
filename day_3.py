import string

# steps for algo:
# 1. read the input file
# 2. write a function that, for a given range returns whether there is a part adjacent to it or not (including diagonals)
# 3. for each line, when we run into an integer, create a start index, then if we hit a "." or when we hit end of line, set end of index range.
# 3a. run fn2 for every integer using that range, checking to see if its adjacent or not to a part. if it is, add the integer to the sum.
# 4. if we run into a part, instead just immediately add the integer to the sum
# 5. return the sum

# 1. read the input file
with open("input.txt") as f:
    lines = f.readlines()

"""
Part 1
"""
# # 2. write a function that, for a given range returns whether there is a part adjacent to it or not (including diagonals)
# def is_adjacent(left_x, right_x, y, lines):
#     """
#     adjacent is visually defined the following way:
#     . . . . . # # # # # . .
#     . . . . . # 1 2 3 # . .
#     . . . . . # # # # # . .

#     1, 2, and 3 are considered to be adjacent if any of the # characters are symbols.

#     where lines are y and columns are x

#     """
#     punctuation_set = set(string.punctuation)
#     punctuation_set.remove(".")

#     for y_range in range(y - 1, y + 2):
#         for x_range in range(left_x - 1, right_x + 2):
#             # we ignore anything out of bounds to avoid index errors
#             if 0 <= y_range < len(lines) and 0 <= x_range < len(lines[0]):
#                 if (y_range != y or x_range < left_x or x_range > right_x) and lines[
#                     y_range
#                 ][x_range] in punctuation_set:
#                     return True
#     return False


# part_sum = 0
# for row_idx, line in enumerate(lines):
#     start_index = None
#     end_index = None
#     for col_idx, char in enumerate(line):
#         if char.isdigit():
#             if start_index is None:
#                 start_index = col_idx
#             end_index = col_idx
#         elif start_index is not None:
#             if is_adjacent(start_index, end_index, row_idx, lines):
#                 part_sum += int("".join(line[start_index : end_index + 1]))
#             start_index = None
#             end_index = None

# print("total part adjacent sum", part_sum)


# in the second part were looking going to seek each line and this time we're going to check if there are exactly two numbers adjacent to it, and if so, we will multiply those two numbers together and add them to the sum
# the updated has_two_adjacent_integers function will take the x,y coordinate of a found *, and it will look
# for exactly two integers that are adjacent to it
# considerations: we will need to first find all integers adjacent to the * and to do that we'll need
# a subfunction that traverses left or right after we find an adjacent integer to get the entire range of that integer
# so in total we'll need 3 functions:
# 1. a function that finds all integers adjacent to a *, using below
# 2. a function that ingests the integer when found and returns the full integer


def get_full_integer(x, y, lines, visited):
    """
    this function will take the x,y coordinate of a found digit, and it will look
    left and right to map the full integer value.
    """
    visited.add((x, y))

    # first walk left
    start_index = x
    while start_index > 0 and lines[y][start_index - 1].isdigit():
        visited.add((start_index - 1, y))
        start_index -= 1

    # then walk right
    end_index = x
    while end_index < len(lines[0]) - 1 and lines[y][end_index + 1].isdigit():
        visited.add((end_index + 1, y))
        end_index += 1

    return int("".join(lines[y][start_index : end_index + 1]))


def find_adjacent_integers(x, y, lines):
    """
    this function will take the x,y coordinate of a found *, and it will look
    for all integers that are adjacent to it
    """
    visited = set()
    adjacent_integers = []
    for y_range in range(y - 1, y + 2):
        for x_range in range(x - 1, x + 2):
            # we ignore anything out of bounds to avoid index errors
            if 0 <= y_range < len(lines) and 0 <= x_range < len(lines[0]):
                if (
                    lines[y_range][x_range].isdigit()
                    and (x_range, y_range) not in visited
                ):
                    # first walk either direction to find and return the full integer
                    # we need to be able to skip to the next index after the integer after this returns
                    adjacent_integers.append(
                        get_full_integer(x_range, y_range, lines, visited)
                    )
    return adjacent_integers


# now we go through each line and find all our *s to use find_adjacent_integers w/

part_sum = 0
for row_idx, line in enumerate(lines):
    for col_idx, char in enumerate(line):
        if char == "*":
            adjacent_integers = find_adjacent_integers(col_idx, row_idx, lines)
            if len(adjacent_integers) == 2:
                print(
                    "Found a gear with exactly two integers on line",
                    row_idx + 1,
                    "at",
                    col_idx + 1,
                    ":",
                    adjacent_integers,
                )
                part_sum += adjacent_integers[0] * adjacent_integers[1]

print(part_sum)
