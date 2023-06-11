import os
import string


path_to_data = "data/"
files = sorted(os.listdir(path_to_data))


all_words_set = set()
all_words = []

for file in files:
    words = []
    with open(path_to_data+file, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            
            for ch in line:
                if ch in string.punctuation or ch in '1234567890"",.-«–»!':
                    ch = ch.replace(ch, "")

            words = line.lower().split(" ")

            all_words.extend(words)
            all_words_set.update(words)


for word in all_words_set:
    count_w = all_words.count(word)
    print(f"{word} - {count_w}")
