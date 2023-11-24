from huffman import *
from huffman_tree import *
from efficiency_plotter import *


def main():
    output = {"a": 0.53, "b": 0.37, "c": 0.10}
    codes = huffman(output)

    output = change_to_letters(output)
    codes = change_to_letters(codes)

    # Assignment 1

    assignment_1_header = "\n\n## Assignment-1\n\n"
    pretty_codes = print_codes(codes)
    i_info = print_I_info(output)
    h_info, h_value = print_H_info(output)
    r_info, r_value = print_R_info(codes, output)
    n_info, n_value = print_n_info(r_value, h_value)

    # ----------------------- Assignment 2 --------------------
    assignment_2_header = "\n\n## Assignment-2\n\n"

    combinations_info, combinations_dict = get_combinations(output)

    huffman_encoded_info, huffman_encoded_value = huffman_encode_pairs(
        combinations_dict
    )

    huffman_r_info, huffman_r_value = print_R_info(
        huffman_encoded_value, combinations_dict
    )

    huffman_h_info = (
        "$$\n H(x) = 2 H(x) = 2 \cdot "
        + f"{h_value} = {2*h_value} \n$$\n\nH(x) = {2*h_value}\n"
    )

    huffman_n_info, huffman_n_value = print_n_info(huffman_r_value, h_value, 2)

    # assignment 2 - 3

    combinations_3_pair_info, combinations_3_pair_dict = get_combinations_different(
        output, combinations_dict
    )

    huff_encoded_3_pair_info, huff_encoded_3_pair_dict = huffman_encode_pairs(
        combinations_3_pair_dict, 3
    )

    huff_encoded_3_pair_r_info, huff_encoded_3_pair_r_dict = print_R_info(
        huff_encoded_3_pair_dict, combinations_3_pair_dict
    )

    huff_encoded_3_h_info = (
        "$$\n H(x) = 3 H(x) = 2 \cdot "
        + f"{h_value} = {2*h_value} \n$$\n\nH(x) = {2*h_value}\n"
    )

    huff_encoded_3_n_info, huff_encoded_3_n_value = print_n_info(
        huff_encoded_3_pair_r_dict, h_value, 3
    )

    image_plotted = plotter([n_value, huffman_n_value, huff_encoded_3_n_value])
    print([n_value, huffman_n_value, huff_encoded_3_n_value])

    # ----------------------- General -----------------------

    lst = [
        assignment_1_header,
        pretty_codes,
        i_info,
        h_info,
        r_info,
        n_info,
        assignment_2_header,
        combinations_info,
        huffman_encoded_info,
        huffman_r_info,
        huffman_h_info,
        huffman_n_info,
        combinations_3_pair_info,
        huff_encoded_3_pair_info,
        huff_encoded_3_pair_r_info,
        huff_encoded_3_h_info,
        huff_encoded_3_n_info,
        image_plotted,
    ]
    result = "\n\n".join(lst)

    # print(result)
    write_to_file(result)


if __name__ == "__main__":
    main()
