from assignment_1_1 import main as main_1
from assignment_1_1 import *


def H(list_of_probabilities):
    """This function will return the entropy of a given probability"""
    import math

    h_value = -sum([p * math.log2(p) for p in list_of_probabilities])
    h_value = round(h_value, 3)
    h_info = (
        "$$\nH(X) = -\sum_{i=1}^{" + f"{len(list_of_probabilities)}" + "}p_i\log_2(p_i)"
    )

    h_info += f" = {h_value}\n$$\n\nH(x) = {h_value}\n\n"

    return h_info, h_value


def main(individual=False):
    letters_of_interest, letter_frequency, dict_of_interest = sharing_data(
        ["L", "h", "l", "H", "s", "n", "w"], "poem.txt", individual
    )
    result = []

    table_self_information_whole = print_table(
        letter_frequency, letter_frequency, individual
    )
    # print()
    result.append("\n".join(table_self_information_whole) + "\n\n")

    h_info, h_value = H(
        [value / sum(letter_frequency.values()) for value in letter_frequency.values()]
    )

    result.append(h_info)

    print("\n".join(result))

    # ------------------

    save_to_file("../MD_Reports/assignment-1-2-code-result.md", result)


if __name__ == "__main__":
    main(True)
