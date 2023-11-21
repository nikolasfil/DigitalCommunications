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

    # printing the table
    ll,lc,li,lp = len('Letter'),len('Count'),len('I= -log2(P)'),len('P = Count/N')

    for key,value in dict_of_interest.items():
        lc = max(lc,len(str(value)))
        li = max(li,len(str(-1*math.log2(value/N))))
        lp = max(lp,len(str(value/N)))
    
    # the table headers
    result =[ f'| {"Letter":^{1}} | {"Count":^{lc}} | {"P = Count/N":^{lp}} | {"I= -log2(P)":^{li+1}} |']

    for key,value in dict_of_interest.items():
        
        letter = f'{key:^{ll}}'
        frequency = f'{value:^{lc}}'
        information = f'{(-1*math.log2(value/N)):^{li+1}.2f}'
        probability = f'{value/N:^{lp}}'

        result.append(f'| {letter} | {frequency} | {information} | {probability} |')


    # printing the total number of letters
    result.append(f'| {"Number of Letters"} | {N:^{li}} | | | ' )
    
    # printing the total number of symbols
    result.append(f'| {"Number of Symbols"} | {letter_frequency["symbol"]:^{li}} | | | ' )
    
    result.append(f'| {"Number of Characters"} | {letter_frequency["symbol"]+N:^{li}} | | | ' )

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