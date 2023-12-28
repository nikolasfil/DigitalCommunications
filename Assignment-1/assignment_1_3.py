from assignment_1_1 import main as main_1
from assignment_1_1 import *
from assignment_1_2 import *


def I_x(x, y):
    """This function will return the self information of a given probability"""
    import math

    i_value = math.log2(1 / x)

    i_info = (
        "$$\nI(X) = -\log_2(p_i)"
        + f" = -\log_2({x})"
        + f" = {i_value}\n$$\n\nI(x) = {i_value}\n\n"
    )

    return i_info, i_value


def I_all(x, y):
    """This function will return the self information of a given probability"""
    import math

    i_value = math.log2(1 / x)

    i_info = (
        "$$\nI(X) = -\log_2(p_i)"
        + f" = -\log_2({x})"
        + f" = {i_value}\n$$\n\nI(x) = {i_value}\n\n"
    )

    return i_info, i_value


def print_ambiguous_table(dict):
    # beautifying
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
        temp += (
            f"({value_d}) * ({singles[key_d.split('|')[1]]}) * ({i_dict[key_d]}) + \\\ "
        )
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


def main(individual=False):
    result = []

    letters_of_interest_frequency = {"0": 0.35, "1": 0.65}

    table_self_information_whole = print_table(
        letters_of_interest_frequency, letters_of_interest_frequency, individual
    )
    result.append("\n".join(table_self_information_whole) + "\n\n")

    h_info, h_value = H([value for value in letters_of_interest_frequency.values()])

    result.append(h_info)

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

    # possible_combinations = {
    #     "x=0": 0.7,
    #     "x=1": 0.3,
    #     "y=0": 0.515,
    #     "y=1": 0.485,
    #     "y=0|x=0": 0.65,
    #     "y=0|x=1": 0.2,
    #     "y=1|x=0": 0.35,
    #     "y=1|x=1": 0.8,
    # }

    table_self_information_whole = print_ambiguous_table(possible_combinations)

    result.append("\n".join(table_self_information_whole) + "\n\n")

    print("\n".join(result))

    save_to_file("../MD_Reports/assignment-1/assignment-1-3-code-result.md", result)


if __name__ == "__main__":
    main()
