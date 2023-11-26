#!/bin/python

from collections import defaultdict
import math


def getting_info_from_file(file, individual=False):
    """This function will return a dictionary with the frequency of each letter in the file"""
    letter_frequency = defaultdict(int)
    with open("poem.txt", "r") as file:
        for line in file:
            for letter in line:
                letter_frequency[letter] += 1
    letter_frequency["newLine"] = letter_frequency.pop("\n")
    return letter_frequency


def letters_of_interest_frequency(letters_of_interest, letter_frequency):
    """This function will return a dictionary with the frequency of each letter of interest of a given dictionary"""
    return {key: letter_frequency[key] for key in letters_of_interest}


def number_of_symbols(letter_frequency):
    """Returns the number of symbols in the dictionary"""
    summ = [
        letter_frequency[key] for key in letter_frequency.keys() if not key.isalpha()
    ]
    return sum(summ)


def print_table(dict_of_interest, letter_frequency, individual=False):
    # total number of letters in the file
    N = sum(letter_frequency.values())
    n_symbols = number_of_symbols(letter_frequency)
    n_letters = N - n_symbols

    # beautifying the Markdown table
    ln = len("Number of Characters") + 2

    # the table headers
    result = [
        f'| {"Letter":^{ln}} | {"Count":^{ln}} | {"P = Count/N":^{ln}} | {"I= -log2(P)":^{ln}} |',
        f'| {"-":^{ln}} | {"-":^{ln}} | {"-":^{ln}} | {"-":^{ln}} |',
    ]

    for key, value in dict_of_interest.items():
        information = f"{(-1*math.log2(value/N))}"
        probability = f"{value/N}"

        result.append(
            f"| {key:^{ln}} | {value:^{ln}} | {probability:^{ln}} | {information:^{ln}} |"
        )

    result.append(
        f'| {"Number of Letters":^{ln}} | {N:^{ln}} | {"":^{ln}} | {"":^{ln}} | '
    )
    result.append(
        f'| {"Number of Symbols":^{ln}} | {n_symbols:^{ln}} | {"":^{ln}} | {"":^{ln}} | '
    )
    result.append(
        f'| {"Number of Characters":^{ln}} | {n_letters:^{ln}} | {"":^{ln}} | {"":^{ln}} | '
    )

    return result


def sharing_data(letters_of_interest, poem_file, individual=False):
    # dictionary with the frequency of each letter in the file
    letter_frequency = getting_info_from_file(poem_file, individual)

    # dictionary with the frequency of each letter of interest
    dict_of_interest = letters_of_interest_frequency(
        letters_of_interest, letter_frequency
    )

    return letters_of_interest, letter_frequency, dict_of_interest


def save_to_file(file_name, result):
    with open(file_name, "w") as file:
        file.write("\n\n")
        file.write("\n".join(result))


def main(individual=False):
    letters_of_interest, letter_frequency, dict_of_interest = sharing_data(
        ["L", "h", "l", "H", "s", "n", "w"], "poem.txt", individual
    )

    # printing the table
    result = print_table(dict_of_interest, letter_frequency, individual)

    print("\n".join(result))

    save_to_file("assignment-1-1-code-result.md", result)


if __name__ == "__main__":
    main()
