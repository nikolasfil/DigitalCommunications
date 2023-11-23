#!/bin/python

from collections import defaultdict
import math


def getting_info_from_file(file, individual=False):
    """This function will return a dictionary with the frequency of each letter in the file"""
    letter_frequency = defaultdict(int)
    with open("poem.txt", "r") as file:
        for line in file:
            for letter in line:
                if letter.isalpha():
                    letter_frequency[letter] += 1
                elif letter != "\n":
                    if individual:
                        letter_frequency[letter] += 1
                    letter_frequency["symbol"] += 1
    return letter_frequency


def letters_of_interest_frequency(letters_of_interest, letter_frequency):
    """This function will return a dictionary with the frequency of each letter of interest of a given dictionary"""
    return {key: letter_frequency[key] for key in letters_of_interest}


def print_table(dict_of_interest, letter_frequency):
    # total number of letters in the file
    N = sum(letter_frequency.values())

    # beautifying
    ln = len("Number of Characters") + 2

    # the table headers
    result = [
        f'| {"Letter":^{ln}} | {"Count":^{ln}} | {"P = Count/N":^{ln}} | {"I= -log2(P)":^{ln}} |'
    ]

    for key, value in dict_of_interest.items():
        if key == "symbol":
            continue
        information = f"{(-1*math.log2(value/N))}"
        # print(value, N)
        probability = f"{value/N}"

        result.append(
            f"| {key:^{ln}} | {value:^{ln}} | {probability:^{ln}} | {information:^{ln}} |"
        )

    result.append(
        f'| {"Number of Letters":^{ln}} | {N:^{ln}} | {"":^{ln}} | {"":^{ln}} | '
    )
    if "symbol" in letter_frequency:
        result.append(
            f'| {"Number of Symbols":^{ln}} | {letter_frequency["symbol"]:^{ln}} | {"":^{ln}} | {"":^{ln}} | '
        )
        result.append(
            f'| {"Number of Characters":^{ln}} | {letter_frequency["symbol"]+N:^{ln}} | {"":^{ln}} | {"":^{ln}} | '
        )

    return result


def sharing_data(letters_of_interest, poem_file, individual=False):
    # list of the characters that interest us
    # letters_of_interest=
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


def main():
    letters_of_interest, letter_frequency, dict_of_interest = sharing_data(
        ["L", "h", "l", "H", "s", "n", "w"], "poem.txt"
    )

    # printing the table
    result = print_table(dict_of_interest, letter_frequency)

    print("\n".join(result))

    save_to_file("assignment-1-1-code-result.md", result)


if __name__ == "__main__":
    main()
