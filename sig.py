import random

def get_random_insult(filename):
    read_file = open(filename)
    text = read_file.read()
    read_file.close()
    lines = list(filter(lambda s: s != "", text.split("\n")))
    lines_with_words_separated = [line.split() for line in lines]
    number_of_cols = len(lines_with_words_separated[0])
    cols = [[line[col_number] for line in lines_with_words_separated] for col_number in range(number_of_cols)]
    random_insults = [random.choice(cols[i]) for i in range(number_of_cols)]
    return "Thou " + " ".join(random_insults) + "!"

if __name__ == "__main__":
    print(get_random_insult("shakespearean_insult_cols.txt"))
