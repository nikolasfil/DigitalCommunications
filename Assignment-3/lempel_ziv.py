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
            bin(i + 1)[2:].zfill(len(bin(max_value)[2:])) if i < max_value else ""
        )
        result.append(f"| {index:^10} | {dict_position} | {phrase:^10} |\n")

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
    while len(temp_string) > 0:
        # iterates through all the possible words of length 1 to max_length
        for length in range(1, max_length):
            temp_word = temp_string[:length]

            if temp_word not in dictionary.keys() and temp_word in binary_dict[length]:
                dictionary[temp_word] = counter

                # removes that temp_word from the string we are examining and continues the while loop
                temp_string = temp_string[length:]
                counter += 1
                break
    return dictionary


def main():
    input_string = "1111100010101010101000110000000001010101000000001001111000010101111110000001010101100"
    input_string = "10101101001001110101000011001110101100011011"
    result = []
    dictionary = lempel_ziv_dict(input_string)

    # print(dictionary)
    result.append("## Lempel-Ziv Dictionary\n\n")
    result.append(print_tables(dictionary))
    result.append("\n\n")

    # Saving Code

    result.append("## Code\n\n")
    result.append("".join(save_code()))
    result.append("\n\n")

    save_to_file(result, "../MD_Reports/assignment-3-code-results.md")


if __name__ == "__main__":
    main()


# Η κωδικη λεξη ειναι το περιεχομενο του κεξθκιυ 
