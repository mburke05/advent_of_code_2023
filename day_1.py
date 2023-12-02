import re


def get_input_file() -> list:
    with open("input.txt", "r") as f:
        return f.readlines()


# # part 1
calibration_sum = 0
for line in get_input_file():
    digits = re.findall(r"\d", line)

    if len(digits) > 1:
        calibration_sum += int(digits[0] + digits[-1])
    else:
        calibration_sum += int(2 * digits[0])

print(calibration_sum)

# part 2

nums_from_text = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

updated_calibration_sum = 0
for line in get_input_file():
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append((i, c))
        else:
            for word, num in nums_from_text.items():
                try:
                    if line[i : i + len(word)] == word:
                        digits.append((i, num))
                except IndexError:
                    pass

    if len(digits) < 2:
        updated_calibration_sum += int(2 * digits[0][1])
    else:
        # first sort the digits array using the index as key
        digits.sort(key=lambda x: x[0])
        updated_calibration_sum += int(digits[0][1] + digits[-1][1])
    print(line, digits)
print(updated_calibration_sum)
