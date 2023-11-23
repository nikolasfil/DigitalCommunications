from assignment_1_1 import main as main_1
from assignment_1_1 import *


def main():
    result = []

    letters_of_interest_frequency = {"0": 0.35, "1": 0.65}

    table_self_information_whole = print_table(
        letters_of_interest_frequency, letters_of_interest_frequency
    )
    result.append("\n".join(table_self_information_whole) + "\n\n")

    print("\n".join(result))

    save_to_file("assignment-1-3-code-result.md", result)


if __name__ == "__main__":
    main()
