

def H(list_of_probabilities):
    """This function will return the entropy of a given probability"""
    import math
    
    h_value = - sum([-1*p*math.log2(p) for p in list_of_probabilities])
    
    h_info = "\n H(X) = $-\sum_{i=1}^{n}p_i\log_2(p_i)$ \n\n"

    return h_info,h_value

    

def main():
    pass 


if __name__ == "__main__":
    main()