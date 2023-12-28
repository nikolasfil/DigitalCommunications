import math
from assignment_2_huffman_functions import *
from efficiency_plotter import *
from huffman_brancher import *

# class Assignment2:
# change the whole file into


def save_to_file(file_name, result):
    with open(file_name, "w") as file:
        file.write("\n\n")
        file.write("\n".join(result))


def change_to_numbering(dictionary):
    result = {}
    for i, value in enumerate(dictionary.values()):
        result[f"a{i+1}"] = value
    return result


def change_to_letters(dictionary):
    result = {}
    for i, value in enumerate(dictionary.values()):
        result[chr(97 + i)] = value
    return result


def print_codes(codes):
    result = f"| {'Symbol':^15} | {'Code':^15} |\n| {'-':^15} | {'-':^15} |\n"
    for key, value in codes.items():
        result += f"| {key:^15} | {value:^15} |\n"
    return result


def I_info(output):
    result = f"| {'I':^14} | {'Log':^15} |\n |{'-':^14} | {'-':^15} |\n"
    i_dict = {}
    for key, value in output.items():
        # do -log2(value )
        val = -1 * math.log2(value)
        val = round(val, 3)
        result += f"| I<sub>{key}</sub> | {val:^15} |\n"
        i_dict[key] = val

    return result, i_dict


def H_info(output):
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


def R_info(codes, output):
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


def n_info(r, h, pairs=1):
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


def get_combinations(output):
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


def get_combinations_different(output1, output2):
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


def same_length_coding(codes):
    # length = max([len(str(bin(key))) for key in codes.keys()])
    length = len(str(bin(len(codes.keys())))[2:])
    return length


def turn_into_same_length(codes):
    length = same_length_coding(codes)
    result = {}
    for i, key in enumerate(codes.keys()):
        result[key] = str(bin(i))[2:].zfill(length)
    return result


def main():
    result = []
    output = {"a1": 0.53, "a2": 0.37, "a3": 0.10}
    output = change_to_letters(output)

    output_huffman_codes = huffman(output)
    output_huffman_codes = change_to_numbering(output_huffman_codes)
    output = change_to_numbering(output)

    result.append("## Assignment-2-1\n\n")

    output_huffman_codes_table = print_codes(output_huffman_codes)
    result.append(output_huffman_codes_table)

    output_i_info, output_i_dict = I_info(output)
    result.append(output_i_info)

    output_h_info, output_h_value = H_info(output)
    result.append(output_h_info)

    output_r_info, output_r_value = R_info(output_huffman_codes, output)
    result.append(output_r_info)

    output_n_info, output_n_value = n_info(output_r_value, output_h_value)
    result.append(output_n_info)

    result.append("## Assignment-2-2\n\n")

    combinations_info, combinations_dict = get_combinations(output)
    result.append(combinations_info)

    huffman_encoded_info, huffman_encoded_value = huffman_encode_pairs(
        combinations_dict
    )

    result.append(huffman_encoded_info)

    huffman_h_info, huffman_h_value = H_info(combinations_dict)
    result.append(huffman_h_info)

    huffman_r_info, huffman_r_value = R_info(huffman_encoded_value, combinations_dict)

    result.append(huffman_r_info)

    huffman_n_info, huffman_n_value = n_info(huffman_r_value, huffman_h_value)
    result.append(huffman_n_info)

    lines = get_huffman_lines()
    resulting_nodes, noding = splitting_huffman_lines(lines)

    # Assignment 2 2

    result.append("\n\n## Assignment-2-2-2\n\n")

    save_tree_to_file("assignment_2_huffman_tree_1.md", resulting_nodes)

    # Assignment 2 3
    result.append("\n\n## Assignment-2-3\n\n")

    comb_same_length = turn_into_same_length(combinations_dict)

    comb_same_length_info = print_codes(comb_same_length)
    result.append(comb_same_length_info)

    comb_sl_h_info, comb_sl_h_value = H_info(combinations_dict)
    result.append(comb_sl_h_info)

    comb_sl_r_info, comb_sl_r_value = R_info(comb_same_length, combinations_dict)
    result.append(comb_sl_r_info)

    comb_sl_n_info, comb_sl_n_value = n_info(comb_sl_r_value, comb_sl_h_value)
    result.append(comb_sl_n_info)

    # Assignment-3
    result.append("\n\n## Assignment-3\n\n")

    combinations_3_pair_info, combinations_3_pair_dict = get_combinations_different(
        output, combinations_dict
    )
    result.append(combinations_3_pair_info)

    huff_encoded_3_pair_info, huff_encoded_3_pair_dict = huffman_encode_pairs(
        combinations_3_pair_dict, 3
    )
    result.append(huff_encoded_3_pair_info)

    huff_encoded_3_pair_h_info, huff_encoded_3_pair_h_value = H_info(
        combinations_3_pair_dict
    )
    result.append(huff_encoded_3_pair_h_info)

    huff_encoded_3_pair_r_info, huff_encoded_3_pair_r_value = R_info(
        huff_encoded_3_pair_dict, combinations_3_pair_dict
    )
    result.append(huff_encoded_3_pair_r_info)

    huff_encoded_3_pair_n_info, huff_encoded_3_pair_n_value = n_info(
        huff_encoded_3_pair_r_value, huff_encoded_3_pair_h_value
    )

    result.append(huff_encoded_3_pair_n_info)

    image_plotted = plotter(
        [output_n_value, huffman_n_value, huff_encoded_3_pair_n_value]
    )

    print("\n\n".join(result))
    from pathlib import Path

    parent_folder = Path(__file__).parent
    root_folder = Path(parent_folder, "../MD_Reports")
    file = Path(root_folder, "assignment-2", "assignment-2-code-results.md")
    # save_to_file("../MD_Reports/assignment-2-code-results.md", result)
    save_to_file(file, result)


if __name__ == "__main__":
    main()
