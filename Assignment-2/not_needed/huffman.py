import math
from huffman_tree import *


def huffman(output):
    # output: dictionary of output symbols and their probabilities
    # return: dictionary of output symbols and their huffman codes

    # sort output symbols by probability
    output = sorted(output.items(), key=lambda x: x[1], reverse=True)
    output = dict(output)
    # create a list of nodes
    nodes = []
    for key in output:
        nodes.append([key, output[key]])
    # create a list of codes
    codes = {}
    for key in output:
        codes[key] = ""
    # create a huffman tree

    while len(nodes) > 1:
        # sort nodes by probability
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        # combine two nodes with the smallest probabilities
        node1 = nodes.pop()
        node2 = nodes.pop()
        combined_node = [node1[0], node2[0]]
        nodes.append([combined_node, node1[1] + node2[1]])
        print(f"Node Tree: {len(nodes)} {nodes}")
        # update codes
        for symbol in node1[0]:
            codes[symbol] = "0" + codes[symbol]
        for symbol in node2[0]:
            codes[symbol] = "1" + codes[symbol]

    return codes


def print_I_info(output):
    result = "| I | Log |\n| --- | --- |\n"
    for key, value in output.items():
        # do -log2(value )
        result += f"| I<sub>{key}</sub> | {-1*math.log2(value)} |\n"

    return result


def print_codes(codes):
    result = "| Symbol | Code |\n"
    for key, value in codes.items():
        result += f"| {key} | {value} |\n"
    return result


def change_to_letters(dictionary):
    result = {}
    for i, value in enumerate(dictionary.values()):
        result[f"a{i+1}"] = value
    return result


def change_to_numbering(dictionary, letters):
    result = {}
    letters = list(letters.keys())
    for i, value in enumerate(dictionary.values()):
        result[letters[i]] = value
    return result


def change_to_single_letter(dictionary):
    result = {}
    for i, value in enumerate(dictionary.values()):
        result[f"{chr(97+i)}"] = value
    return result


def print_H_info(output):
    val = 0
    H = "$$\n H(x) = "
    for key in output.keys():
        # H+=f"I<sub>{key}</sub> * P<sub>{key}</sub> + "
        H += "I_{" + f"{key}" + "} \cdot P_{" + f"{key}" + "} + "
    # H = H[:-2]
    H += " = "
    # round to 3 decimal places
    for key, value in output.items():
        I = round(-1 * math.log2(value), 3)
        val += (I) * value
        # H+=f"{I} * {value}+"
        H += f"{I} \cdot {value}+"

        # H+=f"{(-1*math.log2(value))}*{value}+"
        # val += (-1*math.log2(value))*value

    H = H[:-1]
    # round to 3 decimal places
    val = round(val, 3)
    H += f" = {val} \n$$ \n\nH(x) = {val}\n"
    return H, val


def print_R_info(codes, output):
    val = 0
    R = "$$\n R(x) = "
    for key, value in codes.items():
        # R+=f"{output[key]} * {len(str(value))} + "
        R += f"{output[key]} \cdot {len(str(value))} + "
        val += output[key] * len(str(value))
    R = R[:-2]
    val = round(val, 3)
    R += f" = {val} \n$$ \n\nR(x) = {val}\n"
    return R, val


def print_n_info(r, h, pairs=1):
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

    result = "\n\n| Combination | Probability |\n"
    for key, value in result_dict.items():
        result += f"| {key} | {value} |\n"
    return result, result_dict


def get_combinations_different(output1, output2):
    result_list = []
    for key_a in output1.keys():
        for key_b in output2.keys():
            result_list.append((key_a, key_b))
    result_dict = {}
    for key in result_list:
        result_dict["".join(key)] = round(output1[key[0]] * output2[key[1]], 3)

    result = "\n\n| Combination | Probability |\n"
    for key, value in result_dict.items():
        result += f"| {key} | {value} |\n"
    return result, result_dict


def write_to_file(listing):
    with open("code_result.md", "w", encoding="UTF-8") as f:
        f.write(listing)


def huffman_encode_pairs(combinations_dict, pairs=2):
    """Returns the encoded huffman codes for the combinatios of x pairs"""
    result = ""
    huffman_encoded = huffman_encoding(combinations_dict)
    huffman_pairs_encoded = {
        key: value for key, value in huffman_encoded.items() if len(key) == 2 * pairs
    }
    result = "\n\n| Combination | Code |\n"
    for key in sorted(huffman_pairs_encoded.keys()):
        temp_result = f"| {key} | {huffman_pairs_encoded[key]} | "
        result += temp_result + "\n"

    return result, huffman_pairs_encoded
