def find_first_and_last_digit(line):
    digits = [int(char) for char in line if char.isdigit()]
    if digits:
        first = digits[0]
        last = digits[-1]
    return first, last

def replace_words(line):
    dict = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    for word, digit in dict.items():
        line = line.replace(word, digit)
    return line

def solution(question):
    with open('input.txt') as file:
        result1 = 0
        result2 = 0
        for line in file:
            if question == 2:
                line = replace_words(line)
            first, last = find_first_and_last_digit(line)
            if question == 1:
                result1 += first*10 + last
            else:
                result2 += first*10 + last
    return result1 if result2 == 0 else result2


print("first question:", solution(1))
print("second question:", solution(2))


