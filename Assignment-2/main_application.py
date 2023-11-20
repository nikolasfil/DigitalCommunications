from huffman import * 
from huffman_tree import * 


def main():
    output = {"a": 0.53, "b": 0.37, "c": 0.10}
    codes = huffman(output)


    output = change_to_letters(output)
    codes = change_to_letters(codes)


    # Assignment 1

    assignment_1_header = "\n\n## Assignment-1\n\n"
    pretty_codes = print_codes(codes)
    i_info = print_I_info(output)
    h_info, h_value = print_H_info(output)
    r_info, r_value = print_R_info(codes,output)
    n_info = print_n_info(r_value,h_value)
    

    # Assignment 2 
    assignment_2_header = "\n\n## Assignment-2\n\n"

    combinations_info,combinations_dict = get_combinations(output)


    combinations_single_letter = change_to_single_letter(combinations_dict)

    c_dict_original = change_to_numbering(combinations_single_letter,combinations_dict)


    # codes_2 = huffman(combinations_single_letter)
    
    # codes_2 = change_to_numbering(codes_2,combinations_dict)

    # print(codes_2)

    huffman_encoded = huffman_encoding(combinations_single_letter)
    # print(huffman_encoded)


    # General

    lst = [assignment_1_header,pretty_codes,i_info,h_info,r_info,n_info, assignment_2_header,combinations_info]

    result = "\n\n".join(lst)

    # print(result)
    write_to_file(result)


if __name__ == "__main__":
    main()
