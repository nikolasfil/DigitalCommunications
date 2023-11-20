#!/bin/python

from collections import defaultdict

def pretty_dict(dic):
    result =[ '| Letter | Count |']
    # print('| Letter | Count |')
    ll = len('Letter')
    lc = len('Count')

    for key,value in dic.items():
        result.append(f'| {key:^{ll}} | {value:^{lc}} |')
        # print(f'| {key:^{ll}} | {value:^{lc}} |')
    return result

def getting_info_from_file(file):
    letter_frequency=defaultdict(int)
    with open('poem.txt','r') as file:
        for line in file:
            for letter in line:
                if letter.isalpha():
                    letter_frequency[letter]+=1
    return letter_frequency

def letters_of_interest_frequency(letters_of_interest,letter_frequency):
    return {key:letter_frequency[key] for key in letters_of_interest}

def self_information(letters_of_interest, letter_frequency):
    dict_of_interest = letters_of_interest_frequency(letters_of_interest,letter_frequency)

    lister = pretty_dict(dict_of_interest)
    
    N = sum(dict_of_interest.values())
    p = defaultdict(int)
    logs = defaultdict(int)
    for key,value in letter_frequency.items():
        p[key] = value/N
        logs[key] = -1*p[key]*math.log2(p[key])
    

def main():

    letters_of_interest=['L','h','l','H','s','n','w']
    letter_frequency=getting_info_from_file('poem.txt')
    
if __name__ == '__main__':
    main()