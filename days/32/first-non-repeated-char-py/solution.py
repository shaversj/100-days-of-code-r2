def find_first_non_repeated_char(word):
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] = counts.get(letter) + 1
        else:
            counts[letter] = 1

    for letter in word:
        if counts[letter] == 1:
            return letter

#find_first_non_repeated_char("yellow")


