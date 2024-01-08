from collections import defaultdict
from pathlib import Path
import math

from assignment_1_class import Assignment1
from assignment_2_class import Assignment2
from assignment_5_plotter import plotting

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
        self.assignment_2 = Assignment2(individual=self.individual, display=True)
        # self.main()

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

        # self.assignment_2.brancher.output_file = self.samefolder("assignment-5-4.txt")
        self.assignment_2.brancher.output_file = self.mdreporting(
            "assignment-5", "assignment-5-huffman-tree.md"
        )

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

        # self.output = {
        #     key: round(value / self.n_letter, 3)
        #     for key, value in self.letter_frequency.items()
        # }

        self.result.append(self.h_info)

        self.result.append("\n\n---\n\n")

    def main_2(self):
        # Assignment 2 3
        self.result.append("\n\n## Assignment-5-2\n\n")

        self.combinations_dict = self.output

        self.comb_same_length = self.assignment_2.turn_into_same_length(
            self.combinations_dict
        )
        self.comb_same_length = {
            key: value[1:] for key, value in self.comb_same_length.items()
        }

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

    def not_main_4(self):
        # # self.brancher = self.assignment_2.;\
        # self.bracker = self.assignment_2.HuffmanBrancher(
        #      self.assignment_2.file_tree,
        # )
        # print(self.assignment_2.brancher.input_text)

        self.output = self.assignment_2.huffman_functions.replacing_keys(
            self.origianl_output, self.output
        )

        huffman_codes = self.assignment_2.huffman_functions.huffman_encoding(
            self.output
        )

        # self.result.append("\n\n## Assignment-5-4\n\n")

    def main_3_1(self):
        self.result.append("\n\n## Assignment-5-3\n\n")

        # self.output = self.origianl_output
        self.output_2 = self.output

        self.output_huffman_codes = self.assignment_2.huffman_functions.huffman(
            self.output
        )
        self.output_huffman_codes = self.assignment_2.change_to_numbering(
            self.output_huffman_codes
        )

        self.output = self.assignment_2.change_to_numbering(self.output)
        self.result.append("\n\n---\n\n")

    def main_3_2(self):
        combinations_info, self.combinations_dict = self.assignment_2.get_combinations(
            self.output
        )

        self.result.append(combinations_info)

        (
            huffman_encoded_info,
            huffman_encoded_value,
        ) = self.assignment_2.huffman_functions.huffman_encode_pairs(
            self.combinations_dict
        )

        self.result.append(huffman_encoded_info)

        lines = self.assignment_2.brancher.get_huffman_lines()
        (
            self.resulting_nodes,
            noding,
        ) = self.assignment_2.brancher.splitting_huffman_lines(lines)

        self.assignment_2.brancher.save_tree_to_file(
            self.assignment_2.brancher.output_file, self.resulting_nodes
        )

        self.result.append("\n\n---\n\n")

    def main_4_1(self):
        self.result.append("\n\n## Assignment-5-4 \n\n")

        # Use this variable that is already compiled
        # self.comb_same_length
        output = self.assignment_2.huffman_functions.replacing_keys(
            self.output_2, self.output
        )
        i_info, i_value = self.assignment_2.I_info(output)

        h_info, h_value = self.assignment_2.H_info(output)

        print(output, self.comb_same_length)
        r_info, r_value = self.assignment_2.R_info(self.comb_same_length, output)

        n_info, n_value = self.assignment_2.n_info(r_value, h_value)

        self.result.append(i_info)
        self.result.append(h_info)
        self.result.append(r_info)
        self.result.append(n_info)

    def main_4_2(self):
        self.result.append("\n\n### Huffman Code  \n\n")
        combinations_info, combinations_dict = self.assignment_2.get_combinations(
            self.output
        )

        (
            huffman_encoded_info,
            huffman_encoded_value,
        ) = self.assignment_2.huffman_functions.huffman_encode_pairs(combinations_dict)

        huffman_h_info, huffman_h_value = self.assignment_2.H_info(combinations_dict)

        self.result.append(huffman_h_info)

        huffman_r_info, huffman_r_value = self.assignment_2.R_info(
            huffman_encoded_value, combinations_dict
        )
        print(huffman_encoded_value, combinations_dict)

        self.result.append(huffman_r_info)

        huffman_n_info, huffman_n_value = self.assignment_2.n_info(
            huffman_r_value, huffman_h_value
        )

        self.result.append(huffman_n_info)
        self.result.append("\n\n---\n\n")

    def done_main_8(self):
        # Only needed to run once

        # Define the points
        points = []

        points_ = [
            (1, 0),
            (1, -(math.sqrt(2) / 2)),
            (2, -(math.sqrt(2) / 2)),
            (2, (math.sqrt(2) / 2)),
            (3, (math.sqrt(2) / 2)),
            (3, 0),
        ]
        points.append(points_)

        points_ = [(1, 0), (1, (math.sqrt(2) / 2)), (3, (math.sqrt(2) / 2)), (3, 0)]
        points.append(points_)

        points_ = [(0, -1), (1, -1), (1, 0)]
        points.append(points_)

        points_ = [(3, 0), (3, 1), (4, 1), (4, 0)]
        points.append(points_)

        for i, point_list in enumerate(points):
            file = self.samefolder(f"assignment-5-8-plot-{i+1}.png")
            plotting(point_list, titling=f"Graph of f{i+1}(4-t)", show=False, file=file)

    def main_7(self):
        # Only needed to run once

        # Define the points
        points = []

        points_ = [(1, 0), (0, 1)]
        points.append(points_)

        points_ = [(1, 0), (1, math.sqrt(2) / 2), (3, math.sqrt(2) / 2), (3, 0)]
        points.append(points_)

        points_ = [(3, 0), (3, -1), (4, -1), (4, 0)]
        points.append(points_)

        points_ = [(0, 1), (1, 1), (1, 0)]
        points.append(points_)

        for i, point_list in enumerate(points):
            file = self.samefolder(f"assignment-5-5-plot-{i+1}.png")
            plotting(
                point_list,
                titling=f"Graph of f{i+1}(t)",
                show=False,
                file=file,
                label=f"f{i+1}(t)",
            )

    def resulting(self, printing: bool = True):
        # --------------- Results  --------------------

        printing = False
        if printing:
            print("\n".join(self.result))

        file_to_save = self.mdreporting("assignment-5", "assignment-5-1-code-result.md")

        self.assignment_1.save_to_file(file_to_save, self.result)


if __name__ == "__main__":
    assignment = Assignment5()
    assignment.main()
