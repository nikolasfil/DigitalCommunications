from collections import defaultdict


def save_to_file(result, file):
    with open(file, "w") as f:
        for line in result:
            f.write(line)


def save_code():
    lines = ["```python\n\n"]
    with open(__file__, "r") as f:
        for line in f:
            lines.append(line)
    lines.append("```")
    return lines


def print_tables(dictionary):
    result = []
    result.append(f"| {'index':^10} | {'position':^10} |  {'word':^10} |\n")
    result.append(f"| {'-':^10} | {'-':^10} |{'-':^10} |\n")

    max_value = max(dictionary.values())

    for i, (phrase, index) in enumerate(dictionary.items()):
        dict_position = (
            bin(i + 1)[2:].zfill(len(bin(max_value)[2:])) if i < max_value else " "
        )
        result.append(f"| {i+1:^10} | {dict_position:^10} | {phrase:^10} |\n")

    return "".join(result)


def find_max_position(input_string):
    length = len(input_string)
    counter = 0
    while length > 0:
        length -= counter**2
        counter += 1

    return counter


def create_length_dictionary(max_length):
    binary_dict = defaultdict(list)
    for length in range(1, max_length):
        for i in range(2**length):
            binary_dict[length].append(str(bin(i))[2:].zfill(length))

    return binary_dict


def create_grouped_dict(dictionary):
    """Returns a dictionary with keys the length of the values and values a sorted list of dictionaries"""

    grouped_dict = defaultdict(list)
    for value, index in dictionary.items():
        temp_d = {value: index}
        temp_key = len(str(value))
        grouped_dict[temp_key].append(temp_d)
        grouped_dict[temp_key].sort(key=lambda x: list(x.keys())[0])
    return grouped_dict


def temp_turn_to_binary(temp_word):
    temp_word = str(bin(int(temp_word)))[2:]
    return temp_word


def get_key_from_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key


def get_sorted_list(dictionary):
    sorted_list = []
    values = list(dictionary.values()).sort()
    for value in dictionary.values():
        sorted_list.append(get_key_from_value(dictionary, value))
    return sorted_list


def lempel_ziv_dict(input_string):
    dictionary = {}
    counter = 0

    # Max length of temp_word that I can go looking at
    max_length = find_max_position(input_string)

    # Dictionary that has keys as all the possible lengths, and values lists of the binary representations
    # of numbers iterated
    binary_dict = create_length_dictionary(max_length)

    # assign a temp_string for no reason
    temp_string = input_string

    # counting how many different temp_words will be found
    counter = 0

    # checks the temp_string if it is empty and continues
    # while len(temp_string) > 0:
    # iterates through all the possible words of length 1 to max_length
    for _ in range(len(temp_string)):
        for length in range(1, max_length):
            temp_word = temp_string[:length]
            if temp_word not in dictionary.keys() and temp_word in binary_dict[length]:
                dictionary[temp_word] = counter

                # removes that temp_word from the string we are examining and continues the while loop
                temp_string = temp_string[length:]
                counter += 1
                break

    return dictionary


def lemziv_encoding(input_string):
    dictionary = lempel_ziv_dict(input_string)
    result = []

    # encoded will be a dictionary containing as key the word to be encoded
    # and as value a list of the position of the highest closest word, and one bit
    encoded_dict = defaultdict(list)

    grouped_dict = create_grouped_dict(dictionary)

    sorterd_list = get_sorted_list(dictionary)
    iterated = []

    for word in sorterd_list:
        temp_list = [0, 0]
        for i, w in enumerate(iterated):
            if word.startswith(w):
                # get the last biggest word that was inserted and that starts with w
                temp_list[0] = dictionary[w]

                temp_length = len(word)

                # start checking for the same words in the grouped_dict
                # print(f"{temp_length} {grouped_dict[temp_length]}")
                temp_sorted_length_list = [
                    list(i.keys())[0] for i in grouped_dict[temp_length]
                ]

                temp_sorted_length_list = sorted(
                    temp_sorted_length_list, key=lambda x: int(x, 2)
                )

                # print(temp_sorted_length_list)

                for same_length_word in temp_sorted_length_list:
                    # means that both words start the same
                    if same_length_word.startswith(w):
                        #     # if the same_length_word is bigger than the word we are checking then we found the small word, that means 1
                        if same_length_word > word:
                            temp_list[1] = 0
                        elif same_length_word < word:
                            # print(f"[o]={same_length_word} {word}")
                            temp_list[1] = 1
                    # print(f"[x]={temp_list} {same_length_word} {word}")
                # add the word to the iterated list
        # else:
        #     temp_list[0] = 0
        #     temp_list[1] = 1
        # print(f"{word} {temp_list}")
        encoded_dict[word] = temp_list
        iterated.append(word)
        print(f"{word} {temp_list} {iterated}")

    return encoded_dict


def main():
    # input_string = "1111100010101010101000110000000001010101000000001001111000010101111110000001010101100"
    input_string = "10101101001001110101000011001110101100011011"
    result = []
    dictionary = lempel_ziv_dict(input_string)

    # print(dictionary)
    result.append("## Lempel-Ziv Dictionary\n\n")
    result.append(print_tables(dictionary))
    result.append("\n\n")

    # Encoding
    result.append("## Encoding\n\n")
    encoded_dict = lemziv_encoding(input_string)
    result.append(f"{encoded_dict}\n\n")

    print("".join(result))

    # Saving Code

    result.append("## Code\n\n")
    # result.append("".join(save_code()))
    result.append("\n\n")

    save_to_file(result, "../MD_Reports/assignment-3-code-results.md")


if __name__ == "__main__":
    main()


# Η κωδικη λεξη ειναι το περιεχομενο του κεξθκιυ
