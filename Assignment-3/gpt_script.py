def lempel_ziv_compress(data):
    dictionary = {}
    compressed_data = []
    next_index = 0

    index = 0
    while index < len(data):
        current_char = data[index]
        current_string = current_char

        while current_string in dictionary and index < len(data) - 1:
            index += 1
            current_char = data[index]
            current_string += current_char

        if current_string in dictionary:
            compressed_data.append(
                (
                    bin(dictionary[current_string])[2:],
                    bin(len(current_string))[2:],
                    bin(ord(current_string))[2:],
                    f"{dictionary[current_string]:b}-{len(current_string):b}-{ord(current_string):b}",
                )
            )
        else:
            compressed_data.append(
                (
                    bin(next_index)[2:],
                    bin(1)[2:],
                    bin(ord(current_char))[2:],
                    f"{next_index:b}-1-{ord(current_char):b}",
                )
            )
            dictionary[current_string] = next_index
            next_index += 1

        index += 1

    return compressed_data


def display_compressed_data(compressed_data):
    print(f"{'Index':<15}{'Position':<15}{'Value':<25}{'Encoded Word'}")
    print("-" * 80)

    for i, (index, position, value, encoded_word) in enumerate(compressed_data):
        print(f"{index:<15}{position:<15}{value:<25}{encoded_word}")


if __name__ == "__main__":
    input_data = "10101101001001110101000011001110101100011011"
    compressed_data = lempel_ziv_compress(input_data)
    display_compressed_data(compressed_data)
