def calculate_beauty_of_string(words: str):
    max_beauty = 26
    beauty_of_words = 0
    lowered_words = words.lower()
    counter_table = {}

    for word in lowered_words:
        if word.isalpha():
            if word in counter_table:
                counter_table[word] += 1
            else:
                counter_table[word] = 1

    sorted_table = sorted(counter_table.items(), reverse=True, key=lambda x: x[1])

    for k, v in sorted_table:
        beauty_of_words += v * max_beauty
        max_beauty -= 1

    return beauty_of_words
