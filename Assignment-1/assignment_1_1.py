#!/bin/python

from collections import defaultdict
import math


def getting_info_from_file(file):
    """This function will return a dictionary with the frequency of each letter in the file"""
    letter_frequency=defaultdict(int)
    with open('poem.txt','r') as file:
        for line in file:
            for letter in line:
                if letter.isalpha():
                    letter_frequency[letter]+=1
                elif letter!='\n':
                    letter_frequency["symbol"]+=1
    return letter_frequency
    
def letters_of_interest_frequency(letters_of_interest,letter_frequency):
    """This function will return a dictionary with the frequency of each letter of interest of a given dictionary"""
    return {key:letter_frequency[key] for key in letters_of_interest}


def print_table(dict_of_interest,letter_frequency):
    # total number of letters in the file
    N = sum(dict_of_interest.values())

    # the table headers
    result =[ f'| Letter | Count | P = Count/N | I= -log2(P) |']

    for key,value in dict_of_interest.items():
        
        information = f'{(-1*math.log2(value/N))}'
        probability = f'{value/N}'

        result.append(f'| {key} | {value} | {information} | {probability} |')

    result.append(f'| {"Number of Letters"} | {N} | | | ' )    
    result.append(f'| {"Number of Symbols"} | {letter_frequency["symbol"]} | | | ' )
    result.append(f'| {"Number of Characters"} | {letter_frequency["symbol"]+N} | | | ' )

    return result

def main():

    # list of the characters that interest us 
    letters_of_interest=['L','h','l','H','s','n','w']
    # dictionary with the frequency of each letter in the file
    letter_frequency=getting_info_from_file('poem.txt')
    
  
    # dictionary with the frequency of each letter of interest
    dict_of_interest = letters_of_interest_frequency(letters_of_interest,letter_frequency)

    # printing the table
    result = print_table(dict_of_interest,letter_frequency)
    
    print('\n'.join(result))

    with open('assignment-1-code-result.md','w') as file:
        file.write('\n\n')
        file.write('\n'.join(result))

    
if __name__ == '__main__':
    main()