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


def H(list_of_probabilities):
    """This function will return the entropy of a given probability"""
    import math

    h_value = -sum([p * math.log2(p) for p in list_of_probabilities])
    h_value = round(h_value, 3)
    h_info = (
        "$$\nH(X) = -\sum_{i=1}^{" + f"{len(list_of_probabilities)}" + "}p_i\log_2(p_i)"
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


def main(individual=False):
    # def main_1(individual=False):
    #  --------------- A --------------------------
    result = []

    file = Path(Path(__file__).parent, "words.txt")

    with open(file, "r") as f:
        data = f.read().strip("\n")

    letters_of_interest, letter_frequency, dict_of_interest = sharing_data(
        list("αβγδ"), file, individual
    )

    # printing the table
    table = print_table(dict_of_interest, letter_frequency, individual)

    table = "\n".join(table)

    result.append(table)

    n_letter = sum(letter_frequency.values())

    output = {key: (value / n_letter) for key, value in letter_frequency.items()}

    h_info, h_value = H(list(output.values()))

    output = {
        key: round(value / n_letter, 3) for key, value in letter_frequency.items()
    }

    result.append(h_info)

    result.append("\n\n---\n\n")

    #  --------------- B --------------------------

    # Assignment 2 3
    result.append("\n\n## Assignment-5-1-a\n\n")

    combinations_dict = output

    comb_same_length = turn_into_same_length(combinations_dict)
    comb_same_length = {key: value[1:] for key, value in comb_same_length.items()}
    # print(comb_same_length)

    comb_same_length_info = print_codes(comb_same_length)
    result.append(comb_same_length_info)

    # Data encoding with code of the same length :

    # print(comb_same_length)

    comb_data_encoding = "".join([comb_same_length[key] for key in data])
    result.append(
        f"\n\nData encoding with code of the same length : \n\n {data} -> \n\n\{comb_data_encoding}\n\n"
    )

    # comb_sl_h_info, comb_sl_h_value = H_info(combinations_dict)
    # result.append(comb_sl_h_info)

    # comb_sl_r_info, comb_sl_r_value = R_info(comb_same_length, combinations_dict)
    # result.append(comb_sl_r_info)

    # comb_sl_n_info, comb_sl_n_value = n_info(comb_sl_r_value, comb_sl_h_value)
    # result.append(comb_sl_n_info)

    result.append("\n\n---\n\n")

    #     return result, comb_same_length

    #  --------------- C --------------------------

    combinations_info, combinations = get_combinations(letter_frequency)
    # result.append(combinations_info)

    # comb_same_length_info = print_codes(comb_same_length)
    # result.append(comb_same_length_info)

    #     return result

    # --------------- Results  --------------------
    print("\n".join(result))

    save_to_file("../MD_Reports/assignment-5/assignment-5-1-code-result.md", result)


if __name__ == "__main__":
    main()
