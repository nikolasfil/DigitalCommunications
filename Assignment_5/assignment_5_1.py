from collections import defaultdict
from pathlib import Path
import math

from assignment_1_class import Assignment1
from assignment_2_class import Assignment2

# from assignment_1_2 import H


class Assignment5:
    def __init__(self, file=None, individual=False) -> None:
        self.result = ["---\nnum: 5\n---\n"]
        self.individual = individual
        if file is None:
            self.open_file = "words.txt"

        self.file = Path(Path(__file__).parent, self.open_file)

        with open(self.file, "r") as f:
            self.data = f.read().strip("\n")

        # Getting the functions to run :
        self.method_list = [func for func in dir(self) if callable(getattr(self, func))]

        self.assignment_1 = Assignment1(individual=self.individual)
        self.assignment_2 = Assignment2(individual=self.individual, display=False)
        # self.main()

    def mdreporting(self, assignment, file_name):
        parent_folder = Path(__file__).parent
        root_folder = Path(parent_folder.parent)

        file = Path(root_folder, "MD_Reports", assignment, file_name)

        return file

    def mdreporting(self, assignment, file_name):
        parent_folder = Path(__file__).parent
        root_folder = Path(parent_folder.parent)

        file = Path(root_folder, "MD_Reports", assignment, file_name)

        return file

    def samefolder(self, file_name):
        parent_folder = Path(__file__).parent
        file = Path(parent_folder, file_name)
        return file

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
            # ) = sharing_data(list("αβγδ"), self.file, self.individual)
        ) = self.assignment_1.sharing_data(list("αβγδ"), self.file, self.individual)

    def H(sekf, list_of_probabilities):
        """This function will return the entropy of a given probability"""

        # This is an overwrite of an imported function

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
        # table = print_table(
        table = self.assignment_1.print_table(
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

        self.comb_same_length = self.assignment_2.turn_into_same_length(
            self.combinations_dict
        )
        self.comb_same_length = {
            key: value[1:] for key, value in self.comb_same_length.items()
        }
        # print(comb_same_length)

        self.comb_same_length_info = self.assignment_2.print_codes(
            self.comb_same_length
        )
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
        self.result.append("\n\n## Assignment-5-3\n\n")

        combinations_info, combinations_dict = self.assignment_2.get_combinations(
            self.output
        )
        self.result.append(combinations_info)

        # Bad previous coding forces me to do this
        self.output = self.assignment_2.change_to_numbering(self.output)

        # so this one will be in a1 instead of single lettering but it should be  fun to rerun it and just save again the table from the probabilities and just copy paste it

        combinations_info, combinations_dict = self.assignment_2.get_combinations(
            self.output
        )

        self.result.append(combinations_info)

        (
            huffman_encoded_info,
            huffman_encoded_value,
        ) = self.assignment_2.huffman_functions.huffman_encode_pairs(combinations_dict)

        # print(huffman_encoded_info)
        self.result.append(huffman_encoded_info)

        self.result.append("\n\n---\n\n")

    def main_4(self):
        # # self.brancher = self.assignment_2.;\
        # self.bracker = self.assignment_2.HuffmanBrancher(
        #      self.assignment_2.file_tree,
        # )
        print(self.assignment_2.brancher.file_tree)

    def resulting(self):
        # --------------- Results  --------------------
        # print("\n".join(self.result))

        file_to_save = self.mdreporting("assignment-5", "assignment-5-1-code-result.md")

        self.assignment_1.save_to_file(file_to_save, self.result)


if __name__ == "__main__":
    assignment = Assignment5()
    assignment.main()
