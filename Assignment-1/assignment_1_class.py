#!/bin/python

from collections import defaultdict
import math


class Assignment1:
    def __init__(self, file=None, individual=False) -> None:
        self.result = []
        self.individual = individual
        self.method_list = [func for func in dir(self) if callable(getattr(self, func))]
        # self.main()

    def main(self):
        self.initializations()
        for method in self.method_list:
            if method.startswith("main_"):
                getattr(self, method)()
        self.resulting()

    def initializations(self):
        (
            self.letters_of_interest,
            self.letter_frequency,
            self.dict_of_interest,
        ) = self.sharing_data(
            ["L", "h", "l", "H", "s", "n", "w"], "poem.txt", self.individual
        )

    def sharing_data(self, letters_of_interest, poem_file, individual=False):
        # dictionary with the frequency of each letter in the file
        letter_frequency = self.getting_info_from_file(poem_file, individual)

        # dictionary with the frequency of each letter of interest
        dict_of_interest = self.letters_of_interest_frequency(
            letters_of_interest, letter_frequency
        )

        return letters_of_interest, letter_frequency, dict_of_interest

    def getting_info_from_file(self, poem_file, individual):
        letter_frequency = {}
        with open(poem_file, "r") as file:
            for line in file:
                for letter in line:
                    if letter in letter_frequency:
                        letter_frequency[letter] += 1
                    else:
                        letter_frequency[letter] = 1
        if individual:
            letter_frequency = self.individual_letter_frequency(letter_frequency)
        return letter_frequency

    def individual_letter_frequency(self, letter_frequency):
        for key in letter_frequency:
            letter_frequency[key] = 1
        return letter_frequency

    def letters_of_interest_frequency(self, letters_of_interest, letter_frequency):
        dict_of_interest = {}
        for letter in letters_of_interest:
            if letter in letter_frequency:
                dict_of_interest[letter] = letter_frequency[letter]
            else:
                dict_of_interest[letter] = 0
        return dict_of_interest

    def number_of_symbols(self, letter_frequency):
        """Returns the number of symbols in the dictionary"""
        summ = [
            letter_frequency[key]
            for key in letter_frequency.keys()
            if not key.isalpha()
        ]
        return sum(summ)

    def print_table(self, dict_of_interest, letter_frequency, individual):
        # the table headers

        N = sum(letter_frequency.values())
        n_symbols = self.number_of_symbols(letter_frequency)
        n_letters = N - n_symbols

        # beautifying the Markdown table
        ln = len("Number of Characters") + 2

        result = [
            f'| {"Letter":^{ln}} | {"Count":^{ln}} | {"P = Count/N":^{ln}} | {"I= -log2(P)":^{ln}} |',
            f'| {"-":^{ln}} | {"-":^{ln}} | {"-":^{ln}} | {"-":^{ln}} |',
        ]

        for key, value in dict_of_interest.items():
            information = -1 * math.log2(value / N)
            information = round(information, 3)
            information = f"{information}"
            probability = value / N
            probability = round(probability, 3)
            probability = f"{probability}"

            result.append(
                f"| {key:^{ln}} | {value:^{ln}} | {probability:^{ln}} | {information:^{ln}} |"
            )

        result.append(
            f'| {"Number of Letters":^{ln}} | {n_letters:^{ln}} | {"":^{ln}} | {"":^{ln}} | '
        )
        result.append(
            f'| {"Number of Symbols":^{ln}} | {n_symbols:^{ln}} | {"":^{ln}} | {"":^{ln}} | '
        )
        result.append(
            f'| {"Number of Characters":^{ln}} | {N:^{ln}} | {"":^{ln}} | {"":^{ln}} | '
        )

        return result

    def save_to_file(self, file_name, result):
        with open(file_name, "w") as file:
            file.write("\n\n")
            file.write("\n".join(result))

    def H(self, list_of_probabilities):
        """This function will return the entropy of a given probability"""
        import math

        h_value = -sum([p * math.log2(p) for p in list_of_probabilities])
        h_value = round(h_value, 3)
        h_info = (
            "$$\nH(X) = -\sum_{i=1}^{"
            + f"{len(list_of_probabilities)}"
            + "}p_i\log_2(p_i)"
        )

        h_info += f" = {h_value}\n$$\n\nH(x) = {h_value}\n\n"

        return h_info, h_value

    def I_x(self, x):
        """This function will return the self information of a given probability"""
        import math

        i_value = math.log2(1 / x)

        i_info = (
            "$$\nI(X) = -\log_2(p_i)"
            + f" = -\log_2({x})"
            + f" = {i_value}\n$$\n\nI(x) = {i_value}\n\n"
        )

        return i_info, i_value

    def I_all(self, x, y):
        """This function will return the self information of a given probability"""
        import math

        i_value = math.log2(1 / x)

        i_info = (
            "$$\nI(X) = -\log_2(p_i)"
            + f" = -\log_2({x})"
            + f" = {i_value}\n$$\n\nI(x) = {i_value}\n\n"
        )

        return i_info, i_value

    def print_ambiguous_table(self, dict):
        ln = len("Number of Characters") + 2

        singles = {k: v for k, v in dict.items() if k.count("|") == 0}
        doubles = {k: v for k, v in dict.items() if k.count("|") == 1}

        i_dict = {}
        # the table headers
        result = []

        # I(X)
        for key_d, value_d in doubles.items():
            temp = f'$$ I({key_d.replace("|", ";")}) = \log_' + "{2}"

            temp += "\left(\\frac" + "{" + f"P({key_d})" + "}{"
            temp += f'P({key_d.split("|")[0]})' + "}\\right) ="
            temp += f" \log_2\\left(\\frac{{{value_d}}}{{{singles[key_d.split('|')[0]]}}}\\right) = "
            temp_value = math.log2(value_d / singles[key_d.split("|")[0]])
            temp_value = round(temp_value, 3)
            temp += f"{temp_value} $$"
            i_dict[key_d] = temp_value

            result.append(temp)

        # I(X;Y)

        temp = "$$\n\\begin{align}\nΙ(X;Y) = "
        for key_d, value_d in doubles.items():
            temp += f"P({key_d}) * P({key_d.split('|')[1]}) * I({str(key_d).replace('|',';')}) + \\\ "
        temp = temp[:-6] + f" = \\\ "

        for key_d, value_d in doubles.items():
            temp += f"({value_d}) * ({singles[key_d.split('|')[1]]}) * ({i_dict[key_d]}) + \\\ "
        temp = temp[:-6] + f" = \\\ "

        value = sum(
            [
                value_d * singles[key_d.split("|")[1]] * i_dict[key_d]
                for key_d, value_d in doubles.items()
            ]
        )
        value = round(value, 3)
        temp += f"{value}"
        temp += "\n\end{align}\n$$"

        result.append(temp)

        temp = f"\nI(X;Y) = {value}\n\n"
        result.append(temp)

        return result

    def main_1(self):
        table = self.print_table(
            self.dict_of_interest, self.letter_frequency, self.individual
        )

        self.result.append("\n\n## Assignment 1 - 1\n\n")
        self.result.append("\n".join(table) + "\n\n")
        self.result.append("\n\n --- \n\n")

    def main_2(self):
        h_info, h_value = self.H(
            [
                value / sum(self.letter_frequency.values())
                for value in self.letter_frequency.values()
            ]
        )
        self.result.append("\n\n## Assignment 1 - 2\n\n")
        self.result.append(h_info)
        self.result.append("\n\n --- \n\n")

    def main_3(self):
        self.letters_of_interest = {"0": 0.35, "1": 0.65}
        table = self.print_table(
            self.letters_of_interest, self.letters_of_interest, self.individual
        )
        self.result.append("\n\n## Assignment 1 - 3\n\n")

        self.result.append("\n".join(table) + "\n\n")

        h_info, h_value = self.H([value for value in self.letters_of_interest.values()])

        self.result.append(h_info)

        possible_combinations = {
            "x=0": 0.35,
            "x=1": 0.65,
            "y=0": 0.328,
            "y=1": 0.672,
            "y=0|x=0": 0.75,
            "y=1|x=0": 0.25,
            "y=0|x=1": 0.1,
            "y=1|x=1": 0.9,
        }

        table = self.print_ambiguous_table(possible_combinations)

        self.result.append("\n".join(table) + "\n\n")

        self.result.append("\n\n --- \n\n")

    def resulting(self):
        print("\n".join(self.result))

        from pathlib import Path

        file_name = "assignment-1-all-code-result.md"
        immediate_parent = Path(__file__).parent
        root_folder = Path(immediate_parent.parent)

        file_to_save = Path(root_folder, "MD_Reports", "assignment-1", file_name)
        self.save_to_file(file_to_save, self.result)


if __name__ == "__main__":
    assignment = Assignment1()
    assignment.main()
