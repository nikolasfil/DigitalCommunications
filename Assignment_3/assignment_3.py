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


def print_tables(input_string):
    dictionary, encoded_dict = lemziv_encoding(input_string)

    # max_value is used for the filling of the dictionary position
    max_value = len(dictionary.values())

    result = []
    result.append(
        f"| {'index':^10} | {'position':^10} | {'word':^10} | {'encoded':^10} |\n"
    )

    result.append(f"| {'-':^10} | {'-':^10} | {'-':^10} | {'-':^10} |\n")

    for i, (phrase, index) in enumerate(dictionary.items()):
        temp_encoded = encoded_dict[phrase]

        result.append(
            f"| {i+1:^10} | {index:^10} | {phrase:^10} | {temp_encoded:^10} |\n"
        )

    return "".join(result)


def find_max_position(input_string):
    length = len(input_string)
    counter = 0
    while length > 0:
        length -= counter**2
        counter += 1
    return counter


def create_length_dictionary(max_length):
    """Returns a dictionary with keys the length of the values and values a sorted list of binary representations"""
    binary_dict = defaultdict(list)
    for length in range(1, max_length):
        for i in range(2**length):
            binary_dict[length].append(bin(i)[2:].zfill(length))

    return binary_dict


def length_binary(temp_word):
    """turns a number to binary and returns the length of the binary representation"""
    temp_word = bin(int(temp_word))[2:]
    return len(temp_word)


def temp2bin_filled(temp_word, max_length):
    """turns a number to binary and returns it as a string filled with zeros"""
    temp_word = bin(int(temp_word))[2:].zfill(max_length)
    return temp_word


def lempel_ziv_dict(input_string):
    dictionary = {}

    # Max length of temp_word that I can go looking at
    max_length = find_max_position(input_string)

    # Dictionary that has keys as all the possible lengths, and values lists of the binary representations
    # of numbers iterated
    binary_dict = create_length_dictionary(max_length)

    # assign a temp_string for no reason
    temp_string = input_string

    # counting how many different temp_words will be found
    counter = 1

    # checks the temp_string if it is empty and continues
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

    dictionary = {
        k: temp2bin_filled(v, length_binary(counter)) for k, v in dictionary.items()
    }

    if temp_string:
        print(f"{temp_string} : {counter}")

    return dictionary


def lemziv_encoding(input_string):
    dictionary = lempel_ziv_dict(input_string)

    max_value = len(max(dictionary.values()))

    encoded_dict = defaultdict(str)

    for word in dictionary.keys():
        # check if the word is 0 or 1
        if word == "0" or word == "1":
            # encoded_dict[word] = temp2bin_filled(0, max_value) + word
            encoded_dict[word] = temp2bin_filled(0, max_value) + word
            continue
        temp_pos = dictionary[word[:-1]]
        temp_bit = word[-1]
        encoded_dict[word] = temp_pos + temp_bit
    return dictionary, encoded_dict


def main():
    input_string = "1111100010101010101000110000000001010101000000001001111000010101111110000001010101100"
    # input_string = "10101101001001110101000011001110101100011011"
    result = []

    result.append("## Lempel-Ziv Dictionary\n\n")
    result.append(print_tables(input_string))
    result.append("\n\n")

    print("".join(result))

    # Saving Code

    result.append("## Code\n\n")
    result.append("".join(save_code()))
    result.append("\n\n")

    save_to_file(result, "../MD_Reports/assignment-3-code-results.md")


if __name__ == "__main__":
    main()
