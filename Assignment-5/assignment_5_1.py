from collections import defaultdict
from pathlib import Path
import math
from assignment_2 import (
    print_codes,
    turn_into_same_length,
    get_combinations,
)
from assignment_1_1 import print_table, sharing_data, save_to_file

# from assignment_1_2 import H


class Assignment5:
    def __init__(self, file=None, individual=False) -> None:
        self.result = []
        self.individual = individual
        if file is None:
            self.open_file = "words.txt"

        self.file = Path(Path(__file__).parent, self.open_file)

        with open(self.file, "r") as f:
            self.data = f.read().strip("\n")

        # Getting the functions to run :
        self.method_list = [
            func for func in dir(Assignment5) if callable(getattr(Assignment5, func))
        ]

        self.main()

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
        ) = sharing_data(list("αβγδ"), self.file, self.individual)

    def H(sekf, list_of_probabilities):
        """This function will return the entropy of a given probability"""
        import math

        h_value = -sum([p * math.log2(p) for p in list_of_probabilities])
        h_value = round(h_value, 3)
        h_info = (
            "$$\nH(X) = -\sum_{i=1}^{"
            + f"{len(list_of_probabilities)}"
            + "}p_i\log_2(p_i)"
        )
        h_info += "\n$$\n\n$$\nH(X) = -"
        for i, p in enumerate(list_of_probabilities):
            p = round(p, 3)
            h_info += f" {p}*log_2({p})"
            if i != len(list_of_probabilities) - 1:
                h_info += " - "
            else:
                h_info += f" = {h_value}\n$$\n\nH(x) = {h_value}\n\n"
        # h_info += f" = {h_value}\n$$\n\nH(x) = {h_value}\n\n"

        return h_info, h_value

    def main_1(self):
        # printing the table that contains the possibility of occurence and the αυτοπληροφορια
        table = print_table(
            self.dict_of_interest, self.letter_frequency, self.individual
        )

        # Adding it to the result for printing
        table = "\n".join(table)
        self.result.append(table)

        self.n_letter = sum(self.letter_frequency.values())

        self.output = {
            key: (value / self.n_letter) for key, value in self.letter_frequency.items()
        }

        self.h_info, self.h_value = self.H(list(self.output.values()))

        self.output = {
            key: round(value / self.n_letter, 3)
            for key, value in self.letter_frequency.items()
        }

        self.result.append(self.h_info)

        self.result.append("\n\n---\n\n")

    def main_2(self):
        # Assignment 2 3
        self.result.append("\n\n## Assignment-5-1-a\n\n")

        self.combinations_dict = self.output

        self.comb_same_length = turn_into_same_length(self.combinations_dict)
        self.comb_same_length = {
            key: value[1:] for key, value in self.comb_same_length.items()
        }
        # print(comb_same_length)

        self.comb_same_length_info = print_codes(self.comb_same_length)
        self.result.append(self.comb_same_length_info)

        # Data encoding with code of the same length :

        self.comb_data_encoding = "".join(
            [self.comb_same_length[key] for key in self.data]
        )
        self.result.append(
            f"\n\nData encoding with code of the same length : \n\n {self.data} -> \n\n\{self.comb_data_encoding}\n\n"
        )

        self.result.append("\n\n---\n\n")

    def main_3(self):
        self.combinations_info, self.combinations = get_combinations(
            self.letter_frequency
        )
        # result.append(combinations_info)

        # comb_same_length_info = print_codes(comb_same_length)
        # result.append(comb_same_length_info)

    def resulting(self):
        # --------------- Results  --------------------
        print("\n".join(self.result))

        immediate_parent = Path(__file__).parent
        root_folder = Path(immediate_parent.parent)

        file_to_save = Path(root_folder, "MD_Reports", "assignment-5-1-code-result.md")

        save_to_file(file_to_save, self.result)


if __name__ == "__main__":
    assignment = Assignment5()
