from pathlib import Path
from assignment_1_class import Assignment1
import math
from assignment_2_huffman_functions_class import HuffmanFunctions, HuffmanBrancher
from efficiency_plotter import plotter


class Assignment2:
    def __init__(self, file=None, individual=False) -> None:
        self.result = []
        self.individual = individual

        # Getting the functions to run :
        self.method_list = [func for func in dir(self) if callable(getattr(self, func))]

        self.assignment_1 = Assignment1(individual=self.individual)
        self.huffman_functions = HuffmanFunctions()
        self.brancher = HuffmanBrancher(
            "huffman_tree.txt", "assignment_2_huffman_tree_1.md"
        )
        # self.main()

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

        immediate_parent = Path(__file__).parent
        root_folder = Path(immediate_parent.parent)

        file_to_save = Path(
            root_folder, "MD_Reports", "assignment-5", "assignment-5-1-code-result.md"
        )

        self.assignment_1.save_to_file(file_to_save, self.result)

    def change_to_numbering(self, dictionary):
        result = {}
        for i, value in enumerate(dictionary.values()):
            result[f"a{i+1}"] = value
        return result

    def change_to_letters(self, dictionary):
        result = {}
        for i, value in enumerate(dictionary.values()):
            result[chr(97 + i)] = value
        return result

    def print_codes(self, codes):
        result = f"| {'Symbol':^15} | {'Code':^15} |\n| {'-':^15} | {'-':^15} |\n"
        for key, value in codes.items():
            result += f"| {key:^15} | {value:^15} |\n"
        return result

    def I_info(self, output):
        result = f"| {'I':^14} | {'Log':^15} |\n |{'-':^14} | {'-':^15} |\n"
        i_dict = {}
        for key, value in output.items():
            # do -log2(value )
            val = -1 * math.log2(value)
            val = round(val, 3)
            result += f"| I<sub>{key}</sub> | {val:^15} |\n"
            i_dict[key] = val

        return result, i_dict

    def H_info(self, output):
        val = 0
        result = "$$\n\\begin{align}\nH(X) = "
        result += "  \sum_{i=1}^{n} P(x_{i}) \cdot I(x_{i}) = \\\ "

        for key in output.keys():
            # result += "I_{" + f"{key}" + "} \cdot P_{" + f"{key}" + "} + \\\ "
            result += "I_{" + f"{key}" + "} \cdot P_{" + f"{key}" + "} + "

        # result = result[:-6]
        result = result[:-2]

        result += " = \\\ "

        for key, value in output.items():
            I = round(-1 * math.log2(value), 3)
            val += (I) * value
            result += f"{I} \cdot {value}+"

        result = result[:-1]
        val = round(val, 3)

        result += f" = \\\ {val} \n\end"
        result += "{align}$$"
        result += f" \n\nH(x) = {val}\n"
        return result, val

    def R_info(self, codes, output):
        val = 0
        result = "$$\n\\begin{align}\nR = "
        result += "  \sum_{i=1}^{n} P(x_{i}) \cdot length_{i} = \\\ "

        # for key, value in output.items():
        #     I = round(-1 * math.log2(value), 3)
        #     val += (I) * value
        #     result += f"{I} \cdot {value}+"

        for key, value in codes.items():
            # R+=f"{output[key]} * {len(str(value))} + "
            result += f"{output[key]} \cdot {len(str(value))} + "
            # result += f"{output[key]} \cdot {len(str(value))} + \\\ "
            val += output[key] * len(str(value))
        result = result[:-2]
        # result = result[:-6]
        val = round(val, 3)

        result = result[:-1]
        val = round(val, 3)

        result += f" = \\\ {val} \n\end"
        result += "{align}$$"
        result += f" \n\nR = {val}\n"
        return result, val

    def n_info(self, r, h, pairs=1):
        h = float(h)
        r = float(r)
        val = round(pairs * h / r, 3)
        result = (
            "$$\n n = \\frac{"
            + f"{pairs if pairs !=1 else ''}"
            + "H(x)}{R} = "
            + "\\frac{"
            + f"{pairs*h}"
            + "}{"
            + f"{r}"
            + "}"
            + f" = {val} = {val*100}\\ \% \n$$\n\n n = {val} "
        )
        # result =f"n = H(x)/R = {h}/{r} = {val}"
        return result, val

    def get_combinations(self, output):
        result_list = []
        for key_a in output.keys():
            for key_b in output.keys():
                result_list.append((key_a, key_b))
        result_dict = {}
        for key in result_list:
            result_dict["".join(key)] = round(output[key[0]] * output[key[1]], 3)

        result = f"\n\n| {'Combination':^15} | {'Probability':^15} |\n| {'-':^15} | {'-':^15} |\n"
        for key, value in result_dict.items():
            result += f"| {key:^15} | {value:^15} |\n"
        return result, result_dict

    def get_combinations_different(self, output1, output2):
        result_list = []
        for key_a in output1.keys():
            for key_b in output2.keys():
                result_list.append((key_a, key_b))
        result_dict = {}
        for key in result_list:
            result_dict["".join(key)] = round(output1[key[0]] * output2[key[1]], 3)

        result = f"\n\n| {'Combination':^15} | {'Probability':^15} |\n| {'-':^15} | {'-':^15} |\n"
        for key, value in result_dict.items():
            result += f"| {key:^15} | {value:^15} |\n"
        return result, result_dict

    def same_length_coding(self, codes):
        # length = max([len(str(bin(key))) for key in codes.keys()])
        length = len(str(bin(len(codes.keys())))[2:])
        return length

    def turn_into_same_length(self, codes):
        length = self.same_length_coding(codes)
        result = {}
        for i, key in enumerate(codes.keys()):
            result[key] = str(bin(i))[2:].zfill(length)
        return result

    def main_1(self):
        self.output = {"a1": 0.53, "a2": 0.37, "a3": 0.10}
        self.output = self.change_to_letters(self.output)

        # checkout the huffman functions
        self.output_huffman_codes = self.huffman_functions.huffman(self.output)
        self.output_huffman_codes = self.change_to_numbering(self.output_huffman_codes)
        self.output = self.change_to_numbering(self.output)

    def main_2(self):
        self.result.append("\n\n## 2.1 \n\n")

        huffman_codes_table = self.print_codes(self.output_huffman_codes)
        self.result.append(huffman_codes_table)

        output_i_info, output_i_dict = self.I_info(self.output)
        self.result.append(output_i_info)

        output_h_info, output_h_val = self.H_info(self.output)
        self.result.append(output_h_info)

        output_r_info, output_r_val = self.R_info(
            self.output_huffman_codes, self.output
        )
        self.result.append(output_r_info)

        output_n_info, self.output_n_val = self.n_info(output_r_val, output_h_val)
        self.result.append(output_n_info)

    def main_3(self):
        self.result.append("\n\n## 2.2 \n\n")

        combinations_info, self.combinations_dict = self.get_combinations(self.output)
        self.result.append(combinations_info)

        (
            huffman_encoded_info,
            huffman_encoded_value,
        ) = self.huffman_functions.huffman_encode_pairs(self.combinations_dict)

        self.result.append(huffman_encoded_info)

        huffman_h_info, huffman_h_value = self.H_info(self.combinations_dict)

        self.result.append(huffman_h_info)

        huffman_r_info, huffman_r_value = self.R_info(
            huffman_encoded_value, self.combinations_dict
        )

        self.result.append(huffman_r_info)

        huffman_n_info, self.huffman_n_value = self.n_info(
            huffman_r_value, huffman_h_value
        )
        self.result.append(huffman_n_info)

        lines = self.brancher.get_huffman_lines()
        self.resulting_nodes, noding = self.brancher.splitting_huffman_lines(lines)

    def main_4(self):
        self.result.append("\n\n## 2.2.2 \n\n")

        self.brancher.save_tree_to_file(
            self.brancher.file_to_save, self.resulting_nodes
        )

    def main_5(self):
        self.result.append("\n\n## 2.3 \n\n")

        comb_same_length = self.turn_into_same_length(self.combinations_dict)

        comb_same_length_info = self.print_codes(comb_same_length)
        self.result.append(comb_same_length_info)

        comb_same_length_h_info, comb_same_length_h_value = self.H_info(
            # comb_same_length
            self.combinations_dict
        )
        self.result.append(comb_same_length_h_info)

        comb_same_length_r_info, comb_same_length_r_value = self.R_info(
            comb_same_length, self.combinations_dict
        )

        self.result.append(comb_same_length_r_info)

        comb_same_length_n_info, self.comb_same_length_n_value = self.n_info(
            comb_same_length_r_value, comb_same_length_h_value
        )
        self.result.append(comb_same_length_n_info)

    def main_6(self):
        self.result.append("\n\n ## 3 \n\n")

        (
            combinations_3_pair_info,
            combinations_3_pair_dict,
        ) = self.get_combinations_different(self.output, self.combinations_dict)

        self.result.append(combinations_3_pair_info)

        (
            huffman_encoded_info,
            huffman_encoded_value,
        ) = self.huffman_functions.huffman_encode_pairs(
            combinations_3_pair_dict, pairs=3
        )

        self.result.append(huffman_encoded_info)

        huffman_h_info, huffman_h_value = self.H_info(combinations_3_pair_dict)

        self.result.append(huffman_h_info)

        huffman_r_info, huffman_r_value = self.R_info(
            huffman_encoded_value, combinations_3_pair_dict
        )

        self.result.append(huffman_r_info)

        huffman_n_info, self.huffman_comb_3_n_value = self.n_info(
            huffman_r_value, huffman_h_value
        )

        self.result.append(huffman_n_info)

    def main_7(self):
        image_plotted = plotter(
            [self.output_n_val, self.huffman_n_value, self.huffman_comb_3_n_value]
        )


if __name__ == "__main__":
    assignment = Assignment2()
    assignment.main()
