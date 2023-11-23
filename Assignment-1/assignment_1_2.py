from assignment_1_1 import main as main_1
from assignment_1_1 import * 

def H(list_of_probabilities):
    """This function will return the entropy of a given probability"""
    import math
    
    h_value = - sum([p*math.log2(p) for p in list_of_probabilities])
    
    h_info = "$$\nH(X) = -\sum_{i=1}^{"+f"{len(list_of_probabilities)}"+"}p_i\log_2(p_i)"
    
    # h_info+= f" = - (1/{len(list_of_probabilities)}) \cdot {len(list_of_probabilities)} \cdot \log_2(1/{len(list_of_probabilities)})" 

    h_info+=f" = {h_value}\n$$\n\nH(x) = {h_value}\n\n"

    return h_info,h_value


def H_singular(list_of_probabilities):
    """This function will return the entropy of a given probability"""
    import math
    
    h_value = - sum([p*math.log2(p) for p in list_of_probabilities])
    
    h_info = "$$\nH(X) = -\sum_{i=1}^{"+f"{len(list_of_probabilities)}"+"}p_i\log_2(p_i)"
    
    h_info+= f" = - (1/{len(list_of_probabilities)}) \cdot {len(list_of_probabilities)} \cdot \log_2(1/{len(list_of_probabilities)})" 

    h_info+=f" = {h_value}\n$$\n\nH(x) = {h_value}\n\n"

    return h_info,h_value
    

def main():
    letters_of_interest, letter_frequency, dict_of_interest = sharing_data(['L','h','l','H','s','n','w'],'poem.txt',True)
    result = []

    # print(letter_frequency)
    # Assignment 1.2
    # h_info, h_value = H(letter_frequency.values()) 


    table = print_table(letter_frequency ,letter_frequency)
    # print()
    result.append('\n'.join(table)+'\n\n')

    # removing the symbol from the dictionary
    letter_frequency = {key:value for key,value in letter_frequency.items() if key != 'symbol'}

    h_info, h_value = H([value/sum(letter_frequency.values()) for value in letter_frequency.values()]) 

    # N = len(letter_frequency.keys())
    # h_info, h_value = H([1/N for _ in range(N)]) 


    result.append(h_info)

    # print(result)

    # ------------------

    save_to_file('assignment-1-2-code-result.md',result)

if __name__ == "__main__":
    main()