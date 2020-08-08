# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
# Most frequently used words in a text
import heapq
import re


def top_3_words(text: str):
    counter = {}
    split_text = text.split()
    for word in split_text:
        word_regex = re.compile(r'[a-z\']+')
        parsed_word_search = word_regex.search(word.lower())
        if parsed_word_search:
            parsed_word = parsed_word_search.group()
            # check if parsed_word contains letters
            if parsed_word.islower():
                if parsed_word in counter:
                    counter[parsed_word] += 1
                else:
                    counter[parsed_word] = 1

    heap = [(value, key) for key, value in counter.items()]
    largest = heapq.nlargest(3, heap)
    print(largest)

    return [key for value, key in largest]
