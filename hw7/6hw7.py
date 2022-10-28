def solve_riddle(riddle, word_length, start_letter, reverse=False):
    start = riddle.find(start_letter)
    if not reverse:
        return riddle[start : word_length + start]
    else:
        result = riddle[start - word_length + 1 : start + 1]
        return result[::-1]


print(solve_riddle("mi1powerpret", 5, "p", reverse=False))
print(solve_riddle("mi1powperet", 3, "r", reverse=True))
