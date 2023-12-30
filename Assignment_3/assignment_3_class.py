from pathlib import Path
import math
from itertools import defaultdict


class Assignment3:
    def __init__(self, file=None, individual=False) -> None:
        self.result = [f"---\nnum: {3} \n---\n"]
        self.individual = individual

        # Getting the functions to run :
        self.method_list = [func for func in dir(self) if callable(getattr(self, func))]

        if file:
            self.file = file
        else:
            self.file = "assignment-3-code-result.md"
        parent_folder = Path(__file__).parent
        root_folder = Path(parent_folder.parent)
        self.file = Path(root_folder, "MD_Reports", "assignment-3", self.file)

    def main(self):
        self.initializations()
        for method in self.method_list:
            if method.startswith("main_"):
                getattr(self, method)()
        self.resulting()

    def initializations(self):
        pass

    def resulting(self):
        # --------------- Results  --------------------
        print("\n".join(self.result))

        self.save_to_file(self.file, self.result)

    def save_code():
        lines = ["```python\n\n"]
        with open(__file__, "r") as f:
            for line in f:
                lines.append(line)
        lines.append("```")
        return lines

    def save_to_file(self, file_name, result):
        with open(file_name, "w") as file:
            file.write("\n".join(result))

    def print_tables(self, input_string):
        dictionary, encoded_dict = self.lemziv_encoding(input_string)

        # max_value is used for the filling of the dictionary position

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

    def find_max_position(self, input_string):
        length = len(input_string)
        counter = 0
        while length > 0:
            length -= counter**2
            counter += 1
        return counter

    def create_length_dictionary(self, max_length):
        """Returns a dictionary with keys the length of the values and values a sorted list of binary representations"""
        binary_dict = defaultdict(list)
        for length in range(1, max_length):
            for i in range(2**length):
                binary_dict[length].append(bin(i)[2:].zfill(length))

        return binary_dict

    def length_binary(self, temp_word):
        """Returns the binary representation of the length of the word"""
        binary = bin(int(temp_word))[2:]
        return len(binary)

    def temp2bin_filled(self, temp_word, max_length):
        """Returns the binary representation of the word filled with zeros"""
        binary = bin(int(temp_word))[2:]
        return binary.zfill(max_length)

    def lempel_ziv_dict(self, input_string):
        dictionary = {}

        # Max length of temp_word that I can go looking at
        max_length = self.find_max_position(input_string)

        # Dictionary that has keys as all the possible lengths, and values lists of the binary representations
        # of numbers iterated
        binary_dict = self.create_length_dictionary(max_length)

        # assign a temp_string for no reason
        temp_string = input_string

        # counting how many different temp_words will be found
        counter = 1

        # checks the temp_string if it is empty and continues
        # iterates through all the possible words of length 1 to max_length
        for _ in range(len(temp_string)):
            for length in range(1, max_length):
                temp_word = temp_string[:length]
                if (
                    temp_word not in dictionary.keys()
                    and temp_word in binary_dict[length]
                ):
                    dictionary[temp_word] = counter
                    # removes that temp_word from the string we are examining and continues the while loop
                    temp_string = temp_string[length:]
                    counter += 1
                    break

        dictionary = {
            k: self.temp2bin_filled(v, self.length_binary(counter))
            for k, v in dictionary.items()
        }

        if temp_string:
            print(f"{temp_string} : {counter}")

        return dictionary

    def lemziv_encoding(self, input_string):
        dictionary = self.lempel_ziv_dict(input_string)

        max_value = len(max(dictionary.values()))

        encoded_dict = defaultdict(str)

        for word in dictionary.keys():
            # check if the word is 0 or 1
            if word == "0" or word == "1":
                # encoded_dict[word] = temp2bin_filled(0, max_value) + word
                encoded_dict[word] = self.temp2bin_filled(0, max_value) + word
                continue
            temp_pos = dictionary[word[:-1]]
            temp_bit = word[-1]
            encoded_dict[word] = temp_pos + temp_bit
        return dictionary, encoded_dict

    def main_1(self):
        input_string = "1111100010101010101000110000000001010101000000001001111000010101111110000001010101100"
        # input_string = "10101101001001110101000011001110101100011011"
        result = []

        result.append("## Lempel-Ziv Dictionary\n\n")
        result.append(self.print_tables(input_string))
        result.append("\n\n")

        print("".join(result))

        # Saving Code

        result.append("## Code\n\n")
        result.append("".join(self.save_code()))
        result.append("\n\n")

        # save_to_file(result, "../MD_Reports/assignment-3-code-results.md")
        self.save_to_file(result, self.file)


if __name__ == "__main__":
    assignment = Assignment3()
    assignment.main()
