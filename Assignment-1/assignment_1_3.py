from assignment_1_1 import main as main_1
from assignment_1_1 import * 

    

def main():
    letters_of_interest, letter_frequency, dict_of_interest = sharing_data(['L','h','l','H','s','n','w'],'poem.txt')

    result = []

    save_to_file('assignment-1-3-code-result.md',result)

if __name__ == "__main__":
    main()